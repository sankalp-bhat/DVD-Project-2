
    * Technology Node
    .INCLUDE ../tech_nodes/22nm_HP.pm

    * Gates
    .INCLUDE NOT.sub
    .INCLUDE AND2.sub
    .INCLUDE OR2.sub
    .INCLUDE XOR2.sub
    .INCLUDE AND3.sub

    * Parameters
    .param pvdd = 1.090549802303397
    .param lmin = 4.553887373477018e-08
    .param wmin = 4.41205199621833e-08

    .param toxe_n = 9.253308892920463e-10
    .param toxm_n = 9.056633579038148e-10
    .param toxref_n = 9.048278450489465e-10
    .param toxp_par = 6.570864345309554e-10
    .param toxe_p = 9.00086970216268e-10
    .param toxm_p = 8.86177542802702e-10
    .param toxref_p = 8.88820014775967e-10
    .param xj_n = 1.5125811717120416e-08
    .param xj_p = 1.3965091008082506e-08
    .param ndep_p = 2.835598850392856e+18
    .param ndep_n = 6.54258743682457e+18

    
    .temp 14.01947338863998

    * Voltages
    Vdd supply gnd 1
    Vin1 nodeIN1 gnd 1
    Vin5 nodeIN5 gnd 1
    Vin9 nodeIN9 gnd 1
    Vin13 nodeIN13 gnd 1
    Vin17 nodeIN17 gnd 1
    Vin21 nodeIN21 gnd 1
    Vin25 nodeIN25 gnd 1
    Vin29 nodeIN29 gnd 1
    Vin33 nodeIN33 gnd 1
    Vin37 nodeIN37 gnd 1
    Vin41 nodeIN41 gnd 1
    Vin45 nodeIN45 gnd 1
    Vin49 nodeIN49 gnd 1
    Vin53 nodeIN53 gnd 1
    Vin57 nodeIN57 gnd 1
    Vin61 nodeIN61 gnd 1
    Vin65 nodeIN65 gnd 1
    Vin69 nodeIN69 gnd 1
    Vin73 nodeIN73 gnd 1
    Vin77 nodeIN77 gnd 1
    Vin81 nodeIN81 gnd 1
    Vin85 nodeIN85 gnd 1
    Vin89 nodeIN89 gnd 1
    Vin93 nodeIN93 gnd 1
    Vin97 nodeIN97 gnd 1
    Vin101 nodeIN101 gnd 1
    Vin105 nodeIN105 gnd 1
    Vin109 nodeIN109 gnd 1
    Vin113 nodeIN113 gnd 1
    Vin117 nodeIN117 gnd 1
    Vin121 nodeIN121 gnd 1
    Vin125 nodeIN125 gnd 1
    Vin129 nodeIN129 gnd 1
    Vin130 nodeIN130 gnd 1
    Vin131 nodeIN131 gnd 1
    Vin132 nodeIN132 gnd 1
    Vin133 nodeIN133 gnd 1
    Vin134 nodeIN134 gnd 1
    Vin135 nodeIN135 gnd 1
    Vin136 nodeIN136 gnd 1
    Vin137 nodeIN137 gnd 1

    * Circuit
    * Syndrome
    xXA0 nodeIN1 nodeIN5 nodeXA0 supply gnd XOR2
    xXA1 nodeIN9 nodeIN13 nodeXA1 supply gnd XOR2
    xXA2 nodeIN17 nodeIN21 nodeXA2 supply gnd XOR2
    xXA3 nodeIN25 nodeIN29 nodeXA3 supply gnd XOR2
    xXA4 nodeIN33 nodeIN37 nodeXA4 supply gnd XOR2
    xXA5 nodeIN41 nodeIN45 nodeXA5 supply gnd XOR2
    xXA6 nodeIN49 nodeIN53 nodeXA6 supply gnd XOR2
    xXA7 nodeIN57 nodeIN61 nodeXA7 supply gnd XOR2
    xXA8 nodeIN65 nodeIN69 nodeXA8 supply gnd XOR2
    xXA9 nodeIN73 nodeIN77 nodeXA9 supply gnd XOR2
    xXA10 nodeIN81 nodeIN85 nodeXA10 supply gnd XOR2
    xXA11 nodeIN89 nodeIN93 nodeXA11 supply gnd XOR2
    xXA12 nodeIN97 nodeIN101 nodeXA12 supply gnd XOR2
    xXA13 nodeIN105 nodeIN109 nodeXA13 supply gnd XOR2
    xXA14 nodeIN113 nodeIN117 nodeXA14 supply gnd XOR2
    xXA15 nodeIN121 nodeIN125 nodeXA13 supply gnd XOR2

    xF0 nodeXA0 nodeXA1 nodeF0 supply gnd XOR2
    xF1 nodeXA2 nodeXA3 nodeF1 supply gnd XOR2
    xF2 nodeXA4 nodeXA5 nodeF2 supply gnd XOR2
    xF3 nodeXA6 nodeXA7 nodeF3 supply gnd XOR2
    xF4 nodeXA8 nodeXA9 nodeF4 supply gnd XOR2
    xF5 nodeXA10 nodeXA11 nodeF5 supply gnd XOR2
    xF6 nodeXA12 nodeXA13 nodeF6 supply gnd XOR2
    xF7 nodeXA14 nodeXA15 nodeF7 supply gnd XOR2

    xH0 nodeIN129 nodeIN137 nodeH0 supply gnd AND2
    xH1 nodeIN130 nodeIN137 nodeH1 supply gnd AND2
    xH2 nodeIN131 nodeIN137 nodeH2 supply gnd AND2
    xH3 nodeIN132 nodeIN137 nodeH3 supply gnd AND2
    xH4 nodeIN133 nodeIN137 nodeH4 supply gnd AND2
    xH5 nodeIN134 nodeIN137 nodeH5 supply gnd AND2
    xH6 nodeIN135 nodeIN137 nodeH6 supply gnd AND2
    xH7 nodeIN136 nodeIN137 nodeH7 supply gnd AND2

    xXB0 nodeIN1 nodeIN17 nodeXB0 supply gnd XOR2
    xXB1 nodeIN5 nodeIN21 nodeXB1 supply gnd XOR2
    xXB2 nodeIN9 nodeIN25 nodeXB2 supply gnd XOR2
    xXB3 nodeIN13 nodeIN29 nodeXB3 supply gnd XOR2
    xXB4 nodeIN65 nodeIN81 nodeXB4 supply gnd XOR2
    xXB5 nodeIN69 nodeIN85 nodeXB5 supply gnd XOR2
    xXB6 nodeIN73 nodeIN89 nodeXB6 supply gnd XOR2
    xXB7 nodeIN77 nodeIN93 nodeXB7 supply gnd XOR2

    xXC0 nodeIN33 nodeIN49 nodeXC0 supply gnd XOR2
    xXC1 nodeIN37 nodeIN53 nodeXC1 supply gnd XOR2
    xXC2 nodeIN41 nodeIN57 nodeXC2 supply gnd XOR2
    xXC3 nodeIN45 nodeIN61 nodeXC3 supply gnd XOR2
    xXC4 nodeIN97 nodeIN113 nodeXC4 supply gnd XOR2
    xXC5 nodeIN101 nodeIN117 nodeXC5 supply gnd XOR2
    xXC6 nodeIN105 nodeIN121 nodeXC6 supply gnd XOR2
    xXC7 nodeIN109 nodeIN125 nodeXC7 supply gnd XOR2

    xXE0 nodeXB0 nodeXC0 nodeXE0 supply gnd XOR2
    xXE1 nodeXB1 nodeXC1 nodeXE1 supply gnd XOR2
    xXE2 nodeXB2 nodeXC2 nodeXE2 supply gnd XOR2
    xXE3 nodeXB3 nodeXC3 nodeXE3 supply gnd XOR2
    xXE4 nodeXB4 nodeXC4 nodeXE4 supply gnd XOR2
    xXE5 nodeXB5 nodeXC5 nodeXE5 supply gnd XOR2
    xXE6 nodeXB6 nodeXC6 nodeXE6 supply gnd XOR2
    xXE7 nodeXB7 nodeXC7 nodeXE7 supply gnd XOR2

    xG0 nodeF0 nodeF1 nodeG0 supply gnd XOR2
    xG1 nodeF2 nodeF3 nodeG1 supply gnd XOR2
    xG2 nodeF0 nodeF2 nodeG2 supply gnd XOR2
    xG3 nodeF1 nodeF3 nodeG3 supply gnd XOR2
    xG4 nodeF4 nodeF5 nodeG4 supply gnd XOR2
    xG5 nodeF6 nodeF7 nodeG5 supply gnd XOR2
    xG6 nodeF4 nodeF6 nodeG6 supply gnd XOR2
    xG7 nodeF5 nodeF7 nodeG7 supply gnd XOR2

    xXD0 nodeG4 nodeH0 nodeXD0 supply gnd XOR2
    xXD1 nodeG5 nodeH1 nodeXD1 supply gnd XOR2
    xXD2 nodeG6 nodeH2 nodeXD2 supply gnd XOR2
    xXD3 nodeG7 nodeH3 nodeXD3 supply gnd XOR2
    xXD4 nodeG0 nodeH4 nodeXD4 supply gnd XOR2
    xXD5 nodeG1 nodeH5 nodeXD5 supply gnd XOR2
    xXD6 nodeG2 nodeH6 nodeXD6 supply gnd XOR2
    xXD7 nodeG3 nodeH7 nodeXD7 supply gnd XOR2

    xS0 nodeXD0 nodeXE0 nodeS0 supply gnd XOR2
    xS1 nodeXD1 nodeXE1 nodeS1 supply gnd XOR2
    xS2 nodeXD2 nodeXE2 nodeS2 supply gnd XOR2
    xS3 nodeXD3 nodeXE3 nodeS3 supply gnd XOR2
    xS4 nodeXD4 nodeXE4 nodeS4 supply gnd XOR2
    xS5 nodeXD5 nodeXE5 nodeS5 supply gnd XOR2
    xS6 nodeXD6 nodeXE6 nodeS6 supply gnd XOR2
    xS7 nodeXD7 nodeXE7 nodeS7 supply gnd XOR2

    * Correction
    xS0B0 nodeS0 nodeS0B0 supply gnd NOT
    xS0B1 nodeS0 nodeS0B1 supply gnd NOT
    xS0B2 nodeS0 nodeS0B2 supply gnd NOT
    xS0B3 nodeS0 nodeS0B3 supply gnd NOT
    xS0B4 nodeS0 nodeS0B4 supply gnd NOT
    xS1B0 nodeS1 nodeS1B0 supply gnd NOT
    xS1B1 nodeS1 nodeS1B1 supply gnd NOT
    xS1B2 nodeS1 nodeS1B2 supply gnd NOT
    xS1B3 nodeS1 nodeS1B3 supply gnd NOT
    xS1B4 nodeS1 nodeS1B4 supply gnd NOT
    xS2B0 nodeS2 nodeS2B0 supply gnd NOT
    xS2B1 nodeS2 nodeS2B1 supply gnd NOT
    xS2B2 nodeS2 nodeS2B2 supply gnd NOT
    xS2B3 nodeS2 nodeS2B3 supply gnd NOT
    xS2B4 nodeS2 nodeS2B4 supply gnd NOT
    xS3B0 nodeS3 nodeS3B0 supply gnd NOT
    xS3B1 nodeS3 nodeS3B1 supply gnd NOT
    xS3B2 nodeS3 nodeS3B2 supply gnd NOT
    xS3B3 nodeS3 nodeS3B3 supply gnd NOT
    xS3B4 nodeS3 nodeS3B4 supply gnd NOT
    xS4B0 nodeS4 nodeS4B0 supply gnd NOT
    xS4B1 nodeS4 nodeS4B1 supply gnd NOT
    xS4B2 nodeS4 nodeS4B2 supply gnd NOT
    xS4B3 nodeS4 nodeS4B3 supply gnd NOT
    xS4B4 nodeS4 nodeS4B4 supply gnd NOT
    xS5B0 nodeS5 nodeS5B0 supply gnd NOT
    xS5B1 nodeS5 nodeS5B1 supply gnd NOT
    xS5B2 nodeS5 nodeS5B2 supply gnd NOT
    xS5B3 nodeS5 nodeS5B3 supply gnd NOT
    xS5B4 nodeS5 nodeS5B4 supply gnd NOT
    xS6B0 nodeS6 nodeS6B0 supply gnd NOT
    xS6B1 nodeS6 nodeS6B1 supply gnd NOT
    xS6B2 nodeS6 nodeS6B2 supply gnd NOT
    xS6B3 nodeS6 nodeS6B3 supply gnd NOT
    xS6B4 nodeS6 nodeS6B4 supply gnd NOT
    xS7B0 nodeS7 nodeS7B0 supply gnd NOT
    xS7B1 nodeS7 nodeS7B1 supply gnd NOT
    xS7B2 nodeS7 nodeS7B2 supply gnd NOT
    xS7B3 nodeS7 nodeS7B3 supply gnd NOT
    xS7B4 nodeS7 nodeS7B4 supply gnd NOT

    xT00 nodeS0B0 nodeS1B0 nodeS2B0 nodeT00 supply gnd AND3
    xT0 nodeT00 nodeS3 nodeT0 supply gnd AND2
    xT10 nodeS0B1 nodeS1B1 nodeS2 nodeT10 supply gnd AND3
    xT1 nodeT10 nodeS3B0 nodeT1 supply gnd AND2
    xT20 nodeS0B2 nodeS1 nodeS2B1 nodeT20 supply gnd AND3
    xT2 nodeT20 nodeS3B1 nodeT2 supply gnd AND2
    xT30 nodeS0 nodeS1B2 nodeS2B2 nodeT30 supply gnd AND3
    xT3 nodeT30 nodeS3B2 nodeT3 supply gnd AND2
    xT40 nodeS4B0 nodeS5B0 nodeS6B0 nodeT40 supply gnd AND3
    xT4 nodeT40 nodeS7 nodeT4 supply gnd AND2
    xT50 nodeS4B1 nodeS5B1 nodeS6 nodeT50 supply gnd AND3
    xT5 nodeT50 nodeS3B0 nodeT5 supply gnd AND2
    xT60 nodeS4B2 nodeS5 nodeS6B1 nodeT60 supply gnd AND3
    xT6 nodeT60 nodeS7B1 nodeT6 supply gnd AND2
    xT70 nodeS4 nodeS5B2 nodeS6B2 nodeT70 supply gnd AND3
    xT7 nodeT00 nodeS7B2 nodeT7 supply gnd AND2

    xU00 nodeT0 nodeT1 nodeU00 supply gnd OR2
    xU01 nodeT2 nodeT3 nodeU01 supply gnd OR2
    xU0 nodeU00 nodeU01 nodeU0 supply gnd OR2
    xU10 nodeT4 nodeT5 nodeU10 supply gnd OR2
    xU11 nodeT6 nodeT7 nodeU11 supply gnd OR2
    xU1 nodeU10 nodeU11 nodeU1 supply gnd OR2

    xW00 nodeS4 nodeS5B3 nodeS6 nodeW00 supply gnd AND3
    xW0 nodeW00 nodeS7B3 nodeU0 nodeW0 supply gnd AND3
    xW10 nodeS4 nodeS5B4 nodeS6B3 nodeW10 supply gnd AND3
    xW1 nodeW10 nodeS7 nodeU0 nodeW1 supply gnd AND3
    xW20 nodeS4B3 nodeS5 nodeS6 nodeW20 supply gnd AND3
    xW2 nodeW20 nodeS7B4 nodeU0 nodeW2 supply gnd AND3
    xW30 nodeS4B4 nodeS5 nodeS6B4 nodeW30 supply gnd AND3
    xW3 nodeW30 nodeS7 nodeU0 nodeW3 supply gnd AND3
    xW40 nodeS0 nodeS1B3 nodeS2 nodeW40 supply gnd AND3
    xW4 nodeW40 nodeS3B3 nodeU1 nodeW4 supply gnd AND3
    xW50 nodeS0 nodeS1B4 nodeS2B3 nodeW50 supply gnd AND3
    xW5 nodeW50 nodeS3 nodeU1 nodeW5 supply gnd AND3
    xW60 nodeS0B3 nodeS1 nodeS2 nodeW60 supply gnd AND3
    xW6 nodeW20 nodeS3B4 nodeU1 nodeW6 supply gnd AND3
    xW70 nodeS0B4 nodeS1 nodeS2B4 nodeW70 supply gnd AND3
    xW7 nodeW30 nodeS3 nodeU1 nodeW7 supply gnd AND3

    xE0 nodeW0 nodeS0 nodeE0 supply gnd AND2
    xE1 nodeW0 nodeS1 nodeE1 supply gnd AND2
    xE2 nodeW0 nodeS2 nodeE2 supply gnd AND2
    xE3 nodeW0 nodeS3 nodeE3 supply gnd AND2
    xE4 nodeW1 nodeS0 nodeE4 supply gnd AND2
    xE5 nodeW1 nodeS1 nodeE5 supply gnd AND2
    xE6 nodeW1 nodeS2 nodeE6 supply gnd AND2
    xE7 nodeW1 nodeS3 nodeE7 supply gnd AND2
    xE8 nodeW2 nodeS0 nodeE8 supply gnd AND2
    xE9 nodeW2 nodeS1 nodeE9 supply gnd AND2
    xE10 nodeW2 nodeS2 nodeE10 supply gnd AND2
    xE11 nodeW2 nodeS3 nodeE11 supply gnd AND2
    xE12 nodeW3 nodeS0 nodeE12 supply gnd AND2
    xE13 nodeW3 nodeS1 nodeE13 supply gnd AND2
    xE14 nodeW3 nodeS2 nodeE14 supply gnd AND2
    xE15 nodeW3 nodeS3 nodeE15 supply gnd AND2
    xE16 nodeW4 nodeS4 nodeE16 supply gnd AND2
    xE17 nodeW4 nodeS5 nodeE17 supply gnd AND2
    xE18 nodeW4 nodeS6 nodeE18 supply gnd AND2
    xE19 nodeW4 nodeS7 nodeE19 supply gnd AND2
    xE20 nodeW5 nodeS4 nodeE20 supply gnd AND2
    xE21 nodeW5 nodeS5 nodeE21 supply gnd AND2
    xE22 nodeW5 nodeS6 nodeE22 supply gnd AND2
    xE23 nodeW5 nodeS7 nodeE23 supply gnd AND2
    xE24 nodeW6 nodeS4 nodeE24 supply gnd AND2
    xE25 nodeW6 nodeS5 nodeE25 supply gnd AND2
    xE26 nodeW6 nodeS6 nodeE26 supply gnd AND2
    xE27 nodeW6 nodeS7 nodeE27 supply gnd AND2
    xE28 nodeW7 nodeS4 nodeE28 supply gnd AND2
    xE29 nodeW7 nodeS5 nodeE29 supply gnd AND2
    xE30 nodeW7 nodeS6 nodeE30 supply gnd AND2
    xE31 nodeW7 nodeS7 nodeE31 supply gnd AND2

    xOD0 nodeID0 nodeE0 nodeOD0 supply gnd XOR2
    xOD1 nodeID1 nodeE1 nodeOD1 supply gnd XOR2
    xOD2 nodeID2 nodeE2 nodeOD2 supply gnd XOR2
    xOD3 nodeID3 nodeE3 nodeOD3 supply gnd XOR2
    xOD4 nodeID4 nodeE4 nodeOD4 supply gnd XOR2
    xOD5 nodeID5 nodeE5 nodeOD5 supply gnd XOR2
    xOD6 nodeID6 nodeE6 nodeOD6 supply gnd XOR2
    xOD7 nodeID7 nodeE7 nodeOD7 supply gnd XOR2
    xOD8 nodeID8 nodeE8 nodeOD8 supply gnd XOR2
    xOD9 nodeID9 nodeE9 nodeOD9 supply gnd XOR2
    xOD10 nodeID10 nodeE10 nodeOD10 supply gnd XOR2
    xOD11 nodeID11 nodeE11 nodeOD11 supply gnd XOR2
    xOD12 nodeID12 nodeE12 nodeOD12 supply gnd XOR2
    xOD13 nodeID13 nodeE13 nodeOD13 supply gnd XOR2
    xOD14 nodeID14 nodeE14 nodeOD14 supply gnd XOR2
    xOD15 nodeID15 nodeE15 nodeOD15 supply gnd XOR2
    xOD16 nodeID16 nodeE16 nodeOD16 supply gnd XOR2
    xOD17 nodeID17 nodeE17 nodeOD17 supply gnd XOR2
    xOD18 nodeID18 nodeE18 nodeOD18 supply gnd XOR2
    xOD19 nodeID19 nodeE19 nodeOD19 supply gnd XOR2
    xOD20 nodeID20 nodeE20 nodeOD20 supply gnd XOR2
    xOD21 nodeID21 nodeE21 nodeOD21 supply gnd XOR2
    xOD22 nodeID22 nodeE22 nodeOD22 supply gnd XOR2
    xOD23 nodeID23 nodeE23 nodeOD23 supply gnd XOR2
    xOD24 nodeID24 nodeE24 nodeOD24 supply gnd XOR2
    xOD25 nodeID25 nodeE25 nodeOD25 supply gnd XOR2
    xOD26 nodeID26 nodeE26 nodeOD26 supply gnd XOR2
    xOD27 nodeID27 nodeE27 nodeOD27 supply gnd XOR2
    xOD28 nodeID28 nodeE28 nodeOD28 supply gnd XOR2
    xOD29 nodeID29 nodeE29 nodeOD29 supply gnd XOR2
    xOD30 nodeID30 nodeE30 nodeOD30 supply gnd XOR2
    xOD31 nodeID31 nodeE31 nodeOD31 supply gnd XOR2

    * Control
    .control

    op
    run

    * let P_Vdd = abs(I(Vdd) * pvdd)
    print (-(V(supply)*I(Vdd)))

    .endc
    .end
    