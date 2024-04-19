import subprocess
import pandas as pd

# Load the PVT data
not_data = pd.read_csv('../data/not_data.csv')
not_data = not_data.dropna()

def run_leakage_simulation(not_row):
    netlist = f"""
    .include ../netlists/not_leakage.net
    .PARAM Vin={not_row['Vin']}
    .PARAM pvdd={not_row['pvdd']}

    .PARAM toxe_n={not_row['toxe_n']}
    .PARAM toxm_n={not_row['toxm_n']}
    .PARAM toxref_n={not_row['toxref_n']}
    .PARAM ndep_n={not_row['ndep_n']}
    .PARAM xj_n={not_row['xj_n']}
    .PARAM toxp_par={not_row['toxp_par']}
    .PARAM toxe_p={not_row['toxe_p']}
    .PARAM toxm_p={not_row['toxm_p']}
    .PARAM toxref_p={not_row['toxref_p']}
    .PARAM ndep_p={not_row['ndep_p']}
    .PARAM xj_p={not_row['xj_p']}
    .PARAM lmin={not_row['lmin']}
    .PARAM wmin={not_row['wmin']}
    
    .temp {not_row['temp']}
    .CONTROL
        dc temp {not_row['temp']} {not_row['temp']} 1
        print ((-V(node1)*I(Vdd)) + (-V(nodea)*I(Vina)))
    .ENDC
    .END
    """
    with open('../netlists/not_leakage.sp', 'w') as f:
        f.write(netlist)
    
    # subprocess.run(['ngspice', '-b', 'nor2_leakage.sp'])
    command = "ngspice -b ../netlists/not_leakage.sp > ../netlists/not_leakage.txt"
    subprocess.run(command, shell=True)

    # with open('nor2_leakage.txt', 'r') as f:
    #     lines = f.readlines()
    #     parsed_data = {}
    #     for line in lines:
    #         if '=' in line:
    #             key, value = line.split('=')
    #             key = key.strip()
    #             value = float(value.strip())
    #             parsed_data[key] = value
    #     leakage_power = parsed_data.get('(-v(node1)*i(vdd))', 0.0)

    with open('../netlists/not_leakage.txt', 'r') as f:
        # Read last line of the file
        lines = f.readlines()
        last_line = lines[-1]
        key, value = last_line.split('=')
        leakage_power = float(value.strip())
    return leakage_power

def run_delay_simulation(not_row):
    val = not_row['pvdd']/2
    netlist = f"""
    .include ../netlists/not_delay.net
    .param temp={not_row['temp']}
    .param pvdd={not_row['pvdd']}
    .param Vin={not_row['Vin']}
    .param toxe_n={not_row['toxe_n']}
    .param toxm_n={not_row['toxm_n']}
    .param toxref_n={not_row['toxref_n']}
    .param toxe_p={not_row['toxe_p']}
    .param toxm_p={not_row['toxm_p']}
    .param toxref_p={not_row['toxref_p']}
    .param toxp_par={not_row['toxp_par']}
    .param xj_n={not_row['xj_n']}
    .param xj_p={not_row['xj_p']}
    .param ndep_n={not_row['ndep_n']}
    .param ndep_p={not_row['ndep_p']}
    .PARAM lmin={not_row['lmin']}
    .PARAM wmin={not_row['wmin']}
    cqload nodeZ 0 {not_row['cqload']}

    .temp {not_row['temp']}

    *Definition of type of analysis

    .TRAN 0.1n 42n

    .meas tran delay_lh_nodea trig v(nodea) val={val} fall={not_row['pvdd']} targ v(nodeZ) val={val} rise={not_row['pvdd']}
    .meas tran delay_hl_nodea trig v(nodea) val={val} rise={not_row['pvdd']} targ v(nodeZ) val={val} fall={not_row['pvdd']}

    .CONTROL
        run
    .ENDC

    .END
    """

    with open('../netlists/nor2_delay.sp', 'w') as f:
        f.write(netlist)

    command = "ngspice -b ../netlists/nor2_delay.sp > ../netlists/nor2_delay.txt"
    subprocess.run(command, shell=True)
  
    # Tokenization
    with open('../netlists/nor2_delay.txt', 'r') as f:
        lines = f.readlines()
        # Initialize list to store tokens
        tokens = []
        # Iterate over each line
        for line in lines:
            # Tokenize each line using spaces as delimiters
            words = line.split()
            # Iterate over each word in the line
            for word in words:
                # Append word to tokens list
                tokens.append(word)
        # Find index of the first occurrence of 'delay_lh_nodea'
        index_delay_lh_nodea = tokens.index('delay_lh_nodea')
        # Find index of the first occurrence of 'delay_hl_nodea'
        index_delay_hl_nodea = tokens.index('delay_hl_nodea')
        # Extract values from tokens
        delay_lh_nodea = float(tokens[index_delay_lh_nodea + 2])
        delay_hl_nodea = float(tokens[index_delay_hl_nodea + 2])

    return delay_lh_nodea, delay_hl_nodea

# Initialize list to store individual DataFrame results
results_list = []

# Iterate over each PVT sample and run simulations
for index, not_row in not_data.iterrows():
    leakage_power = run_leakage_simulation(not_row)
    delay_lh_nodea, delay_hl_nodea = run_delay_simulation(not_row)
    result_row = {
        'Vin': not_row['Vin'],
        'temp': not_row['temp'],
        'pvdd': not_row['pvdd'],
        'cqload': not_row['cqload'],
        'lmin': not_row['lmin'],
        'wmin': not_row['wmin'],
        'toxe_n': not_row['toxe_n'],
        'toxm_n': not_row['toxm_n'],
        'toxref_n': not_row['toxref_n'],
        'toxe_p': not_row['toxe_p'],
        'toxm_p': not_row['toxm_p'],
        'toxref_p': not_row['toxref_p'],
        'toxp_par': not_row['toxp_par'],
        'xj_n': not_row['xj_n'],
        'xj_p': not_row['xj_p'],
        'ndep_n': not_row['ndep_n'],
        'ndep_p': not_row['ndep_p'],
        'leakage': leakage_power,
        'delay_LH_NodeA': delay_lh_nodea,
        'delay_HL_NodeA': delay_hl_nodea,
    }
    results_list.append(pd.DataFrame([result_row]))  # Append individual DataFrame

# Concatenate all individual DataFrames into one final DataFrame
results = pd.concat(results_list, ignore_index=True)

# Save results to CSV file
results.to_csv('../outputs/simulation_results_not.csv', index=False)