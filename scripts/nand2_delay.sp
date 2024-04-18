
    .include ../netlists/nand2_delay.net
    .param temp=40
    .param pvdd=1.1
    .param Vin_A=1
    .param Vin_B=0
    .param toxe_n=8.25e-10
    .param toxm_n=8.25e-10
    .param toxref_n=8.25e-10
    .param toxe_p=8.25e-10
    .param toxm_p=8.25e-10
    .param toxref_p=8.25e-10
    .param toxp_par=8.25e-10
    .param xj_n=6.99e-09
    .param xj_p=6.99e-09
    .param ndep_n=5.5e+18
    .param ndep_p=5.5e+18
    cqload nodea 0 5e-17
    .CONTROL
    print delay_lh_nodea delay_hl_nodea delay_lh_nodeb delay_hl_nodeb > nand2_delay.sp.out
    .ENDC
    .END
    