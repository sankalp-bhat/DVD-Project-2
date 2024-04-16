import subprocess
import pandas as pd

# Load the PVT data
pvt_data = pd.read_csv('../data/pvt_data.csv')

def run_leakage_simulation(pvt_row):
    with open('nand2_leakage.net', 'w') as f:
        f.write(f".include nand2_leakage.net\n")
        f.write(f".param temp={pvt_row['temp']}\n")
        f.write(f".param pvdd={pvt_row['pvdd']}\n")
        f.write(f".param toxe_n={pvt_row['toxe_n']}\n")
        f.write(f".param toxm_n={pvt_row['toxm_n']}\n")
        f.write(f".param toxref_n={pvt_row['toxref_n']}\n")
        f.write(f".param toxe_p={pvt_row['toxe_p']}\n")
        f.write(f".param toxm_p={pvt_row['toxm_p']}\n")
        f.write(f".param toxref_p={pvt_row['toxref_p']}\n")
        f.write(f".param toxp_par={pvt_row['toxp_par']}\n")
        f.write(f".param xj_n={pvt_row['xj_n']}\n")
        f.write(f".param xj_p={pvt_row['xj_p']}\n")
        f.write(f".param ndep_n={pvt_row['ndep_n']}\n")
        f.write(f".param ndep_p={pvt_row['ndep_p']}\n")
        f.write(f".dc vin_A={pvt_row['Vin_A']} vin_B={pvt_row['Vin_B']}\n")
        f.write(f".save v(node1) v(nodea) v(nodeb) i(Vdd)\n")

    subprocess.run(['ngspice', '-b', '../netlists/nand2_leakage.net'])

    # Read leakage output file
    with open('nand2_leakage.net', 'r') as f:
        lines = f.readlines()
        leakage_node1 = None
        leakage_nodea = None
        leakage_nodeb = None
        leakage_current = None
        for line in lines:
            if 'v(node1)' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    leakage_node1 = float(parts[1].strip())
            elif 'v(nodea)' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    leakage_nodea = float(parts[1].strip())
            elif 'v(nodeb)' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    leakage_nodeb = float(parts[1].strip())
            elif 'i(Vdd)' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    leakage_current = float(parts[1].strip())

    # Check if any of the leakage values are None, if so, return None for expr_result
    if leakage_node1 is None or leakage_nodea is None or leakage_nodeb is None or leakage_current is None:
        return None, None, None, None, None

    # Calculate the expression result
    expr_result = (-leakage_node1 * leakage_current), (
        (-leakage_node1 * leakage_current) + (-leakage_nodea * pvt_row['Vin_A']) + (-leakage_nodeb * pvt_row['Vin_B'])
    )

    return leakage_node1, leakage_nodea, leakage_nodeb, leakage_current, expr_result


# Function to run NGSPICE simulation for delay
def run_delay_simulation(pvt_row):
    with open('nand2_delay.net', 'w') as f:
        f.write(f".include nand2_delay.net\n")
        f.write(f".param temp={pvt_row['temp']}\n")
        f.write(f".param pvdd={pvt_row['pvdd']}\n")
        f.write(f".param toxe_n={pvt_row['toxe_n']}\n")
        f.write(f".param toxm_n={pvt_row['toxm_n']}\n")
        f.write(f".param toxref_n={pvt_row['toxref_n']}\n")
        f.write(f".param toxe_p={pvt_row['toxe_p']}\n")
        f.write(f".param toxm_p={pvt_row['toxm_p']}\n")
        f.write(f".param toxref_p={pvt_row['toxref_p']}\n")
        f.write(f".param toxp_par={pvt_row['toxp_par']}\n")
        f.write(f".param xj_n={pvt_row['xj_n']}\n")
        f.write(f".param xj_p={pvt_row['xj_p']}\n")
        f.write(f".param ndep_n={pvt_row['ndep_n']}\n")
        f.write(f".param ndep_p={pvt_row['ndep_p']}\n")
        f.write(f".tran 0.01n 10n\n")
        f.write(f".save v(nodea) v(nodeb)\n")

    subprocess.run(['ngspice', '-b', '../netlists/nand2_delay.net'])

    # Read delay output file
    with open('nand2_delay.net', 'r') as f:
        lines = f.readlines()
        delay_lh_nodea = None
        delay_hl_nodea = None
        delay_lh_nodeb = None
        delay_hl_nodeb = None
        for line in lines:
            if 'delay_lh_nodea' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    delay_lh_nodea = float(parts[1].strip())
            elif 'delay_hl_nodea' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    delay_hl_nodea = float(parts[1].strip())
            elif 'delay_lh_nodeb' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    delay_lh_nodeb = float(parts[1].strip())
            elif 'delay_hl_nodeb' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    delay_hl_nodeb = float(parts[1].strip())

    return delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb


# Initialize list to store individual DataFrame results
results_list = []

# Iterate over each PVT sample and run simulations
for index, pvt_row in pvt_data.iterrows():
    leakage_node1, leakage_nodea, leakage_nodeb, leakage_current, expr_result = run_leakage_simulation(pvt_row)
    delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb = run_delay_simulation(pvt_row)
    result_row = {
        'Vin_A': pvt_row['Vin_A'],
        'Vin_B': pvt_row['Vin_B'],
        'temp': pvt_row['temp'],
        'pvdd': pvt_row['pvdd'],
        'cqload': pvt_row['cqload'],
        # 'lmin': pvt_row['lmin'],
        # 'wmin': pvt_row['wmin'],
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
        'leakage': expr_result,
        'delay_LH_NodeA': delay_lh_nodea,
        'delay_HL_NodeA': delay_hl_nodea,
        'delay_LH_NodeB': delay_lh_nodeb,
        'delay_HL_NodeB': delay_hl_nodeb
    }
    results_list.append(pd.DataFrame([result_row]))  # Append individual DataFrame

# Concatenate all individual DataFrames into one final DataFrame
results = pd.concat(results_list, ignore_index=True)

# Save results to CSV file
results.to_csv('../data/simulation_results.csv', index=False)