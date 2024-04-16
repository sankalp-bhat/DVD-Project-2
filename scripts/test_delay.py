import subprocess
import os

def run_delay_simulation(pvt_row):
    with open('nand2_delay.sp', 'w') as f:
        f.write(f".include ../netlists/nand2_delay.net\n")
        f.write(f".param temp={pvt_row['temp']}\n")
        f.write(f".param pvdd={pvt_row['pvdd']}\n")
        f.write(f".param Vin_A={pvt_row['Vin_A']}\n")
        f.write(f".param Vin_B={pvt_row['Vin_B']}\n")
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
        f.write(f".print delay_lh_nodea delay_hl_nodea delay_lh_nodeb delay_hl_nodeb > nand2_delay.sp.out\n")
        f.write(f".tran 0.1p 1000p\n")
        f.write(f".save V(nodea) V(nodeb) V(nodeZ)\n")

    subprocess.run(['ngspice', '-b', 'nand2_delay.sp'])

    # Check if output file exists
    if os.path.isfile('nand2_delay.sp.out'):
        # Read delay output file
        with open('nand2_delay.net.out', 'r') as f:
            lines = f.readlines()
            delay_lh_nodea = None
            delay_hl_nodea = None
            delay_lh_nodeb = None
            delay_hl_nodeb = None
            for line in lines:
                if line.startswith('delay_lh_nodea'):
                    parts = line.split()
                    if len(parts) > 1:
                        delay_lh_nodea = float(parts[1])
                elif line.startswith('delay_hl_nodea'):
                    parts = line.split()
                    if len(parts) > 1:
                        delay_hl_nodea = float(parts[1])
                elif line.startswith('delay_lh_nodeb'):
                    parts = line.split()
                    if len(parts) > 1:
                        delay_lh_nodeb = float(parts[1])
                elif line.startswith('delay_hl_nodeb'):
                    parts = line.split()
                    if len(parts) > 1:
                        delay_hl_nodeb = float(parts[1])

        return delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb
    else:
        return None, None, None, None

# Example PVT sample
pvt_sample = {
    'temp': 40,
    'pvdd': 1.1,
    'Vin_A': 1,
    'Vin_B': 0,
    'toxe_n': 8.25e-10,
    'toxm_n': 8.25e-10,
    'toxref_n': 8.25e-10,
    'ndep_n': 5.5e18,
    'ndep_p': 5.5e18,  # Added missing parameter 'ndep_p'
    'xj_n': 6.99e-9,
    'toxe_p': 8.25e-10,
    'toxm_p': 8.25e-10,
    'toxref_p': 8.25e-10,
    'toxp_par': 8.25e-10,
    'xj_p': 6.99e-9,
}

delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb = run_delay_simulation(pvt_sample)

print(f"Delay LH NodeA: {delay_lh_nodea} s")
print(f"Delay HL NodeA: {delay_hl_nodea} s")
print(f"Delay LH NodeB: {delay_lh_nodeb} s")
print(f"Delay HL NodeB: {delay_hl_nodeb} s")

