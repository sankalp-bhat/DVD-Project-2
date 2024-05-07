
    .include ../../tech_nodes/32nm_MGK.pm

    .param SUPPLY = 1
    .param cqload = 3.73974552838374e-15
    .param high = 0
    .param low = -1*SUPPLY
    .param ckpd = 100n
    .temp 23.194992600461745
    .param toxe_n = 8.529669682707463e-10
    .param toxm_n = 8.989471446939099e-10
    .param toxref_n = 8.644594022876533e-10
    .param toxe_p = 9.260468856927191e-10
    .param toxm_p = 9.022465103750747e-10
    .param toxref_p = 9.116501995648841e-10
    .param toxp_par = 6.000547181407236e-10
    .param xj_n = 1.4244961669701412e-08
    .param xj_p = 1.4034199868270234e-08
    .param ndep_n = 6.39849685698606e+18
    .param ndep_p = 2.8035462945889946e+18
    .param lmin = 4.3895263242741377e-08
    .param wmin = 4.471587310678231e-08
    .temp 23.194992600461745

    VDS supp gnd 'SUPPLY'
    Va a gnd pulse(0 'SUPPLY' 0 0.1p 0.1p 'ckpd' '2*ckpd')
    Vb b gnd pulse(0 'SUPPLY' 50n 0.1p 0.1p '2*ckpd' '4*ckpd')

    * NOT gates *
    M1 an a gnd gnd nmos W=4.471587310678231e-08 L=4.3895263242741377e-08
    + AS=9.814075105756147e-15 PS=5.283843786409784e-07 AD=9.814075105756147e-15 PD=5.283843786409784e-07

    M2 an a supp supp pmos W=8.943174621356462e-08 L=4.3895263242741377e-08
    + AS=1.9628150211512294e-14 PS=6.17816124854543e-07 AD=1.9628150211512294e-14 PD=6.17816124854543e-07


    M3 bn b gnd gnd nmos W=4.471587310678231e-08 L=4.3895263242741377e-08
    + AS=9.814075105756147e-15 PS=5.283843786409784e-07 AD=9.814075105756147e-15 PD=5.283843786409784e-07

    M4 bn b supp supp pmos W=8.943174621356462e-08 L=4.3895263242741377e-08
    + AS=1.9628150211512294e-14 PS=6.17816124854543e-07 AD=1.9628150211512294e-14 PD=6.17816124854543e-07


    * PMOS 1 *
    M5    i1     an     supp     supp     pmos     W=8.943174621356462e-08     L=4.3895263242741377e-08
    + AS=1.9628150211512294e-14  PS=6.17816124854543e-07  AD=1.9628150211512294e-14  PD=6.17816124854543e-07

    * PMOS 2 *
    M6    Out     b     i1     supp     pmos     W=8.943174621356462e-08     L=4.3895263242741377e-08
    + AS=1.9628150211512294e-14  PS=6.17816124854543e-07  AD=1.9628150211512294e-14  PD=6.17816124854543e-07

    * PMOS 3 *
    M7    i2     a     supp     supp     pmos     W=8.943174621356462e-08     L=4.3895263242741377e-08
    + AS=1.9628150211512294e-14  PS=6.17816124854543e-07  AD=1.9628150211512294e-14  PD=6.17816124854543e-07

    * PMOS 4 *
    M8    Out     bn     i2     supp     pmos     W=8.943174621356462e-08     L=4.3895263242741377e-08
    + AS=1.9628150211512294e-14  PS=6.17816124854543e-07  AD=1.9628150211512294e-14  PD=6.17816124854543e-07


    * NMOS 1 *
    M9    Out     an     node4     0     nmos     W=4.471587310678231e-08     L=4.3895263242741377e-08
    + AS=9.814075105756147e-15  PS=5.283843786409784e-07  AD=9.814075105756147e-15  PD=5.283843786409784e-07

    * NMOS 2 *
    M10    node4     bn     0     0     nmos     W=4.471587310678231e-08     L=4.3895263242741377e-08
    + AS=9.814075105756147e-15  PS=5.283843786409784e-07  AD=9.814075105756147e-15  PD=5.283843786409784e-07

    M11    Out     a     node5     0     nmos     W=4.471587310678231e-08     L=4.3895263242741377e-08
    + AS=9.814075105756147e-15  PS=5.283843786409784e-07  AD=9.814075105756147e-15  PD=5.283843786409784e-07

    * NMOS 2 *
    M12    node5     b     0     0     nmos     W=4.471587310678231e-08     L=4.3895263242741377e-08
    + AS=9.814075105756147e-15  PS=5.283843786409784e-07  AD=9.814075105756147e-15  PD=5.283843786409784e-07

    Cload out gnd 'cqload'

    * Analysis *

    .tran 0.1n 500n


    .measure tran tfall_a
    +TRIG v(a) VAL = 'SUPPLY/2' RISE = 2
    +TARG v(Out) VAL = 'SUPPLY/2' FALL = 2

    .measure tran trise_a
    +TRIG v(a) VAL = 'SUPPLY/2' RISE = 1
    +TARG v(out) VAL = 'SUPPLY/2' RISE = 1

    .measure tran tpd_a param = '(trise_a + tfall_a)/2' goal = 0

    .measure tran tfall_b
    +TRIG v(b) VAL = 'SUPPLY/2' RISE = 1
    +TARG v(Out) VAL = 'SUPPLY/2' FALL = 1

    .measure tran trise_b
    +TRIG v(b) VAL = 'SUPPLY/2' FALL = 1
    +TARG v(out) VAL = 'SUPPLY/2' RISE = 3

    .measure tran tpd_b param = '(trise_b + tfall_b)/2' goal = 0

    .measure tran delay_lh_nodea param = 'trise_a' goal =0
    .measure tran delay_hl_nodea param = 'tfall_a' goal =0
    .measure tran delay_lh_nodeb param = 'trise_b' goal =0
    .measure tran delay_hl_nodeb param = 'tfall_b' goal =0

    .control

    run

    print delay_hl_nodea delay_lh_nodea delay_hl_nodeb delay_lh_nodeb

    .endc
    .end
    