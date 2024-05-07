
    .include ../../tech_nodes/16nm_HP.pm

    .param SUPPLY = 1
    .param cqload = 1.2552133197397764e-15
    .param high = 0
    .param low = -1*SUPPLY
    .param ckpd = 100n
    .temp 43.78643070691845
    .param toxe_n = 9.208131945807039e-10
    .param toxm_n = 8.646252620808692e-10
    .param toxref_n = 9.37952335142663e-10
    .param toxe_p = 9.35726984699511e-10
    .param toxm_p = 9.52476835802887e-10
    .param toxref_p = 8.681006399174606e-10
    .param toxp_par = 6.871377818450326e-10
    .param xj_n = 1.4448323585948308e-08
    .param xj_p = 1.3771461656225921e-08
    .param ndep_n = 6.774605858544042e+18
    .param ndep_p = 2.756889910566933e+18
    .param lmin = 4.1604509548446296e-08
    .param wmin = 4.5832571913615656e-08
    .temp 43.78643070691845

    VDS supp gnd 'SUPPLY'
    Va a gnd pulse(0 'SUPPLY' 0 0.1p 0.1p 'ckpd' '2*ckpd')
    Vb b gnd pulse(0 'SUPPLY' 50n 0.1p 0.1p '2*ckpd' '4*ckpd')

    * NOT gates *
    M1 an a gnd gnd CMOSN W=4.5832571913615656e-08 L=4.1604509548446296e-08
    + AS=9.53420837904937e-15 PS=5.077102393116943e-07 AD=9.53420837904937e-15 PD=5.077102393116943e-07

    M2 an a supp supp CMOSP W=9.166514382723131e-08 L=4.1604509548446296e-08
    + AS=1.906841675809874e-14 PS=5.993753831389256e-07 AD=1.906841675809874e-14 PD=5.993753831389256e-07


    M3 bn b gnd gnd CMOSN W=4.5832571913615656e-08 L=4.1604509548446296e-08
    + AS=9.53420837904937e-15 PS=5.077102393116943e-07 AD=9.53420837904937e-15 PD=5.077102393116943e-07

    M4 bn b supp supp CMOSP W=9.166514382723131e-08 L=4.1604509548446296e-08
    + AS=1.906841675809874e-14 PS=5.993753831389256e-07 AD=1.906841675809874e-14 PD=5.993753831389256e-07


    * PMOS 1 *
    M5    i1     an     supp     supp     CMOSP     W=9.166514382723131e-08     L=4.1604509548446296e-08
    + AS=1.906841675809874e-14  PS=5.993753831389256e-07  AD=1.906841675809874e-14  PD=5.993753831389256e-07

    * PMOS 2 *
    M6    Out     b     i1     supp     CMOSP     W=9.166514382723131e-08     L=4.1604509548446296e-08
    + AS=1.906841675809874e-14  PS=5.993753831389256e-07  AD=1.906841675809874e-14  PD=5.993753831389256e-07

    * PMOS 3 *
    M7    i2     a     supp     supp     CMOSP     W=9.166514382723131e-08     L=4.1604509548446296e-08
    + AS=1.906841675809874e-14  PS=5.993753831389256e-07  AD=1.906841675809874e-14  PD=5.993753831389256e-07

    * PMOS 4 *
    M8    Out     bn     i2     supp     CMOSP     W=9.166514382723131e-08     L=4.1604509548446296e-08
    + AS=1.906841675809874e-14  PS=5.993753831389256e-07  AD=1.906841675809874e-14  PD=5.993753831389256e-07


    * NMOS 1 *
    M9    Out     an     node4     0     CMOSN     W=4.5832571913615656e-08     L=4.1604509548446296e-08
    + AS=9.53420837904937e-15  PS=5.077102393116943e-07  AD=9.53420837904937e-15  PD=5.077102393116943e-07

    * NMOS 2 *
    M10    node4     bn     0     0     CMOSN     W=4.5832571913615656e-08     L=4.1604509548446296e-08
    + AS=9.53420837904937e-15  PS=5.077102393116943e-07  AD=9.53420837904937e-15  PD=5.077102393116943e-07

    M11    Out     a     node5     0     CMOSN     W=4.5832571913615656e-08     L=4.1604509548446296e-08
    + AS=9.53420837904937e-15  PS=5.077102393116943e-07  AD=9.53420837904937e-15  PD=5.077102393116943e-07

    * NMOS 2 *
    M12    node5     b     0     0     CMOSN     W=4.5832571913615656e-08     L=4.1604509548446296e-08
    + AS=9.53420837904937e-15  PS=5.077102393116943e-07  AD=9.53420837904937e-15  PD=5.077102393116943e-07

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
    