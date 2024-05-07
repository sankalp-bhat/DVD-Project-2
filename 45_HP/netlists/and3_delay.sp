
    .include ../../tech_nodes/45nm_HP.pm

    .param SUPPLY = 1
    .param cqload = 1.34786523191357e-15
    .param high = 0
    .param low = -1*SUPPLY
    .param ckpd = 100n
    .temp -54.15481428534153
    .param toxe_n = 9.208424743096801e-10
    .param toxm_n = 8.843643206309666e-10
    .param toxref_n = 9.606313068445436e-10
    .param toxe_p = 9.451897820687611e-10
    .param toxm_p = 9.066063843179543e-10
    .param toxref_p = 9.275485321863351e-10
    .param toxp_par = 6.226312535714883e-10
    .param xj_n = 1.4605661368970513e-08
    .param xj_p = 1.4088433164189026e-08
    .param ndep_n = 6.597437621716932e+18
    .param ndep_p = 2.9304703177014287e+18
    .param lmin = 4.471674782967332e-08
    .param wmin = 4.384994271819466e-08
    .temp -54.15481428534153

    * Circuit discription *

    * Voltage Sources *

    VDS supp gnd 'SUPPLY'
    Va a gnd pulse(0 'SUPPLY' 0 0.1p 0.1p 'ckpd' '2*ckpd')
    Vb b gnd pulse(0 'SUPPLY' 50n 0.1p 0.1p '2*ckpd' '4*ckpd')
    Vc c gnd pulse(0 'SUPPLY' 75n 0.1p 0.1p '4*ckpd' '8*ckpd')

    * PMOS 1 *
    M1    node7     a     supp     supp     pmos     W=8.769988543638931e-08     L=4.471674782967332e-08
    + AS=1.9608268308751305e-14  PS=6.225672491695119e-07  AD=1.9608268308751305e-14  PD=6.225672491695119e-07

    * PMOS 2 *
    M2    node7     b     supp     supp     pmos     W=8.769988543638931e-08     L=4.471674782967332e-08
    + AS=1.9608268308751305e-14  PS=6.225672491695119e-07  AD=1.9608268308751305e-14  PD=6.225672491695119e-07

    * PMOS 3 *
    M3    node7     c     supp     supp     pmos     W=8.769988543638931e-08     L=4.471674782967332e-08
    + AS=1.9608268308751305e-14  PS=6.225672491695119e-07  AD=1.9608268308751305e-14  PD=6.225672491695119e-07

    * NMOS 1 *
    M4    node7     c     node6     0     nmos     W=1.3154982815458398e-07     L=4.471674782967332e-08
    + AS=2.9412402463126954e-14  PS=7.102671346059012e-07  AD=2.9412402463126954e-14  PD=7.102671346059012e-07

    * NMOS 2 *
    M5    node6     b     node5     0     nmos     W=1.3154982815458398e-07     L=4.471674782967332e-08
    + AS=2.9412402463126954e-14  PS=7.102671346059012e-07  AD=2.9412402463126954e-14  PD=7.102671346059012e-07

    * NMOS 3 *
    M6    node5     a     0     0     nmos     W=1.3154982815458398e-07     L=4.471674782967332e-08
    + AS=2.9412402463126954e-14  PS=7.102671346059012e-07  AD=2.9412402463126954e-14  PD=7.102671346059012e-07

    * NOT gate *

    M7    Out     node7     supp     supp     pmos     W=8.769988543638931e-08     L=4.471674782967332e-08
    + AS=1.9608268308751305e-14  PS=6.225672491695119e-07  AD=1.9995875364625938e-14  PD=6.225672491695119e-07

    M8    Out     node7     0     0     nmos     W=4.384994271819466e-08     L=4.471674782967332e-08
    + AS=9.804134154375652e-15  PS=5.348673637331225e-07  AD=9.804134154375652e-15  PD=5.348673637331225e-07

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
    