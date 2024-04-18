import subprocess
import os

def run_delay_simulation(pvt_row):
    netlist = f"""
    .include ../netlists/nand2_delay.net
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
    cqload nodea 0 {pvt_row['cqload']}
    .CONTROL
    print delay_lh_nodea delay_hl_nodea delay_lh_nodeb delay_hl_nodeb > nand2_delay.sp.out
    .ENDC
    .END
    """

    with open('nand2_delay.sp', 'w') as f:
        f.write(netlist)

    subprocess.run(['ngspice','-b','nand2_delay.sp'])

    # Check if output file exists
    if os.path.isfile('nand2_delay.sp.out'):
        # Read delay output file
        with open('nand2_delay.sp.out', 'r') as f:
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
    'ndep_p': 5.5e18,  
    'xj_n': 6.99e-9,
    'toxe_p': 8.25e-10,
    'toxm_p': 8.25e-10,
    'toxref_p': 8.25e-10,
    'toxp_par': 8.25e-10,
    'xj_p': 6.99e-9,
    'cqload': 0.05e-15,
}

delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb = run_delay_simulation(pvt_sample)

print(f"Delay LH NodeA: {delay_lh_nodea} s")
print(f"Delay HL NodeA: {delay_hl_nodea} s")
print(f"Delay LH NodeB: {delay_lh_nodeb} s")
print(f"Delay HL NodeB: {delay_hl_nodeb} s")

