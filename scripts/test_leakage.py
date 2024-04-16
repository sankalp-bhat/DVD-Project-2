import subprocess

def generate_netlist(pvt_row):
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
print V(node1) V(nodea) V(nodeb) I(Vdd) (-V(node1)*I(Vdd)) ((-V(node1)*I(Vdd))+(-V(nodea)*I(Vina))+(-V(nodeb)*I(Vinb))) > leakage_netlist.sp.out
.ENDC
.END
"""
    with open('leakage_netlist.sp', 'w') as f:
        f.write(netlist)

def run_leakage_simulation():
    subprocess.run(['ngspice', '-b', 'leakage_netlist.sp'])

def parse_leakage_output():
    with open('leakage_netlist.sp.out', 'r') as f:
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

# Example PVT sample
pvt_sample = {
    'Vin_A': 1,
    'Vin_B': 0,
    'pvdd': 1.1,
    'toxe_n': 8.25e-10,
    'toxm_n': 8.25e-10,
    'toxref_n': 8.25e-10,
    'ndep_n': 5.5e18,
    'xj_n': 6.99e-9,
    'toxp_par': 8.25e-10,
    'toxe_p': 8.25e-10,
    'toxm_p': 8.25e-10,
    'toxref_p': 8.25e-10,
    'ndep_p': 5.5e18,
    'xj_p': 6.99e-9,
}

generate_netlist(pvt_sample)
print("netlist generated")
run_leakage_simulation()
print("simulation run")
leakage_current, leakage_power = parse_leakage_output()
print("output parsed")

print(f"Leakage Current: {leakage_current} A")
print(f"Leakage Power: {leakage_power} W")
