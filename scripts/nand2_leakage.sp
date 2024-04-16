
    .include ../netlists/nand2_leakage.net
    .PARAM Vin_A=1.0
    .PARAM Vin_B=1.0
    .PARAM pvdd=1.0944459671412408

    .PARAM toxe_n=9.197983854983275e-10
    .PARAM toxm_n=8.662474739855985e-10
    .PARAM toxref_n=9.052528536819101e-10
    .PARAM ndep_n=6.414769601483049e+18
    .PARAM xj_n=1.374067423478764e-08
    .PARAM toxp_par=6.598721319949616e-10
    .PARAM toxe_p=9.350188870322447e-10
    .PARAM toxm_p=9.137768819679607e-10
    .PARAM toxref_p=8.915629736065262e-10
    .PARAM ndep_p=2.8931082959170207e+18
    .PARAM xj_p=1.296066502723909e-08
    .PARAM Lmin=45n
    .PARAM Wmin=45n

    .temp 40
    .CONTROL
    dc temp 40 40 1
    print V(node1) V(nodea) V(nodeb) I(Vdd) (-V(node1)*I(Vdd)) ((-V(node1)*I(Vdd))+(-V(nodea)*I(Vina))+(-V(nodeb)*I(Vinb))) > nand2_leakage.sp.out
    .ENDC
    .END
    