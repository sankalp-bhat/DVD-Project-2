import subprocess
import pandas as pd

# Load the PVT data
pvt_data = pd.read_csv('../data/pvt_data.csv')


def run_leakage_simulation(pvt_row):
    netlist = f"""
    .include ../netlists/nand2_leakage.net
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
    .PARAM Lmin=45n
    .PARAM Wmin=45n

    .temp 40
    .CONTROL
    dc temp 40 40 1
    print V(node1) V(nodea) V(nodeb) I(Vdd) (-V(node1)*I(Vdd)) ((-V(node1)*I(Vdd))+(-V(nodea)*I(Vina))+(-V(nodeb)*I(Vinb))) > nand2_leakage.sp.out
    .ENDC
    .END
    """
    with open('nand2_leakage.sp', 'w') as f:
        f.write(netlist)

    subprocess.run(['ngspice', '-b', 'nand2_leakage.sp'])

    with open('nand2_leakage.sp.out', 'r') as f:
        lines = f.readlines()
        parsed_data = {}
        for line in lines:
            if '=' in line:
                key, value = line.split('=')
                key = key.strip()
                value = float(value.strip())
                parsed_data[key] = value
        leakage_current = parsed_data.get('i(vdd)', 0.0)
        leakage_power = parsed_data.get('(-v(node1)*i(vdd))', 0.0)
    return leakage_current, leakage_power

# # Function to run NGSPICE simulation for delay
# def run_delay_simulation(pvt_row):
#     with open('nand2_delay.net', 'w') as f:
#         f.write(f".include nand2_delay.sp\n")
#         f.write(f".param temp={pvt_row['temp']}\n")
#         f.write(f".param pvdd={pvt_row['pvdd']}\n")
#         f.write(f".param Vin_A={pvt_row['Vin_A']}\n")
#         f.write(f".param Vin_B={pvt_row['Vin_B']}\n")
#         f.write(f".param toxe_n={pvt_row['toxe_n']}\n")
#         f.write(f".param toxm_n={pvt_row['toxm_n']}\n")
#         f.write(f".param toxref_n={pvt_row['toxref_n']}\n")
#         f.write(f".param toxe_p={pvt_row['toxe_p']}\n")
#         f.write(f".param toxm_p={pvt_row['toxm_p']}\n")
#         f.write(f".param toxref_p={pvt_row['toxref_p']}\n")
#         f.write(f".param toxp_par={pvt_row['toxp_par']}\n")
#         f.write(f".param xj_n={pvt_row['xj_n']}\n")
#         f.write(f".param xj_p={pvt_row['xj_p']}\n")
#         f.write(f".param ndep_n={pvt_row['ndep_n']}\n")
#         f.write(f".param ndep_p={pvt_row['ndep_p']}\n")
#         f.write(f".tran 0.1p 1000p\n")
#         f.write(f".save V(nodea) V(nodeb) V(nodeZ)\n")
#         f.write(f".print delay_lh_nodea delay_hl_nodea delay_lh_nodeb delay_hl_nodeb >> nand2_delay.net.out\n")

#     subprocess.run(['ngspice', '-b', 'nand2_delay.net'])

#     # Read delay output file
#     with open('nand2_delay.net.out', 'r') as f:
#         lines = f.readlines()
#         delay_lh_nodea = None
#         delay_hl_nodea = None
#         delay_lh_nodeb = None
#         delay_hl_nodeb = None
#         for line in lines:
#             if line.startswith('delay_lh_nodea'):
#                 parts = line.split()
#                 if len(parts) > 1:
#                     delay_lh_nodea = float(parts[1])
#             elif line.startswith('delay_hl_nodea'):
#                 parts = line.split()
#                 if len(parts) > 1:
#                     delay_hl_nodea = float(parts[1])
#             elif line.startswith('delay_lh_nodeb'):
#                 parts = line.split()
#                 if len(parts) > 1:
#                     delay_lh_nodeb = float(parts[1])
#             elif line.startswith('delay_hl_nodeb'):
#                 parts = line.split()
#                 if len(parts) > 1:
#                     delay_hl_nodeb = float(parts[1])

#     return delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb



# Initialize list to store individual DataFrame results
results_list = []

# Iterate over each PVT sample and run simulations
for index, pvt_row in pvt_data.iterrows():
    leakage_current, leakage_power = run_leakage_simulation(pvt_row)
    # delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb = run_delay_simulation(pvt_row)
    print("leakage power: ", leakage_power)
    # print("delay:",delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb)
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
        'leakage': leakage_power
        # 'delay_LH_NodeA': delay_lh_nodea,
        # 'delay_HL_NodeA': delay_hl_nodea,
        # 'delay_LH_NodeB': delay_lh_nodeb,
        # 'delay_HL_NodeB': delay_hl_nodeb
    }
    results_list.append(pd.DataFrame([result_row]))  # Append individual DataFrame

# Concatenate all individual DataFrames into one final DataFrame
results = pd.concat(results_list, ignore_index=True)

# Save results to CSV file
results.to_csv('../data/simulation_results_nand.csv', index=False)