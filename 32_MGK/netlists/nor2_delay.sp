
    .include ../netlists/not_delay.net
    .param temp=91.4435143912212
    .param pvdd=1.0251773291983624
    .param Vin=1.0
    .param toxe_n=9.04522818997131e-10
    .param toxm_n=8.77442506638153e-10
    .param toxref_n=8.855996797151805e-10
    .param toxe_p=9.384903024469308e-10
    .param toxm_p=9.220999760912921e-10
    .param toxref_p=9.031884142096815e-10
    .param toxp_par=6.682386915447985e-10
    .param xj_n=1.4566774277853691e-08
    .param xj_p=1.4779783497461212e-08
    .param ndep_n=6.233398801043673e+18
    .param ndep_p=2.980220887479032e+18
    .PARAM lmin=4.552864068390532e-08
    .PARAM wmin=4.697390058083092e-08
    cqload nodeZ 0 3.572204379239302e-15

    .temp 91.4435143912212

    *Definition of type of analysis

    .TRAN 0.1n 42n

    .meas tran delay_lh_nodea trig v(nodea) val=0.5125886645991812 fall=1.0251773291983624 targ v(nodeZ) val=0.5125886645991812 rise=1.0251773291983624
    .meas tran delay_hl_nodea trig v(nodea) val=0.5125886645991812 rise=1.0251773291983624 targ v(nodeZ) val=0.5125886645991812 fall=1.0251773291983624

    .CONTROL
        run
    .ENDC

    .END
    