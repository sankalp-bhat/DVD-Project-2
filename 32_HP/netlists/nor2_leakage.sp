
    .include ../netlists/nor2_leakage.net
    .PARAM Vin_A=1.0
    .PARAM Vin_B=1.0
    .PARAM pvdd=1.099253574326969

    .PARAM toxe_n=9.041722718736135e-10
    .PARAM toxm_n=9.147815896173303e-10
    .PARAM toxref_n=8.836625274561985e-10
    .PARAM ndep_n=6.426754264279328e+18
    .PARAM xj_n=1.3543099903675788e-08
    .PARAM toxp_par=6.673297252663476e-10
    .PARAM toxe_p=9.217907345595883e-10
    .PARAM toxm_p=9.206563612183675e-10
    .PARAM toxref_p=8.958128938438405e-10
    .PARAM ndep_p=2.7725618888092984e+18
    .PARAM xj_p=1.3302062106702594e-08
    .PARAM lmin=4.641094963685349e-08
    .PARAM wmin=4.1044889737988806e-08
    
    .temp 61.2609403519981
    .CONTROL
    dc temp 61.2609403519981 61.2609403519981 1
    print ((-V(node1)*I(Vdd))+(-V(nodea)*I(Vina))+(-V(nodeb)*I(Vinb)))
    .ENDC
    .END
    