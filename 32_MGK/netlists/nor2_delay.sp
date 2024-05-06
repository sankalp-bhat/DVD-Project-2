
    .include ../netlists/nor2_delay.net
    .param temp=104.75400952875518
    .param pvdd=0.939497358430222
    .param Vin_A=0.0
    .param Vin_B=0.0
    .param toxe_n=9.129801163296e-10
    .param toxm_n=8.992913029975581e-10
    .param toxref_n=8.579607320564975e-10
    .param toxe_p=9.133869628987415e-10
    .param toxm_p=9.552456972836899e-10
    .param toxref_p=9.85844841029758e-10
    .param toxp_par=6.439610304863983e-10
    .param xj_n=1.3935769005785881e-08
    .param xj_p=1.316488075375551e-08
    .param ndep_n=6.337948231293587e+18
    .param ndep_p=2.8678272005251256e+18
    .PARAM lmin=4.2594072424678656e-08
    .PARAM wmin=4.64502581255931e-08
    cqload nodeZ 0 1.330018261107423e-15

    .temp 104.75400952875518

    *Definition of type of analysis

    .TRAN 0.1n 42n

    .meas tran delay_lh_nodea trig v(nodea) val=0.469748679215111 fall=0.939497358430222 targ v(nodeZ) val=0.469748679215111 rise=0.939497358430222
    .meas tran delay_hl_nodea trig v(nodea) val=0.469748679215111 rise=0.939497358430222 targ v(nodeZ) val=0.469748679215111 fall=0.939497358430222

    .meas tran delay_lh_nodeb trig v(nodeb) val=0.469748679215111 fall=0.939497358430222 targ v(nodeZ) val=0.469748679215111 rise=0.939497358430222
    .meas tran delay_hl_nodeb trig v(nodeb) val=0.469748679215111 rise=0.939497358430222 targ v(nodeZ) val=0.469748679215111 fall=0.939497358430222

    .CONTROL
        run
    .ENDC 
    
    .END
    