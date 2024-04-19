
    .include ../netlists/nor2_leakage.net
    .PARAM Vin_A=1.0
    .PARAM Vin_B=1.0
    .PARAM pvdd=1.0251773291983624

    .PARAM toxe_n=9.04522818997131e-10
    .PARAM toxm_n=8.77442506638153e-10
    .PARAM toxref_n=8.855996797151805e-10
    .PARAM ndep_n=6.233398801043673e+18
    .PARAM xj_n=1.4566774277853691e-08
    .PARAM toxp_par=6.682386915447985e-10
    .PARAM toxe_p=9.384903024469308e-10
    .PARAM toxm_p=9.220999760912921e-10
    .PARAM toxref_p=9.031884142096815e-10
    .PARAM ndep_p=2.980220887479032e+18
    .PARAM xj_p=1.4779783497461212e-08
    .PARAM lmin=4.552864068390532e-08
    .PARAM wmin=4.697390058083092e-08
    
    .temp 91.4435143912212
    .CONTROL
    dc temp 91.4435143912212 91.4435143912212 1
    print ((-V(node1)*I(Vdd))+(-V(nodea)*I(Vina))+(-V(nodeb)*I(Vinb)))
    .ENDC
    .END
    