import subprocess
import pandas as pd

# Load the PVT data
pvt_data = pd.read_csv('../data/pvt_data.csv')

# Function to run NGSPICE simulation for leakage
def run_leakage_simulation(pvt_row):
    with open('nor2_leakage.net', 'w') as f:
        f.write(f".include nor2_leakage.net\n")
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
        f.write(f".dc vin={pvt_row['Vin_A']}\n")
        f.write(f".save v(nodea) v(nodeb)\n")

    subprocess.run(['ngspice', '-b', '../netlists/nor2_leakage.net'])

    # Read leakage output file
    with open('nor2_leakage.net', 'r') as f:
        lines = f.readlines()
        leakage_nodea = None
        leakage_nodeb = None
        for line in lines:
            if 'v(nodea)' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    leakage_nodea = float(parts[1].strip())
            elif 'v(nodeb)' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    leakage_nodeb = float(parts[1].strip())

    return leakage_nodea, leakage_nodeb


# Function to run NGSPICE simulation for delay
def run_delay_simulation(pvt_row):
    with open('nor2_delay.net', 'w') as f:
        f.write(f".include nor2_delay.net\n")
        f.write(f".param temp={pvt_row['temp']}\n")
        f.write(f".param pvdd={pvt_row['pvdd']}\n")
        f.write(f".param cqload={pvt_row['cqload']}\n")
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

    subprocess.run(['ngspice', '-b', '../netlists/nor2_delay.net'])

    # Read leakage output file
    with open('nor2_delay.net', 'r') as f:
        lines = f.readlines()
        leakage_nodea = None
        leakage_nodeb = None
        for line in lines:
            if 'v(nodea)' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    leakage_nodea = float(parts[1].strip())
            elif 'v(nodeb)' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    leakage_nodeb = float(parts[1].strip())

    return leakage_nodea, leakage_nodeb

# Initialize list to store individual DataFrame results
results_list = []

# Iterate over each PVT sample and run simulations
for index, pvt_row in pvt_data.iterrows():
    leakage_nodea, leakage_nodeb = run_leakage_simulation(pvt_row)
    delay_nodea, delay_nodeb = run_delay_simulation(pvt_row)
    result_row = {
        'Vin_A': pvt_row['Vin_A'],
        'Vin_B': pvt_row['Vin_B'],
        'Leakage_NodeA': leakage_nodea,
        'Leakage_NodeB': leakage_nodeb,
        'Delay_NodeA': delay_nodea,
        'Delay_NodeB': delay_nodeb
    }
    results_list.append(pd.DataFrame([result_row]))  # Append individual DataFrame

# Concatenate all individual DataFrames into one final DataFrame
results = pd.concat(results_list, ignore_index=True)

# Save results to CSV file
results.to_csv('../data/simulation_results_nor.csv', index=False)
