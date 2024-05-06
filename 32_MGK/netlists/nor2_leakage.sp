
    .include ../netlists/nor2_leakage.net
    .PARAM Vin_A=0.0
    .PARAM Vin_B=0.0
    .PARAM pvdd=0.939497358430222

    .PARAM toxe_n=9.129801163296e-10
    .PARAM toxm_n=8.992913029975581e-10
    .PARAM toxref_n=8.579607320564975e-10
    .PARAM ndep_n=6.337948231293587e+18
    .PARAM xj_n=1.3935769005785881e-08
    .PARAM toxp_par=6.439610304863983e-10
    .PARAM toxe_p=9.133869628987415e-10
    .PARAM toxm_p=9.552456972836899e-10
    .PARAM toxref_p=9.85844841029758e-10
    .PARAM ndep_p=2.8678272005251256e+18
    .PARAM xj_p=1.316488075375551e-08
    .PARAM lmin=4.2594072424678656e-08
    .PARAM wmin=4.64502581255931e-08
    
    .temp 104.75400952875518
    .CONTROL
    dc temp 104.75400952875518 104.75400952875518 1
    print ((-V(node1)*I(Vdd))+(-V(nodea)*I(Vina))+(-V(nodeb)*I(Vinb)))
    .ENDC
    .END
    