from sci import *

import os

qatom.basis = baslib("def2-svp") # Molecule Basis Set
Ctz = baslib("def2-TZVPP").C
Csvp = baslib("def2-SVP").C
Cotz = baslib("def2-TZVPP").Co
Cosvp = baslib("def2-SVP").Co
Ntz = baslib("def2-TZVPP").N
Nsvp = baslib("def2-SVP").N
geom = [
qatom(atom.C, [-1.95194600, -3.80064700, 12.01017100]),
qatom(atom.C, [-2.67048600, -3.29382100, 10.90321300]),
qatom(atom.C, [-2.02521000, -3.68893400, 9.67438300]),
qatom(atom.C, [-0.67595100, -4.22685200, 9.67329300]),
qatom(atom.C, [0.06718700, -4.37327200, 10.90135600]),
qatom(atom.C, [-0.80605000, -4.25214400, 12.00630600]),
qatom(atom.C, [1.46363000, -4.14305000, 10.90029200]),
qatom(atom.C, [2.11669000, -3.76017900, 9.67147000]),
qatom(atom.C, [1.43960100, -4.01417500, 8.43755000]),
qatom(atom.C, [0.04598600, -4.24771300, 8.43891400]),
qatom(atom.C, [2.25090800, -3.74829200, 12.00635500]),
qatom(atom.C, [3.18043500, -2.94021700, 12.00634300]),
qatom(atom.C, [3.68443000, -2.21677700, 10.90170600]),
qatom(atom.C, [3.21163800, -2.80513500, 9.67166100]),
qatom(atom.C, [3.55231400, -2.16545000, 8.43873600]),
qatom(atom.C, [3.99172400, -0.82244200, 8.44195200]),
qatom(atom.C, [4.10027100, -0.11198700, 9.67894300]),
qatom(atom.C, [4.12572700, -0.87278700, 10.90468600]),
qatom(atom.C, [3.15038700, -2.76347400, 7.19232900]),
qatom(atom.C, [2.08927200, -3.70056600, 7.19177100]),
qatom(atom.C, [1.44970300, -4.02062400, 5.96514900]),
qatom(atom.C, [0.03459300, -4.26167000, 5.96634600]),
qatom(atom.C, [-0.67250400, -4.16764000, 7.19424200]),
qatom(atom.C, [-1.98622100, -3.64175200, 7.19475600]),
qatom(atom.C, [-2.56576700, -3.21049400, 8.43967800]),
qatom(atom.C, [3.54680500, -2.16754200, 5.96632000]),
qatom(atom.C, [3.13973900, -2.75051300, 4.73827400]),
qatom(atom.C, [2.08224500, -3.69142800, 4.73790900]),
qatom(atom.C, [1.43039600, -4.00203000, 3.49347100]),
qatom(atom.C, [0.04100200, -4.24552200, 3.49454200]),
qatom(atom.C, [-0.67491200, -4.16815900, 4.74002900]),
qatom(atom.C, [-1.98992500, -3.64428900, 4.74050100]),
qatom(atom.C, [-2.56758000, -3.22750900, 5.96771000]),
qatom(atom.C, [3.53134400, -2.14213300, 3.49545000]),
qatom(atom.C, [3.18820400, -2.77515600, 2.26222400]),
qatom(atom.C, [2.10326200, -3.73828100, 2.26075800]),
qatom(atom.C, [1.45213500, -4.12198000, 1.03366800]),
qatom(atom.C, [0.05775700, -4.36941400, 1.03516900]),
qatom(atom.C, [-0.68375000, -4.22964200, 2.26316300]),
qatom(atom.C, [-2.03396500, -3.69939600, 2.26438400]),
qatom(atom.C, [-2.57155100, -3.21579100, 3.49682400]),
qatom(atom.C, [3.65002100, -2.17520600, 1.03581600]),
qatom(atom.C, [3.14921000, -2.89518500, -0.07153600]),
qatom(atom.C, [2.22919900, -3.71424700, -0.07412400]),
qatom(atom.C, [-2.67898700, -3.30486200, 1.03757800]),
qatom(atom.C, [-1.96229200, -3.81070300, -0.06969600]),
qatom(atom.C, [-0.81438100, -4.25702200, -0.07058300]),
qatom(atom.C, [-3.45205100, -2.11443800, 3.49643200]),
qatom(atom.C, [-3.81114600, -1.48719100, 2.26464400]),
qatom(atom.C, [-3.56430300, -2.20141600, 1.03804600]),
qatom(atom.C, [-3.45930700, -2.10524300, 5.96638900]),
qatom(atom.C, [-3.74269000, -1.45304600, 4.73926100]),
qatom(atom.C, [-4.00349700, -0.06218300, 4.73758900]),
qatom(atom.C, [-3.96365200, 0.65531800, 3.49394200]),
qatom(atom.C, [-4.07050300, -0.06064500, 2.26353500]),
qatom(atom.C, [-4.08469500, 0.69313400, 1.03596800]),
qatom(atom.C, [-4.13209900, -0.18510800, -0.06948200]),
qatom(atom.C, [-3.91412800, -1.39712500, -0.06971600]),
qatom(atom.C, [-3.52764900, 1.99480300, 3.49448600]),
qatom(atom.C, [-3.17940700, 2.62940700, 2.26546900]),
qatom(atom.C, [-3.64015600, 2.03570700, 1.03608400]),
qatom(atom.C, [-3.98599800, 0.65214300, 5.96307700]),
qatom(atom.C, [-3.56398600, 2.02299900, 5.96431300]),
qatom(atom.C, [-3.14672900, 2.60500300, 4.73882800]),
qatom(atom.C, [-2.08939700, 3.54634400, 4.74406400]),
qatom(atom.C, [-1.43346300, 3.86141300, 3.50521100]),
qatom(atom.C, [-2.09954500, 3.59482500, 2.27171800]),
qatom(atom.C, [-1.44650500, 3.98163300, 1.04796700]),
qatom(atom.C, [-2.21947700, 3.57634200, -0.06305600]),
qatom(atom.C, [-3.14035800, 2.75844700, -0.06974100]),
qatom(atom.C, [-0.04495000, 4.10225200, 3.51190600]),
qatom(atom.C, [0.68263600, 4.08485200, 2.28442700]),
qatom(atom.C, [-0.05404600, 4.22973700, 1.05482100]),
qatom(atom.C, [-1.46479900, 3.87381400, 5.97573600]),
qatom(atom.C, [-0.04735400, 4.09820400, 5.98151600]),
qatom(atom.C, [0.66476200, 4.00798100, 4.75760900]),
qatom(atom.C, [1.97852900, 3.48283400, 4.75908800]),
qatom(atom.C, [2.56719900, 3.06672800, 3.51584400]),
qatom(atom.C, [2.03012000, 3.55274100, 2.28616700]),
qatom(atom.C, [2.67657700, 3.16449900, 1.05874100]),
qatom(atom.C, [1.96480200, 3.67551600, -0.04891900]),
qatom(atom.C, [0.81834000, 4.12501300, -0.05106300]),
qatom(atom.C, [3.45182100, 1.96917500, 3.51180500]),
qatom(atom.C, [3.80889300, 1.34480000, 2.27883500]),
qatom(atom.C, [3.55968500, 2.06103000, 1.05487000]),
qatom(atom.C, [2.55345900, 3.05961200, 5.98482300]),
qatom(atom.C, [3.45820200, 1.94844100, 5.98124400]),
qatom(atom.C, [3.74380200, 1.30348400, 4.75071200]),
qatom(atom.C, [4.00853700, -0.08617400, 4.74562900]),
qatom(atom.C, [3.96538100, -0.80093500, 3.49964900]),
qatom(atom.C, [4.07129900, -0.08096300, 2.27147600]),
qatom(atom.C, [4.09099700, -0.83082400, 1.04116500]),
qatom(atom.C, [4.13584900, 0.05020800, -0.06246800]),
qatom(atom.C, [3.91264400, 1.26122800, -0.05514800]),
qatom(atom.C, [3.98794000, -0.80342900, 5.96959600]),
qatom(atom.C, [4.02466800, -0.09669400, 7.19967400]),
qatom(atom.C, [3.75246500, 1.29215500, 7.20514500]),
qatom(atom.C, [3.44903600, 1.94044600, 8.45342900]),
qatom(atom.C, [2.54837100, 3.02957500, 8.45715300]),
qatom(atom.C, [1.96829100, 3.46320100, 7.21357100]),
qatom(atom.C, [0.65451200, 3.98904100, 7.21144600]),
qatom(atom.C, [-0.06633300, 4.07442600, 8.45523100]),
qatom(atom.C, [-1.46916800, 3.86855800, 8.45008000]),
qatom(atom.C, [-2.11881400, 3.56312900, 7.19964400]),
qatom(atom.C, [-3.18332300, 2.62561200, 7.19470900]),
qatom(atom.C, [-3.58584400, 2.01873700, 8.43916200]),
qatom(atom.C, [-3.99895200, 0.66225800, 8.43725900]),
qatom(atom.C, [-4.01547500, -0.06079100, 7.19076200]),
qatom(atom.C, [-3.74568000, -1.45074300, 7.19286100]),
qatom(atom.C, [-3.45235800, -2.10967800, 8.43834200]),
qatom(atom.C, [3.81610300, 1.31276900, 9.68532000]),
qatom(atom.C, [3.55320000, 2.01678600, 10.91753000]),
qatom(atom.C, [2.64939100, 3.10416400, 10.92153900]),
qatom(atom.C, [2.00309000, 3.49949600, 9.69327100]),
qatom(atom.C, [0.65361300, 4.03668000, 9.69298600]),
qatom(atom.C, [-0.08953400, 4.18818700, 10.92072900]),
qatom(atom.C, [-1.48882200, 3.97274900, 10.91654000]),
qatom(atom.C, [-2.14731600, 3.60588800, 9.68430500]),
qatom(atom.C, [-3.24305200, 2.64953400, 9.67832800]),
qatom(atom.C, [-3.70574600, 2.04455700, 10.90561500]),
qatom(atom.C, [-4.13378600, 0.69597000, 10.90170000]),
qatom(atom.C, [-4.09748900, -0.05791300, 9.67178700]),
qatom(atom.C, [-3.81762100, -1.48462300, 9.67157700]),
qatom(atom.C, [-3.56244300, -2.19662200, 10.90095300]),
qatom(atom.C, [4.16007800, 0.00436100, 12.01261300]),
qatom(atom.C, [3.91915200, 1.21196700, 12.02062900]),
qatom(atom.C, [0.77902700, 4.06224100, 12.02857900]),
qatom(atom.C, [1.92259200, 3.60469200, 12.02519600]),
qatom(atom.C, [-3.20497300, 2.76220600, 12.01422300]),
qatom(atom.C, [-2.27601800, 3.57083100, 12.01875700]),
qatom(atom.C, [-3.92719600, -1.39124200, 12.00348700]),
qatom(atom.C, [-4.17005800, -0.18408100, 12.00699900]),
qatom(atom.C, [-0.41104100, 0.67817000, 6.68894700]),
qatom(atom.H, [0.59597600, 1.04894900, 6.49601800]),
qatom(atom.H, [-1.13268500, 1.25653100, 6.11950400]),
qatom(atom.H, [-0.49274400, -0.37326900, 6.41245900]),
qatom(atom.Cl, [-0.00621900, 0.71077200, 3.75908400]),
qatom(atom.N, [-0.71860800, 0.82921200, 8.16965100]),
qatom(atom.H, [-1.69050000, 0.55768700, 8.37547600]),
qatom(atom.H, [-0.61157100, 1.81216600, 8.46131600]),
qatom(atom.H, [-0.09455000, 0.25752800, 8.74727200]),
qatom(atom.H, [3.62176398, -2.70820005, -1.01314598]),
qatom(atom.H, [1.99321055, -4.16506082, -1.01538717]),
qatom(atom.H, [-0.43617817, -4.59691267, -1.01203770]),
qatom(atom.H, [-2.47237881, -3.80553494, -1.01027281]),
qatom(atom.H, [-3.99898497, -1.89601160, -1.01248397]),
qatom(atom.H, [-4.38592989, 0.25190373, -1.01261011]),
qatom(atom.H, [-3.61153849, 2.57615785, -1.01295869]),
qatom(atom.H, [-1.97839416, 4.02973792, -1.00178451]),
qatom(atom.H, [0.44313315, 4.47330208, -0.99064511]),
qatom(atom.H, [2.47734323, 3.67168279, -0.98816699]),
qatom(atom.H, [3.99533580, 1.76469987, -0.99566814]),
qatom(atom.H, [4.39156801, -0.38180889, -1.00738556]),
qatom(atom.H, [-4.00110728, -1.88970494, 12.94740004]),
qatom(atom.H, [-4.43776531, 0.24549797, 12.94970505]),
qatom(atom.H, [-3.68550252, 2.58374056, 12.95344686]),
qatom(atom.H, [-2.03900629, 4.01828867, 12.96136354]),
qatom(atom.H, [0.40279565, 4.40067113, 12.97134886]),
qatom(atom.H, [2.42510303, 3.58373845, 12.96962366]),
qatom(atom.H, [3.99514740, 1.70644846, 12.96646873]),
qatom(atom.H, [4.42617164, -0.43130685, 12.95297873]),
qatom(atom.H, [3.65964816, -2.76660452, 12.94714769]),
qatom(atom.H, [2.01319124, -4.20108001, 12.94623465]),
qatom(atom.H, [-0.42796873, -4.59185222, 12.94787537]),
qatom(atom.H, [-2.45808716, -3.79097127, 12.95284141]),
] 

qatom.unit = unit.angstrom

qmolecule = molecule( geom, charge=0, mult=1, sym=sym.C1 )
print qmolecule

qatom.basis = baslib("def2-svp/jkfit")
Ctz = baslib("def2-TZVPP/jkfit").C
Csvp = baslib("def2-SVP/jkfit").C
Cotz = baslib("def2-TZVPP/jkfit").Co
Cosvp = baslib("def2-SVP/jkfit").Co
Ntz = baslib("def2-TZVPP/jkfit").N
Nsvp = baslib("def2-SVP/jkfit").N

acene = [
qatom(atom.C, [-1.95194600, -3.80064700, 12.01017100]),
qatom(atom.C, [-2.67048600, -3.29382100, 10.90321300]),
qatom(atom.C, [-2.02521000, -3.68893400, 9.67438300]),
qatom(atom.C, [-0.67595100, -4.22685200, 9.67329300]),
qatom(atom.C, [0.06718700, -4.37327200, 10.90135600]),
qatom(atom.C, [-0.80605000, -4.25214400, 12.00630600]),
qatom(atom.C, [1.46363000, -4.14305000, 10.90029200]),
qatom(atom.C, [2.11669000, -3.76017900, 9.67147000]),
qatom(atom.C, [1.43960100, -4.01417500, 8.43755000]),
qatom(atom.C, [0.04598600, -4.24771300, 8.43891400]),
qatom(atom.C, [2.25090800, -3.74829200, 12.00635500]),
qatom(atom.C, [3.18043500, -2.94021700, 12.00634300]),
qatom(atom.C, [3.68443000, -2.21677700, 10.90170600]),
qatom(atom.C, [3.21163800, -2.80513500, 9.67166100]),
qatom(atom.C, [3.55231400, -2.16545000, 8.43873600]),
qatom(atom.C, [3.99172400, -0.82244200, 8.44195200]),
qatom(atom.C, [4.10027100, -0.11198700, 9.67894300]),
qatom(atom.C, [4.12572700, -0.87278700, 10.90468600]),
qatom(atom.C, [3.15038700, -2.76347400, 7.19232900]),
qatom(atom.C, [2.08927200, -3.70056600, 7.19177100]),
qatom(atom.C, [1.44970300, -4.02062400, 5.96514900]),
qatom(atom.C, [0.03459300, -4.26167000, 5.96634600]),
qatom(atom.C, [-0.67250400, -4.16764000, 7.19424200]),
qatom(atom.C, [-1.98622100, -3.64175200, 7.19475600]),
qatom(atom.C, [-2.56576700, -3.21049400, 8.43967800]),
qatom(atom.C, [3.54680500, -2.16754200, 5.96632000]),
qatom(atom.C, [3.13973900, -2.75051300, 4.73827400]),
qatom(atom.C, [2.08224500, -3.69142800, 4.73790900]),
qatom(atom.C, [1.43039600, -4.00203000, 3.49347100]),
qatom(atom.C, [0.04100200, -4.24552200, 3.49454200]),
qatom(atom.C, [-0.67491200, -4.16815900, 4.74002900]),
qatom(atom.C, [-1.98992500, -3.64428900, 4.74050100]),
qatom(atom.C, [-2.56758000, -3.22750900, 5.96771000]),
qatom(atom.C, [3.53134400, -2.14213300, 3.49545000]),
qatom(atom.C, [3.18820400, -2.77515600, 2.26222400]),
qatom(atom.C, [2.10326200, -3.73828100, 2.26075800]),
qatom(atom.C, [1.45213500, -4.12198000, 1.03366800]),
qatom(atom.C, [0.05775700, -4.36941400, 1.03516900]),
qatom(atom.C, [-0.68375000, -4.22964200, 2.26316300]),
qatom(atom.C, [-2.03396500, -3.69939600, 2.26438400]),
qatom(atom.C, [-2.57155100, -3.21579100, 3.49682400]),
qatom(atom.C, [3.65002100, -2.17520600, 1.03581600]),
qatom(atom.C, [3.14921000, -2.89518500, -0.07153600]),
qatom(atom.C, [2.22919900, -3.71424700, -0.07412400]),
qatom(atom.C, [-2.67898700, -3.30486200, 1.03757800]),
qatom(atom.C, [-1.96229200, -3.81070300, -0.06969600]),
qatom(atom.C, [-0.81438100, -4.25702200, -0.07058300]),
qatom(atom.C, [-3.45205100, -2.11443800, 3.49643200]),
qatom(atom.C, [-3.81114600, -1.48719100, 2.26464400]),
qatom(atom.C, [-3.56430300, -2.20141600, 1.03804600]),
qatom(atom.C, [-3.45930700, -2.10524300, 5.96638900]),
qatom(atom.C, [-3.74269000, -1.45304600, 4.73926100]),
qatom(atom.C, [-4.00349700, -0.06218300, 4.73758900]),
qatom(atom.C, [-3.96365200, 0.65531800, 3.49394200]),
qatom(atom.C, [-4.07050300, -0.06064500, 2.26353500]),
qatom(atom.C, [-4.08469500, 0.69313400, 1.03596800]),
qatom(atom.C, [-4.13209900, -0.18510800, -0.06948200]),
qatom(atom.C, [-3.91412800, -1.39712500, -0.06971600]),
qatom(atom.C, [-3.52764900, 1.99480300, 3.49448600]),
qatom(atom.C, [-3.17940700, 2.62940700, 2.26546900]),
qatom(atom.C, [-3.64015600, 2.03570700, 1.03608400]),
qatom(atom.C, [-3.98599800, 0.65214300, 5.96307700]),
qatom(atom.C, [-3.56398600, 2.02299900, 5.96431300]),
qatom(atom.C, [-3.14672900, 2.60500300, 4.73882800]),
qatom(atom.C, [-2.08939700, 3.54634400, 4.74406400]),
qatom(atom.C, [-1.43346300, 3.86141300, 3.50521100]),
qatom(atom.C, [-2.09954500, 3.59482500, 2.27171800]),
qatom(atom.C, [-1.44650500, 3.98163300, 1.04796700]),
qatom(atom.C, [-2.21947700, 3.57634200, -0.06305600]),
qatom(atom.C, [-3.14035800, 2.75844700, -0.06974100]),
qatom(atom.C, [-0.04495000, 4.10225200, 3.51190600]),
qatom(atom.C, [0.68263600, 4.08485200, 2.28442700]),
qatom(atom.C, [-0.05404600, 4.22973700, 1.05482100]),
qatom(atom.C, [-1.46479900, 3.87381400, 5.97573600]),
qatom(atom.C, [-0.04735400, 4.09820400, 5.98151600]),
qatom(atom.C, [0.66476200, 4.00798100, 4.75760900]),
qatom(atom.C, [1.97852900, 3.48283400, 4.75908800]),
qatom(atom.C, [2.56719900, 3.06672800, 3.51584400]),
qatom(atom.C, [2.03012000, 3.55274100, 2.28616700]),
qatom(atom.C, [2.67657700, 3.16449900, 1.05874100]),
qatom(atom.C, [1.96480200, 3.67551600, -0.04891900]),
qatom(atom.C, [0.81834000, 4.12501300, -0.05106300]),
qatom(atom.C, [3.45182100, 1.96917500, 3.51180500]),
qatom(atom.C, [3.80889300, 1.34480000, 2.27883500]),
qatom(atom.C, [3.55968500, 2.06103000, 1.05487000]),
qatom(atom.C, [2.55345900, 3.05961200, 5.98482300]),
qatom(atom.C, [3.45820200, 1.94844100, 5.98124400]),
qatom(atom.C, [3.74380200, 1.30348400, 4.75071200]),
qatom(atom.C, [4.00853700, -0.08617400, 4.74562900]),
qatom(atom.C, [3.96538100, -0.80093500, 3.49964900]),
qatom(atom.C, [4.07129900, -0.08096300, 2.27147600]),
qatom(atom.C, [4.09099700, -0.83082400, 1.04116500]),
qatom(atom.C, [4.13584900, 0.05020800, -0.06246800]),
qatom(atom.C, [3.91264400, 1.26122800, -0.05514800]),
qatom(atom.C, [3.98794000, -0.80342900, 5.96959600]),
qatom(atom.C, [4.02466800, -0.09669400, 7.19967400]),
qatom(atom.C, [3.75246500, 1.29215500, 7.20514500]),
qatom(atom.C, [3.44903600, 1.94044600, 8.45342900]),
qatom(atom.C, [2.54837100, 3.02957500, 8.45715300]),
qatom(atom.C, [1.96829100, 3.46320100, 7.21357100]),
qatom(atom.C, [0.65451200, 3.98904100, 7.21144600]),
qatom(atom.C, [-0.06633300, 4.07442600, 8.45523100]),
qatom(atom.C, [-1.46916800, 3.86855800, 8.45008000]),
qatom(atom.C, [-2.11881400, 3.56312900, 7.19964400]),
qatom(atom.C, [-3.18332300, 2.62561200, 7.19470900]),
qatom(atom.C, [-3.58584400, 2.01873700, 8.43916200]),
qatom(atom.C, [-3.99895200, 0.66225800, 8.43725900]),
qatom(atom.C, [-4.01547500, -0.06079100, 7.19076200]),
qatom(atom.C, [-3.74568000, -1.45074300, 7.19286100]),
qatom(atom.C, [-3.45235800, -2.10967800, 8.43834200]),
qatom(atom.C, [3.81610300, 1.31276900, 9.68532000]),
qatom(atom.C, [3.55320000, 2.01678600, 10.91753000]),
qatom(atom.C, [2.64939100, 3.10416400, 10.92153900]),
qatom(atom.C, [2.00309000, 3.49949600, 9.69327100]),
qatom(atom.C, [0.65361300, 4.03668000, 9.69298600]),
qatom(atom.C, [-0.08953400, 4.18818700, 10.92072900]),
qatom(atom.C, [-1.48882200, 3.97274900, 10.91654000]),
qatom(atom.C, [-2.14731600, 3.60588800, 9.68430500]),
qatom(atom.C, [-3.24305200, 2.64953400, 9.67832800]),
qatom(atom.C, [-3.70574600, 2.04455700, 10.90561500]),
qatom(atom.C, [-4.13378600, 0.69597000, 10.90170000]),
qatom(atom.C, [-4.09748900, -0.05791300, 9.67178700]),
qatom(atom.C, [-3.81762100, -1.48462300, 9.67157700]),
qatom(atom.C, [-3.56244300, -2.19662200, 10.90095300]),
qatom(atom.C, [4.16007800, 0.00436100, 12.01261300]),
qatom(atom.C, [3.91915200, 1.21196700, 12.02062900]),
qatom(atom.C, [0.77902700, 4.06224100, 12.02857900]),
qatom(atom.C, [1.92259200, 3.60469200, 12.02519600]),
qatom(atom.C, [-3.20497300, 2.76220600, 12.01422300]),
qatom(atom.C, [-2.27601800, 3.57083100, 12.01875700]),
qatom(atom.C, [-3.92719600, -1.39124200, 12.00348700]),
qatom(atom.C, [-4.17005800, -0.18408100, 12.00699900]),
qatom(atom.C, [-0.41104100, 0.67817000, 6.68894700]),
qatom(atom.H, [0.59597600, 1.04894900, 6.49601800]),
qatom(atom.H, [-1.13268500, 1.25653100, 6.11950400]),
qatom(atom.H, [-0.49274400, -0.37326900, 6.41245900]),
qatom(atom.Cl, [-0.00621900, 0.71077200, 3.75908400]),
qatom(atom.N, [-0.71860800, 0.82921200, 8.16965100]),
qatom(atom.H, [-1.69050000, 0.55768700, 8.37547600]),
qatom(atom.H, [-0.61157100, 1.81216600, 8.46131600]),
qatom(atom.H, [-0.09455000, 0.25752800, 8.74727200]),
qatom(atom.H, [3.62176398, -2.70820005, -1.01314598]),
qatom(atom.H, [1.99321055, -4.16506082, -1.01538717]),
qatom(atom.H, [-0.43617817, -4.59691267, -1.01203770]),
qatom(atom.H, [-2.47237881, -3.80553494, -1.01027281]),
qatom(atom.H, [-3.99898497, -1.89601160, -1.01248397]),
qatom(atom.H, [-4.38592989, 0.25190373, -1.01261011]),
qatom(atom.H, [-3.61153849, 2.57615785, -1.01295869]),
qatom(atom.H, [-1.97839416, 4.02973792, -1.00178451]),
qatom(atom.H, [0.44313315, 4.47330208, -0.99064511]),
qatom(atom.H, [2.47734323, 3.67168279, -0.98816699]),
qatom(atom.H, [3.99533580, 1.76469987, -0.99566814]),
qatom(atom.H, [4.39156801, -0.38180889, -1.00738556]),
qatom(atom.H, [-4.00110728, -1.88970494, 12.94740004]),
qatom(atom.H, [-4.43776531, 0.24549797, 12.94970505]),
qatom(atom.H, [-3.68550252, 2.58374056, 12.95344686]),
qatom(atom.H, [-2.03900629, 4.01828867, 12.96136354]),
qatom(atom.H, [0.40279565, 4.40067113, 12.97134886]),
qatom(atom.H, [2.42510303, 3.58373845, 12.96962366]),
qatom(atom.H, [3.99514740, 1.70644846, 12.96646873]),
qatom(atom.H, [4.42617164, -0.43130685, 12.95297873]),
qatom(atom.H, [3.65964816, -2.76660452, 12.94714769]),
qatom(atom.H, [2.01319124, -4.20108001, 12.94623465]),
qatom(atom.H, [-0.42796873, -4.59185222, 12.94787537]),
qatom(atom.H, [-2.45808716, -3.79097127, 12.95284141]),
]
qmolecule_RI_JK = molecule(acene, charge=0, mult=1, sym=sym.C1) # hojokitei in icmr module
casscf.no4c_RI_JK = True
hint.use_RI_JK = True
hint.itrf_RI_JK_memory = 2000
hint.trafo_algo = "RI-SemiDirect-Disk"

benzene = [ i.new_basis() for i in geom]
qmolecule_RI_C = molecule(benzene, charge=0, mult=1, sym=sym.C1) # hojokitei in lct module

qmolecule_RI_C = qmolecule_RI_JK

scf.maxloop = 300
scf.tol_density = 1e-4
scf.orb_print = 'all'
#scf.guess = "moread"

# orb info bgn ------------
# orig frozen ... 139.00
# orig closed ... 287.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [426]
casscf.occ = [0]
casscf.roots = {1.0:1}

casscf.maxMacroloop = 100
casscf.tolMacroloop = 1e-5

prop.dipmom = True

casscf.citype = "fullci"
casscf.CI_restartGrad = casscf.tolMacroloop
casscf.CI_onedotGrad = casscf.tolMacroloop

casscf.debugkeys=["canonical"]

# ICMR
icmr.orbconfig = "symlist"
icmr.frozen = [139]
icmr.closed = [287]
icmr.occ = [0]
icmr.roots  = {1.0:1}
icmr.citype = casscf.citype

icmr.localize_type = casscf.localize_type
icmr.use_3RDM = True # kept True
icmr.use_4RDM = True
icmr.use_d4cum_of = False # ???
icmr.ampAllocType = 2 # 1=disk, 2=GA
icmr.icb_type = -2 # 0=MS-MR, 1=MS-SR, 2=SS-SR
icmr.xms_type = 0 # 0=Non-XMS, 1=XMS
icmr.pt.ipeashift = 0
icmr.pt.lvl_shift = 0.0 # level shift (<0 imaginary level shift)
icmr.pt.toliter = 1e-8
icmr.pt.tolOrthExternal = 1e-8
icmr.pt.tolOrthInternal = 1e-8

icmr.method = "caspt2"


# LCT
lct.Ansatz = "PNO-CASPT2"
lct.DoLoc       = True
lct.DoCEPT2     = True
lct.NewTrafo    = True
lct.Make4EXT    = False

lct.TCutPNOrho0 = 1e-8
lct.TCutPNOrho1 = 1e-8
lct.TCutPNOrho2 = 1e-8
lct.TCutPairs   = 1e-5
lct.TCutPre     = 1e-6

lct.MaxIter = 50

lct.DoCEPT2     = False
lct.NNewTrafo   = True
lct.NewTrafo    = (not lct.NNewTrafo)
lct.TrafoMode   = "Disk"
lct.NewAlgoPNO  = True
lct.OVLMode     = lct.TrafoMode

# Use of Local PAO/PNO
lct.UsePAOs = False
lct.UseNaiveMapPAOs = False
lct.DomScheme = 'Scheme1'
lct.TCutDOI = 1e-3
lct.TCutDOI_Active = 5e-3
lct.TCutDOI_PAO = 1e-2
lct.UseNewDomain = True
lct.FormLVOs = True
lct.UseVM1_CD   = True
lct.UseVM12     = (not lct.UseVM1_CD)
# Crude screening
lct.DoTwoStepGuess = True
lct.TCutPairs_Crude = 5e-6
lct.TCutDOI_PAO_Crude = 1e-1
lct.TCutDOI_Crude = 1e-2


lct.PrintPairDistDBG = True
lct.PrintMapsDBG     = True

lct.LocMet = "PSM"
lct.LocRecursive = True
lct.LocMeasure = True
hint.nroots = 1
hint.nconvroots = 1

# new PMNR scheme threshold (impl = sparse, locrec = True)
lct.PMMaxIt = 20
lct.PMStep = 0.1
lct.GThresh = 5.0e-3
lct.IterLevel = 2
#hint.PM_nontrunc_incore = False
hint.PM_trunc_thresh = 1e-1
hint.PM_AB_thresh = 5e-2
hint.PM_ang_thresh = 5e-4
hint.ChargeType = "Loewdin"
hint.ImplTypePM = "sparse"
# ---------------------------------------

hint.PSMVersion = 2
lct.LocPower = 1

hint.jacobi_thresh     = 1e-6 # Convergence threshold for Jacobi rotations
hint.loc_thresh        = 1e-6 # Convergence thrshold for grad norm
hint.cg_thresh         = 1e-6 # Convergence threshold for preconditioned conjugate gradient(=PCG) iterations
hint.res_tol           = 1e-6
hint.kscal = 5e-3
hint.print_dvd  = True
hint.stepThresh = 0.5
hint.maximize_niter = 1000
hint.nmicroiter     = 1000

# # No Domain
lct.DomScheme = 'Scheme1'

##
lct.StackSize = 50000000
# old option
#lct.test        = False
#lct.DoPNO       = True
#lct.UseOrthPNOs = True
#lct.RIMP2 = False 
#hint.isOnTheFly = True
#hint.PMNRdebug = "no-debug"

# add option

