import subprocess
import pandas as pd

# Load the PVT data
pvt_data = pd.read_csv('../../data/and3_data_test.csv')
pvt_data = pvt_data.dropna()

def run_delay_simulation(pvt_row):
    val = pvt_row['pvdd']/2
    wmin = pvt_row['wmin']
    lmin = pvt_row['lmin']
    netlist = f"""
    .include ../../tech_nodes/45nm_HP.pm

    .param SUPPLY = 1
    .param cqload = {pvt_row['cqload']}
    .param high = 0
    .param low = -1*SUPPLY
    .param ckpd = 100n
    .temp {pvt_row['temp']}
    .param toxe_n = {pvt_row['toxe_n']}
    .param toxm_n = {pvt_row['toxm_n']}
    .param toxref_n = {pvt_row['toxref_n']}
    .param toxe_p = {pvt_row['toxe_p']}
    .param toxm_p = {pvt_row['toxm_p']}
    .param toxref_p = {pvt_row['toxref_p']}
    .param toxp_par = {pvt_row['toxp_par']}
    .param xj_n = {pvt_row['xj_n']}
    .param xj_p = {pvt_row['xj_p']}
    .param ndep_n = {pvt_row['ndep_n']}
    .param ndep_p = {pvt_row['ndep_p']}
    .param lmin = {pvt_row['lmin']}
    .param wmin = {pvt_row['wmin']}
    .temp {pvt_row['temp']}

    * Circuit discription *

    * Voltage Sources *

    VDS supp gnd 'SUPPLY'
    Va a gnd pulse(0 'SUPPLY' 0 0.1p 0.1p 'ckpd' '2*ckpd')
    Vb b gnd pulse(0 'SUPPLY' 50n 0.1p 0.1p '2*ckpd' '4*ckpd')
    Vc c gnd pulse(0 'SUPPLY' 75n 0.1p 0.1p '4*ckpd' '8*ckpd')

    * PMOS 1 *
    M1    node7     a     supp     supp     pmos     W={2*wmin}     L={lmin}
    + AS={10*wmin*lmin}  PS={10*lmin+4*wmin}  AD={10*wmin*lmin}  PD={10*lmin+4*wmin}

    * PMOS 2 *
    M2    node7     b     supp     supp     pmos     W={2*wmin}     L={lmin}
    + AS={10*wmin*lmin}  PS={10*lmin+4*wmin}  AD={10*wmin*lmin}  PD={10*lmin+4*wmin}

    * PMOS 3 *
    M3    node7     c     supp     supp     pmos     W={2*wmin}     L={lmin}
    + AS={10*wmin*lmin}  PS={10*lmin+4*wmin}  AD={10*wmin*lmin}  PD={10*lmin+4*wmin}

    * NMOS 1 *
    M4    node7     c     node6     0     nmos     W={3*wmin}     L={lmin}
    + AS={15*wmin*lmin}  PS={10*lmin+6*wmin}  AD={15*wmin*lmin}  PD={10*lmin+6*wmin}

    * NMOS 2 *
    M5    node6     b     node5     0     nmos     W={3*wmin}     L={lmin}
    + AS={15*wmin*lmin}  PS={10*lmin+6*wmin}  AD={15*wmin*lmin}  PD={10*lmin+6*wmin}

    * NMOS 3 *
    M6    node5     a     0     0     nmos     W={3*wmin}     L={lmin}
    + AS={15*wmin*lmin}  PS={10*lmin+6*wmin}  AD={15*wmin*lmin}  PD={10*lmin+6*wmin}

    * NOT gate *

    M7    Out     node7     supp     supp     pmos     W={2*wmin}     L={lmin}
    + AS={10*wmin*lmin}  PS={10*lmin+4*wmin}  AD={10*lmin*lmin}  PD={10*lmin+2*2*wmin}

    M8    Out     node7     0     0     nmos     W={wmin}     L={lmin}
    + AS={5*wmin*lmin}  PS={10*lmin+2*wmin}  AD={5*wmin*lmin}  PD={10*lmin+2*wmin}

    Cload Out gnd 'cqload'

    * Analysis *

    .tran 0.1n 500n


    .measure tran tfall_a
    +TRIG v(a) VAL = 'SUPPLY/2' FALL = 1
    +TARG v(Out) VAL = 'SUPPLY/2' FALL = 1

    .measure tran trise_a
    +TRIG v(a) VAL = 'SUPPLY/2' RISE = 2
    +TARG v(out) VAL = 'SUPPLY/2' RISE = 2

    .measure tran tpd_a param = '(trise_a + tfall_a)/2' goal = 0

    .measure tran tfall_b
    +TRIG v(b) VAL = 'SUPPLY/2' FALL = 1
    +TARG v(Out) VAL = 'SUPPLY/2' FALL = 2

    .measure tran trise_b
    +TRIG v(b) VAL = 'SUPPLY/2' RISE = 2
    +TARG v(out) VAL = 'SUPPLY/2' RISE = 3

    .measure tran tpd_b param = '(trise_b + tfall_b)/2' goal = 0

    .measure tran tfall_c
    +TRIG v(c) VAL = 'SUPPLY/2' FALL = 1
    +TARG v(out) VAL = 'SUPPLY/2' FALL = 3

    .measure tran trise_c
    +TRIG v(c) VAL = 'SUPPLY/2' RISE = 1
    +TARG v(Out) VAL = 'SUPPLY/2' RISE = 1

    .measure tran tpd_c param = '(trise_c + tfall_c)/2' goal = 0

    .measure tran delay_lh_nodea param = 'trise_a' goal =0
    .measure tran delay_hl_nodea param = 'tfall_a' goal =0
    .measure tran delay_lh_nodeb param = 'trise_b' goal =0
    .measure tran delay_hl_nodeb param = 'tfall_b' goal =0
    .measure tran delay_lh_nodec param = 'trise_c' goal =0
    .measure tran delay_hl_nodec param = 'tfall_c' goal =0

    .control

    run

    print delay_hl_nodea delay_lh_nodea delay_hl_nodeb delay_lh_nodeb delay_hl_nodec delay_lh_nodec

    .endc
    .end
    """

    with open('../netlists/and3_delay.sp', 'w') as f:
        f.write(netlist)

    command = "ngspice -b ../netlists/and3_delay.sp > ../netlists/and3_delay.txt"
    subprocess.run(command, shell=True)
  
    # Tokenization
    with open('../netlists/and3_delay.txt', 'r') as f:
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
        # Find index of the first occurrence of 'delay_lh_nodec'
        index_delay_lh_nodec = tokens.index('delay_lh_nodec')
        # Find index of the first occurrence of 'delay_hl_nodec'
        index_delay_hl_nodec = tokens.index('delay_hl_nodec')
        # Extract values from tokens
        delay_lh_nodea = float(tokens[index_delay_lh_nodea + 2])
        delay_hl_nodea = float(tokens[index_delay_hl_nodea + 2])
        delay_lh_nodeb = float(tokens[index_delay_lh_nodeb + 2])
        delay_hl_nodeb = float(tokens[index_delay_hl_nodeb + 2])
        delay_lh_nodec = float(tokens[index_delay_lh_nodec + 2])
        delay_hl_nodec = float(tokens[index_delay_hl_nodec + 2])        

    return delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb, delay_lh_nodec, delay_hl_nodec

# Initialize list to store individual DataFrame results
results_list = []

# Iterate over each PVT sample and run simulations
for index, pvt_row in pvt_data.iterrows():
    # leakage_power = run_leakage_simulation(pvt_row)
    delay_lh_nodea, delay_hl_nodea, delay_lh_nodeb, delay_hl_nodeb, delay_lh_nodec, delay_hl_nodec = run_delay_simulation(pvt_row)
    result_row = {
        'Vin_A': pvt_row['Vin_A'],
        'Vin_B': pvt_row['Vin_B'],
        'Vin_C': pvt_row['Vin_C'],
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
        # 'leakage': leakage_power,
        'delay_LH_NodeA': delay_lh_nodea,
        'delay_HL_NodeA': delay_hl_nodea,
        'delay_LH_NodeB': delay_lh_nodeb,
        'delay_HL_NodeB': delay_hl_nodeb,
        'delay_LH_NodeC': delay_lh_nodec,
        'delay_HL_NodeC': delay_hl_nodec
    }
    results_list.append(pd.DataFrame([result_row]))  # Append individual DataFrame

# Concatenate all individual DataFrames into one final DataFrame
results = pd.concat(results_list, ignore_index=True)

# Save results to CSV file
results.to_csv('../outputs/simulation_results_and_delay.csv', index=False)