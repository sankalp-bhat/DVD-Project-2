import subprocess
import pandas as pd

# Load the PVT data
pvt_data = pd.read_csv('../../data/pvt_data.csv')
pvt_data = pvt_data.dropna()

def run_leakage_simulation(pvt_row):
    netlist = f"""
    .include ../netlists/nor2_leakage.net
    .PARAM Vin_A={pvt_row['Vin_A']}
    .PARAM Vin_B={pvt_row['Vin_B']}
    .PARAM pvdd={pvt_row['pvdd']}

    .PARAM toxe_n={pvt_row['toxe_n']}
    .PARAM toxm_n={pvt_row['toxm_n']}
    .PARAM toxref_n={pvt_row['toxref_n']}
    .PARAM ndep_n={pvt_row['ndep_n']}
    .PARAM xj_n={pvt_row['xj_n']}
    .PARAM toxp_par={pvt_row['toxp_par']}
    .PARAM toxe_p={pvt_row['toxe_p']}
    .PARAM toxm_p={pvt_row['toxm_p']}
    .PARAM toxref_p={pvt_row['toxref_p']}
    .PARAM ndep_p={pvt_row['ndep_p']}
    .PARAM xj_p={pvt_row['xj_p']}
    .PARAM lmin={pvt_row['lmin']}
    .PARAM wmin={pvt_row['wmin']}
    
    .temp {pvt_row['temp']}
    .CONTROL
    dc temp {pvt_row['temp']} {pvt_row['temp']} 1
    print ((-V(node1)*I(Vdd))+(-V(nodea)*I(Vina))+(-V(nodeb)*I(Vinb)))
    .ENDC
    .END
    """
    with open('../netlists/nor2_leakage.sp', 'w') as f:
        f.write(netlist)
    
    # subprocess.run(['ngspice', '-b', 'nor2_leakage.sp'])
    command = "ngspice -b ../netlists/nor2_leakage.sp > ../netlists/nor2_leakage.txt"
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

    with open('../netlists/nor2_leakage.txt', 'r') as f:
        # Read last line of the file
        lines = f.readlines()
        last_line = lines[-1]
        key, value = last_line.split('=')
        leakage_power = float(value.strip())
    return leakage_power

def run_delay_simulation(pvt_row):
    val = pvt_row['pvdd']/2
    netlist = f"""
    .include ../netlists/nor2_delay.net
    .param temp={pvt_row['temp']}
    .param pvdd={pvt_row['pvdd']}
    .param Vin_A={pvt_row['Vin_A']}
    .param Vin_B={pvt_row['Vin_B']}
    .param toxe_n={pvt_row['toxe_n']}
    .param toxm_n={pvt_row['toxm_n']}
    .param toxref_n={pvt_row['toxref_n']}
    .param toxe_p={pvt_row['toxe_p']}
    .param toxm_p={pvt_row['toxm_p']}
    .param toxref_p={pvt_row['toxref_p']}
    .param toxp_par={pvt_row['toxp_par']}
    .param xj_n={pvt_row['xj_n']}
    .param xj_p={pvt_row['xj_p']}
    .param ndep_n={pvt_row['ndep_n']}
    .param ndep_p={pvt_row['ndep_p']}
    .PARAM lmin={pvt_row['lmin']}
    .PARAM wmin={pvt_row['wmin']}
    cqload nodeZ 0 {pvt_row['cqload']}

    .temp {pvt_row['temp']}

    *Definition of type of analysis

    .TRAN 0.1n 42n

    .meas tran delay_lh_nodea trig v(nodea) val={val} fall={pvt_row['pvdd']} targ v(nodeZ) val={val} rise={pvt_row['pvdd']}
    .meas tran delay_hl_nodea trig v(nodea) val={val} rise={pvt_row['pvdd']} targ v(nodeZ) val={val} fall={pvt_row['pvdd']}

    .meas tran delay_lh_nodeb trig v(nodeb) val={val} fall={pvt_row['pvdd']} targ v(nodeZ) val={val} rise={pvt_row['pvdd']}
    .meas tran delay_hl_nodeb trig v(nodeb) val={val} rise={pvt_row['pvdd']} targ v(nodeZ) val={val} fall={pvt_row['pvdd']}

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
        # Find index of the first occurrence of 'delay_lh_nodeb'
        index_delay_lh_nodeb = tokens.index('delay_lh_nodeb')
        # Find index of the first occurrence of 'delay_hl_nodeb'
        index_delay_hl_nodeb = tokens.index('delay_hl_nodeb')
        # Extract values from tokens
        delay_lh_nodea = float(tokens[index_delay_lh_nodea + 2])
        delay_hl_nodea = float(tokens[index_delay_hl_nodea + 2])
        delay_lh_nodeb = float(tokens[index_delay_lh_nodeb + 2])
        delay_hl_nodeb = float(tokens[index_delay_hl_nodeb + 2])

    return delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb

# Initialize list to store individual DataFrame results
results_list = []

# Iterate over each PVT sample and run simulations
for index, pvt_row in pvt_data.iterrows():
    leakage_power = run_leakage_simulation(pvt_row)
    delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb = run_delay_simulation(pvt_row)
    result_row = {
        'Vin_A': pvt_row['Vin_A'],
        'Vin_B': pvt_row['Vin_B'],
        'temp': pvt_row['temp'],
        'pvdd': pvt_row['pvdd'],
        'cqload': pvt_row['cqload'],
        'lmin': pvt_row['lmin'],
        'wmin': pvt_row['wmin'],
        'toxe_n': pvt_row['toxe_n'],
        'toxm_n': pvt_row['toxm_n'],
        'toxref_n': pvt_row['toxref_n'],
        'toxe_p': pvt_row['toxe_p'],
        'toxm_p': pvt_row['toxm_p'],
        'toxref_p': pvt_row['toxref_p'],
        'toxp_par': pvt_row['toxp_par'],
        'xj_n': pvt_row['xj_n'],
        'xj_p': pvt_row['xj_p'],
        'ndep_n': pvt_row['ndep_n'],
        'ndep_p': pvt_row['ndep_p'],
        'leakage': leakage_power,
        'delay_LH_NodeA': delay_lh_nodea,
        'delay_HL_NodeA': delay_hl_nodea,
        'delay_LH_NodeB': delay_lh_nodeb,
        'delay_HL_NodeB': delay_hl_nodeb
    }
    results_list.append(pd.DataFrame([result_row]))  # Append individual DataFrame

# Concatenate all individual DataFrames into one final DataFrame
results = pd.concat(results_list, ignore_index=True)

# Save results to CSV file
results.to_csv('../outputs/simulation_results_nor.csv', index=False)