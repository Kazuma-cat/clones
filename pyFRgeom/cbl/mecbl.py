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
qatom(atom.Co, [0.0, 0.0, 0.0]),
qatom(atom.N, [0.4836255999999963, 0.5960138999999955, 1.7100990000000005]),
qatom(atom.N, [0.42402299999999116, 1.7424594999999954, -0.7394483999999997]),
qatom(atom.N, [-0.6002676000000093, -0.7897720000000064, -1.6500312]),
qatom(atom.N, [-0.16466739999999902, -1.6524801000000053, 0.8743436000000004]),
qatom(atom.C, [0.21272150000000067, -0.32824850000000083, 2.857700500000001]),
qatom(atom.C, [-1.2527395000000041, -0.22895860000000567, 3.300834900000001]),
qatom(atom.C, [1.2287073999999905, 0.185005799999999, 3.951520600000001]),
qatom(atom.C, [0.7673453000000023, -0.06492880000000412, 5.3867135]),
qatom(atom.C, [2.6246544999999912, -0.4639948000000018, 3.712369]),
qatom(atom.C, [3.7610469999999907, 0.21349359999999962, 4.466987800000001]),
qatom(atom.O, [3.846747499999992, 0.20924239999999372, 5.701807700000001]),
qatom(atom.C, [1.3635056999999904, 1.693881299999994, 3.5773564]),
qatom(atom.C, [0.4079385000000002, 2.7082817999999946, 4.2499139]),
qatom(atom.C, [0.9562687999999895, 3.270198899999997, 5.563013600000001]),
qatom(atom.C, [-0.039106700000004935, 4.217461799999995, 6.221738900000001]),
qatom(atom.O, [-1.2624572, 4.0284196999999935, 6.1654176000000005]),
qatom(atom.C, [1.1393314999999973, 1.6639419999999987, 2.081105700000001]),
qatom(atom.C, [1.559200599999997, 2.7147900999999948, 1.1995158000000012]),
qatom(atom.C, [2.43981389999999, 3.7929592999999997, 1.7988312000000013]),
qatom(atom.C, [1.1684556999999955, 2.7385744999999986, -0.12545299999999937]),
qatom(atom.C, [1.5562796999999904, 3.808001499999996, -1.1592037999999993]),
qatom(atom.C, [1.4235791999999918, 5.272113399999995, -0.7162459999999999]),
qatom(atom.C, [3.0302784000000003, 3.475865199999994, -1.5788285999999996]),
qatom(atom.C, [3.590041599999992, 4.466409399999996, -2.5906550999999993]),
qatom(atom.O, [3.2152711999999894, 4.488852699999995, -3.7730863999999995]),
qatom(atom.C, [0.6342724000000004, 3.4566620999999955, -2.3663964999999996]),
qatom(atom.C, [-0.5953886000000068, 4.354272199999997, -2.648556599999999]),
qatom(atom.C, [-1.7197229000000078, 4.233963699999997, -1.6265498999999997]),
qatom(atom.C, [-2.965639500000009, 5.0170862999999954, -2.0189908999999995]),
qatom(atom.O, [-3.034878000000006, 5.699983899999999, -3.0503038999999994]),
qatom(atom.C, [0.2109425000000016, 2.0540248999999946, -2.0382409999999993]),
qatom(atom.C, [-0.3439493999999996, 1.2157518999999937, -2.9873699]),
qatom(atom.C, [-0.7011202000000054, -0.11345530000000537, -2.8091571999999996]),
qatom(atom.C, [-1.2281413000000043, -0.9584280000000049, -3.9528238999999994]),
qatom(atom.C, [-0.15494980000001135, -1.1072332000000031, -5.0515794]),
qatom(atom.C, [-2.471555600000002, -0.2713857000000033, -4.5473251]),
qatom(atom.C, [-1.4741170000000068, -2.334207500000005, -3.2543504]),
qatom(atom.C, [-2.9187962000000027, -2.8961698000000027, -3.2675633999999993]),
qatom(atom.C, [-3.183337200000011, -3.994421800000005, -4.315626999999999]),
qatom(atom.C, [-3.281260000000003, -3.4861912000000004, -5.7439896]),
qatom(atom.O, [-2.3928742000000085, -3.6975544000000014, -6.5884491999999995]),
qatom(atom.C, [-0.9678151000000099, -2.1122648000000055, -1.8365732999999995]),
qatom(atom.C, [-0.886294300000003, -3.1205529, -0.8988620999999997]),
qatom(atom.C, [-1.1788324000000046, -4.5420625, -1.3320311999999994]),
qatom(atom.C, [-0.4723538000000076, -2.854226000000004, 0.4479527000000001]),
qatom(atom.C, [-0.2261304000000024, -3.9033125999999996, 1.5404518999999999]),
qatom(atom.C, [1.1239807999999982, -4.596183800000006, 1.2486670000000002]),
qatom(atom.C, [-1.3368241000000012, -4.951819100000002, 1.7456170000000002]),
qatom(atom.C, [-2.7380672999999973, -4.354600100000006, 1.7528170000000012]),
qatom(atom.C, [-3.8237223, -5.378190100000005, 2.0481120000000006]),
qatom(atom.O, [-3.5901132000000047, -6.577263200000004, 2.2670849000000013]),
qatom(atom.C, [-0.13317640000001063, -2.9901735000000045, 2.803569800000001]),
qatom(atom.C, [0.5679075999999981, -3.640804000000003, 3.996137100000001]),
qatom(atom.C, [-0.17868010000000822, -3.447068800000004, 5.315263500000001]),
qatom(atom.O, [-1.3800676000000038, -3.1535589, 5.3625675]),
qatom(atom.C, [0.4604836999999975, -1.708351300000004, 2.2223782000000005]),
qatom(atom.C, [-6.2625467000000015, -5.688462300000005, 2.0892845000000007]),
qatom(atom.C, [-6.5648265000000094, -6.276024100000001, 0.7102469000000005]),
qatom(atom.C, [-7.803009400000008, -7.157126099999999, 0.7141807000000009]),
qatom(atom.O, [-6.803789500000008, -5.183065300000003, -0.2283861999999992]),
qatom(atom.O, [-6.436272200000005, -4.442318500000006, -2.5715845999999996]),
qatom(atom.O, [-4.458521900000008, -5.564456300000003, -1.2624012999999996]),
qatom(atom.P, [-5.671238400000007, -4.6953344, -1.2882907999999995]),
qatom(atom.O, [-5.190424300000004, -3.234955300000003, -0.6965914]),
qatom(atom.C, [-6.128264900000005, -2.1573352000000057, -0.6763892]),
qatom(atom.C, [-6.049164900000008, -1.3710945000000052, 0.6702891000000006]),
qatom(atom.O, [-5.092686900000004, -1.9474704000000003, 1.551061400000001]),
qatom(atom.C, [-5.729225800000009, 0.08555499999999938, 0.24449640000000006]),
qatom(atom.O, [-6.1180240000000055, 0.1709360999999987, -1.1157594999999993]),
qatom(atom.C, [-5.824153700000011, -1.0960329000000044, -1.7536781999999995]),
qatom(atom.C, [-6.659949100000006, -1.1493334000000033, -3.0314498]),
qatom(atom.O, [-6.277902400000002, -2.2214276000000055, -3.8871242999999995]),
qatom(atom.N, [-4.3364282, 0.48952500000000043, 0.4540804000000005]),
qatom(atom.C, [-3.9748413000000085, 1.718316299999998, 1.0064117000000001]),
qatom(atom.C, [-3.1671089000000023, -0.13472520000000543, 0.0859646000000005]),
qatom(atom.N, [-2.0945893000000098, 0.5994516999999959, 0.3410346000000004]),
qatom(atom.C, [-2.5704905000000053, 1.7759106999999972, 0.9308870000000011]),
qatom(atom.C, [-1.9043721999999974, 2.8981119999999976, 1.429254300000001]),
qatom(atom.C, [-2.6387371, 3.934280699999995, 2.0008308]),
qatom(atom.C, [-1.9206014000000096, 5.149187699999999, 2.532859600000001]),
qatom(atom.C, [-4.0594422000000066, 3.8555733999999973, 2.0838574999999997]),
qatom(atom.C, [-4.8431685999999985, 4.977881399999994, 2.716105100000001]),
qatom(atom.C, [-4.733195899999998, 2.744585899999997, 1.5724155000000009]),
qatom(atom.C, [1.859710899999996, -0.4795408000000023, -0.4471097999999998]),
qatom(atom.H, [-1.4190994000000074, -0.839460300000006, 4.191032900000001]),
qatom(atom.H, [-1.5374301000000088, 0.8021247999999943, 3.5135408000000004]),
qatom(atom.H, [-1.897256100000007, -0.6009859000000048, 2.502849800000001]),
qatom(atom.H, [1.5386003999999929, 0.26146190000000047, 6.086874300000001]),
qatom(atom.H, [0.6025822000000005, -1.1302819, 5.5598912]),
qatom(atom.H, [-0.16472840000000133, 0.45884399999999914, 5.609713700000001]),
qatom(atom.H, [2.605301499999996, -1.5081360000000004, 4.037283100000001]),
qatom(atom.H, [2.8528613999999948, -0.4513061000000036, 2.6418106999999997]),
qatom(atom.H, [2.3814146999999934, 2.029157599999998, 3.7944138]),
qatom(atom.H, [-0.5776267000000104, 2.273945299999994, 4.422471600000001]),
qatom(atom.H, [0.25116549999999904, 3.5415299000000005, 3.5583055999999997]),
qatom(atom.H, [1.1486392999999993, 2.4616377999999983, 6.277716300000001]),
qatom(atom.H, [1.9131536000000011, 3.7767476999999943, 5.3948834]),
qatom(atom.H, [3.059008800000001, 3.3816188999999994, 2.5987216]),
qatom(atom.H, [1.862768399999993, 4.622000699999994, 2.2258672000000006]),
qatom(atom.H, [3.1237203999999963, 4.217502399999994, 1.0661002000000002]),
qatom(atom.H, [0.4658896999999911, 5.454621699999997, -0.22223879999999951]),
qatom(atom.H, [2.2159547999999916, 5.5793368, -0.03483809999999998]),
qatom(atom.H, [1.4802559999999971, 5.922954799999999, -1.5935420999999996]),
qatom(atom.H, [3.6681174, 3.4423084999999958, -0.6921792999999994]),
qatom(atom.H, [3.0434134999999998, 2.481870299999997, -2.0368483999999993]),
qatom(atom.H, [1.2355214999999902, 3.470499999999994, -3.279375999999999]),
qatom(atom.H, [-0.2738579000000101, 5.394923199999994, -2.7438760999999996]),
qatom(atom.H, [-0.98543260000001, 4.066364799999995, -3.6303756999999997]),
qatom(atom.H, [-1.4043624000000108, 4.574535699999998, -0.6347629999999995]),
qatom(atom.H, [-2.005704899999998, 3.1828212999999934, -1.4986813999999997]),
qatom(atom.H, [-0.4553125000000051, 1.626132399999996, -3.9852587999999995]),
qatom(atom.H, [0.7645607999999982, -1.5351274000000004, -4.638585599999999]),
qatom(atom.H, [-0.5290788000000077, -1.7738647000000043, -5.835475799999999]),
qatom(atom.H, [0.08415379999999573, -0.13767720000000594, -5.4999784]),
qatom(atom.H, [-3.224252100000001, -0.05788380000000615, -3.7818871999999994]),
qatom(atom.H, [-2.9283389, -0.8889474000000064, -5.323439499999999]),
qatom(atom.H, [-2.180016100000003, 0.6804971999999978, -5.0009067]),
qatom(atom.H, [-0.8253990999999985, -3.078628100000003, -3.7321659999999994]),
qatom(atom.H, [-3.147583300000008, -3.3258699000000007, -2.2916507999999993]),
qatom(atom.H, [-3.636378300000004, -2.0880843000000056, -3.4139858]),
qatom(atom.H, [-2.38726410000001, -4.742936100000001, -4.284653499999999]),
qatom(atom.H, [-4.1245428, -4.4852852, -4.0460121]),
qatom(atom.H, [-0.4865691000000112, -5.2415114, -0.8617134999999996]),
qatom(atom.H, [-2.1999495000000024, -4.865483000000005, -1.0966571999999992]),
qatom(atom.H, [-1.0460689000000087, -4.6461738, -2.4106639999999997]),
qatom(atom.H, [1.3459993999999966, -5.338374200000004, 2.0217800000000006]),
qatom(atom.H, [1.9459449000000006, -3.873494700000002, 1.2183165000000011]),
qatom(atom.H, [1.0986487999999923, -5.116307200000001, 0.2884094000000008]),
qatom(atom.H, [-1.1447166000000095, -5.445499700000006, 2.7065361]),
qatom(atom.H, [-1.2742866000000106, -5.738294700000004, 0.9912876000000006]),
qatom(atom.H, [-2.820320300000006, -3.5551464000000053, 2.497722200000001]),
qatom(atom.H, [-2.977800700000003, -3.8944494000000063, 0.7875445000000001]),
qatom(atom.H, [-1.1567318000000029, -2.7701423000000034, 3.1187549]),
qatom(atom.H, [1.6118507999999991, -3.3289986999999996, 4.098630900000001]),
qatom(atom.H, [0.6012247999999971, -4.728789000000006, 3.8536951000000004]),
qatom(atom.H, [1.5363968999999997, -1.8328954000000053, 2.056108600000001]),
qatom(atom.H, [-7.105435200000002, -5.079251900000003, 2.429699200000001]),
qatom(atom.H, [-6.109234700000002, -6.5051226, 2.8005588]),
qatom(atom.H, [-5.687192400000001, -6.826417200000002, 0.3597633]),
qatom(atom.H, [-8.6821068, -6.585791500000006, 1.0319721]),
qatom(atom.H, [-7.987757000000002, -7.558164099999999, -0.2864379999999995]),
qatom(atom.H, [-7.663979800000007, -7.995406200000005, 1.4052376000000004]),
qatom(atom.H, [-7.143846600000003, -2.5422742000000014, -0.8038361999999992]),
qatom(atom.H, [-7.035125800000003, -1.3638958000000017, 1.1402893]),
qatom(atom.H, [-5.2519352000000055, -1.5821381000000017, 2.437390700000001]),
qatom(atom.H, [-6.329112199999997, 0.8099206999999993, 0.7919471000000007]),
qatom(atom.H, [-4.7574769, -1.1454616000000044, -2.008103899999999]),
qatom(atom.H, [-7.723851300000007, -1.2187474000000051, -2.7603523999999995]),
qatom(atom.H, [-6.506868400000002, -0.21927450000000448, -3.5873182999999997]),
qatom(atom.H, [-6.351686600000008, -3.0911006000000043, -3.3732556999999996]),
qatom(atom.H, [-3.1464612999999986, -1.1301243999999997, -0.33305399999999974]),
qatom(atom.H, [-0.8279485999999991, 2.978634999999997, 1.3617245000000002]),
qatom(atom.H, [-2.3643975000000097, 6.0766025, 2.1542752]),
qatom(atom.H, [-1.9667433999999986, 5.186745799999997, 3.628250800000001]),
qatom(atom.H, [-0.8668084000000107, 5.1337323999999995, 2.2407159000000005]),
qatom(atom.H, [-4.498684800000007, 5.171475099999995, 3.738699900000001]),
qatom(atom.H, [-5.908565899999999, 4.737438299999994, 2.7496641000000013]),
qatom(atom.H, [-4.719805100000002, 5.913951399999995, 2.1571597000000002]),
qatom(atom.H, [-5.816285800000003, 2.6942022999999935, 1.631323300000001]),
qatom(atom.H, [2.5321792999999957, 0.07555289999999815, 0.21405840000000076]),
qatom(atom.H, [2.005473099999989, -1.556912600000004, -0.33290679999999995]),
qatom(atom.H, [-4.868566800000011, 5.392577299999999, -1.3461334999999996]),
qatom(atom.H, [-3.937648600000003, 4.348916799999998, -0.31117989999999995]),
qatom(atom.H, [-0.09170819999999935, 5.903140999999998, 7.395558800000001]),
qatom(atom.H, [1.5040446999999944, 5.403900099999994, 6.929723400000001]),
qatom(atom.H, [5.488272999999992, 1.269221299999998, 4.1105998]),
qatom(atom.H, [4.662873099999999, 0.7528920999999968, 2.6798168]),
qatom(atom.H, [0.12956419999999014, -3.624057200000003, 7.338353800000001]),
qatom(atom.H, [1.5370245999999952, -3.9257584000000065, 6.3705381]),
qatom(atom.H, [4.835979499999993, 5.2892704999999935, -1.1543238999999996]),
qatom(atom.H, [4.91895439999999, 6.0261309999999995, -2.7213648]),
qatom(atom.H, [-5.080055200000004, -2.5372588000000036, -5.302566]),
qatom(atom.H, [-4.502792800000009, -2.374908900000001, -6.949397899999999]),
qatom(atom.H, [-5.168583600000005, -3.885323100000001, 1.7600722000000006]),
qatom(atom.N, [4.508258900000001, 5.3315731, -2.1089972999999995]),
qatom(atom.N, [0.5043151999999935, 5.261037099999996, 6.887644800000001]),
qatom(atom.N, [0.5623695999999967, -3.662928200000003, 6.4239959]),
qatom(atom.N, [-5.071728300000004, -4.854335000000006, 2.068473]),
qatom(atom.N, [-4.406319699999997, -2.7936243000000047, -6.0321833]),
qatom(atom.N, [4.672151299999996, 0.844596199999998, 3.6860430000000006]),
qatom(atom.N, [-4.000871900000007, 4.907850199999999, -1.1547033999999998]),
qatom(atom.H, [2.0281718999999896, -0.18737320000000324, -1.4871809999999996]),
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
qatom(atom.Co, [0.0, 0.0, 0.0]),
qatom(atom.N, [0.4836255999999963, 0.5960138999999955, 1.7100990000000005]),
qatom(atom.N, [0.42402299999999116, 1.7424594999999954, -0.7394483999999997]),
qatom(atom.N, [-0.6002676000000093, -0.7897720000000064, -1.6500312]),
qatom(atom.N, [-0.16466739999999902, -1.6524801000000053, 0.8743436000000004]),
qatom(atom.C, [0.21272150000000067, -0.32824850000000083, 2.857700500000001]),
qatom(atom.C, [-1.2527395000000041, -0.22895860000000567, 3.300834900000001]),
qatom(atom.C, [1.2287073999999905, 0.185005799999999, 3.951520600000001]),
qatom(atom.C, [0.7673453000000023, -0.06492880000000412, 5.3867135]),
qatom(atom.C, [2.6246544999999912, -0.4639948000000018, 3.712369]),
qatom(atom.C, [3.7610469999999907, 0.21349359999999962, 4.466987800000001]),
qatom(atom.O, [3.846747499999992, 0.20924239999999372, 5.701807700000001]),
qatom(atom.C, [1.3635056999999904, 1.693881299999994, 3.5773564]),
qatom(atom.C, [0.4079385000000002, 2.7082817999999946, 4.2499139]),
qatom(atom.C, [0.9562687999999895, 3.270198899999997, 5.563013600000001]),
qatom(atom.C, [-0.039106700000004935, 4.217461799999995, 6.221738900000001]),
qatom(atom.O, [-1.2624572, 4.0284196999999935, 6.1654176000000005]),
qatom(atom.C, [1.1393314999999973, 1.6639419999999987, 2.081105700000001]),
qatom(atom.C, [1.559200599999997, 2.7147900999999948, 1.1995158000000012]),
qatom(atom.C, [2.43981389999999, 3.7929592999999997, 1.7988312000000013]),
qatom(atom.C, [1.1684556999999955, 2.7385744999999986, -0.12545299999999937]),
qatom(atom.C, [1.5562796999999904, 3.808001499999996, -1.1592037999999993]),
qatom(atom.C, [1.4235791999999918, 5.272113399999995, -0.7162459999999999]),
qatom(atom.C, [3.0302784000000003, 3.475865199999994, -1.5788285999999996]),
qatom(atom.C, [3.590041599999992, 4.466409399999996, -2.5906550999999993]),
qatom(atom.O, [3.2152711999999894, 4.488852699999995, -3.7730863999999995]),
qatom(atom.C, [0.6342724000000004, 3.4566620999999955, -2.3663964999999996]),
qatom(atom.C, [-0.5953886000000068, 4.354272199999997, -2.648556599999999]),
qatom(atom.C, [-1.7197229000000078, 4.233963699999997, -1.6265498999999997]),
qatom(atom.C, [-2.965639500000009, 5.0170862999999954, -2.0189908999999995]),
qatom(atom.O, [-3.034878000000006, 5.699983899999999, -3.0503038999999994]),
qatom(atom.C, [0.2109425000000016, 2.0540248999999946, -2.0382409999999993]),
qatom(atom.C, [-0.3439493999999996, 1.2157518999999937, -2.9873699]),
qatom(atom.C, [-0.7011202000000054, -0.11345530000000537, -2.8091571999999996]),
qatom(atom.C, [-1.2281413000000043, -0.9584280000000049, -3.9528238999999994]),
qatom(atom.C, [-0.15494980000001135, -1.1072332000000031, -5.0515794]),
qatom(atom.C, [-2.471555600000002, -0.2713857000000033, -4.5473251]),
qatom(atom.C, [-1.4741170000000068, -2.334207500000005, -3.2543504]),
qatom(atom.C, [-2.9187962000000027, -2.8961698000000027, -3.2675633999999993]),
qatom(atom.C, [-3.183337200000011, -3.994421800000005, -4.315626999999999]),
qatom(atom.C, [-3.281260000000003, -3.4861912000000004, -5.7439896]),
qatom(atom.O, [-2.3928742000000085, -3.6975544000000014, -6.5884491999999995]),
qatom(atom.C, [-0.9678151000000099, -2.1122648000000055, -1.8365732999999995]),
qatom(atom.C, [-0.886294300000003, -3.1205529, -0.8988620999999997]),
qatom(atom.C, [-1.1788324000000046, -4.5420625, -1.3320311999999994]),
qatom(atom.C, [-0.4723538000000076, -2.854226000000004, 0.4479527000000001]),
qatom(atom.C, [-0.2261304000000024, -3.9033125999999996, 1.5404518999999999]),
qatom(atom.C, [1.1239807999999982, -4.596183800000006, 1.2486670000000002]),
qatom(atom.C, [-1.3368241000000012, -4.951819100000002, 1.7456170000000002]),
qatom(atom.C, [-2.7380672999999973, -4.354600100000006, 1.7528170000000012]),
qatom(atom.C, [-3.8237223, -5.378190100000005, 2.0481120000000006]),
qatom(atom.O, [-3.5901132000000047, -6.577263200000004, 2.2670849000000013]),
qatom(atom.C, [-0.13317640000001063, -2.9901735000000045, 2.803569800000001]),
qatom(atom.C, [0.5679075999999981, -3.640804000000003, 3.996137100000001]),
qatom(atom.C, [-0.17868010000000822, -3.447068800000004, 5.315263500000001]),
qatom(atom.O, [-1.3800676000000038, -3.1535589, 5.3625675]),
qatom(atom.C, [0.4604836999999975, -1.708351300000004, 2.2223782000000005]),
qatom(atom.C, [-6.2625467000000015, -5.688462300000005, 2.0892845000000007]),
qatom(atom.C, [-6.5648265000000094, -6.276024100000001, 0.7102469000000005]),
qatom(atom.C, [-7.803009400000008, -7.157126099999999, 0.7141807000000009]),
qatom(atom.O, [-6.803789500000008, -5.183065300000003, -0.2283861999999992]),
qatom(atom.O, [-6.436272200000005, -4.442318500000006, -2.5715845999999996]),
qatom(atom.O, [-4.458521900000008, -5.564456300000003, -1.2624012999999996]),
qatom(atom.P, [-5.671238400000007, -4.6953344, -1.2882907999999995]),
qatom(atom.O, [-5.190424300000004, -3.234955300000003, -0.6965914]),
qatom(atom.C, [-6.128264900000005, -2.1573352000000057, -0.6763892]),
qatom(atom.C, [-6.049164900000008, -1.3710945000000052, 0.6702891000000006]),
qatom(atom.O, [-5.092686900000004, -1.9474704000000003, 1.551061400000001]),
qatom(atom.C, [-5.729225800000009, 0.08555499999999938, 0.24449640000000006]),
qatom(atom.O, [-6.1180240000000055, 0.1709360999999987, -1.1157594999999993]),
qatom(atom.C, [-5.824153700000011, -1.0960329000000044, -1.7536781999999995]),
qatom(atom.C, [-6.659949100000006, -1.1493334000000033, -3.0314498]),
qatom(atom.O, [-6.277902400000002, -2.2214276000000055, -3.8871242999999995]),
qatom(atom.N, [-4.3364282, 0.48952500000000043, 0.4540804000000005]),
qatom(atom.C, [-3.9748413000000085, 1.718316299999998, 1.0064117000000001]),
qatom(atom.C, [-3.1671089000000023, -0.13472520000000543, 0.0859646000000005]),
qatom(atom.N, [-2.0945893000000098, 0.5994516999999959, 0.3410346000000004]),
qatom(atom.C, [-2.5704905000000053, 1.7759106999999972, 0.9308870000000011]),
qatom(atom.C, [-1.9043721999999974, 2.8981119999999976, 1.429254300000001]),
qatom(atom.C, [-2.6387371, 3.934280699999995, 2.0008308]),
qatom(atom.C, [-1.9206014000000096, 5.149187699999999, 2.532859600000001]),
qatom(atom.C, [-4.0594422000000066, 3.8555733999999973, 2.0838574999999997]),
qatom(atom.C, [-4.8431685999999985, 4.977881399999994, 2.716105100000001]),
qatom(atom.C, [-4.733195899999998, 2.744585899999997, 1.5724155000000009]),
qatom(atom.C, [1.859710899999996, -0.4795408000000023, -0.4471097999999998]),
qatom(atom.H, [-1.4190994000000074, -0.839460300000006, 4.191032900000001]),
qatom(atom.H, [-1.5374301000000088, 0.8021247999999943, 3.5135408000000004]),
qatom(atom.H, [-1.897256100000007, -0.6009859000000048, 2.502849800000001]),
qatom(atom.H, [1.5386003999999929, 0.26146190000000047, 6.086874300000001]),
qatom(atom.H, [0.6025822000000005, -1.1302819, 5.5598912]),
qatom(atom.H, [-0.16472840000000133, 0.45884399999999914, 5.609713700000001]),
qatom(atom.H, [2.605301499999996, -1.5081360000000004, 4.037283100000001]),
qatom(atom.H, [2.8528613999999948, -0.4513061000000036, 2.6418106999999997]),
qatom(atom.H, [2.3814146999999934, 2.029157599999998, 3.7944138]),
qatom(atom.H, [-0.5776267000000104, 2.273945299999994, 4.422471600000001]),
qatom(atom.H, [0.25116549999999904, 3.5415299000000005, 3.5583055999999997]),
qatom(atom.H, [1.1486392999999993, 2.4616377999999983, 6.277716300000001]),
qatom(atom.H, [1.9131536000000011, 3.7767476999999943, 5.3948834]),
qatom(atom.H, [3.059008800000001, 3.3816188999999994, 2.5987216]),
qatom(atom.H, [1.862768399999993, 4.622000699999994, 2.2258672000000006]),
qatom(atom.H, [3.1237203999999963, 4.217502399999994, 1.0661002000000002]),
qatom(atom.H, [0.4658896999999911, 5.454621699999997, -0.22223879999999951]),
qatom(atom.H, [2.2159547999999916, 5.5793368, -0.03483809999999998]),
qatom(atom.H, [1.4802559999999971, 5.922954799999999, -1.5935420999999996]),
qatom(atom.H, [3.6681174, 3.4423084999999958, -0.6921792999999994]),
qatom(atom.H, [3.0434134999999998, 2.481870299999997, -2.0368483999999993]),
qatom(atom.H, [1.2355214999999902, 3.470499999999994, -3.279375999999999]),
qatom(atom.H, [-0.2738579000000101, 5.394923199999994, -2.7438760999999996]),
qatom(atom.H, [-0.98543260000001, 4.066364799999995, -3.6303756999999997]),
qatom(atom.H, [-1.4043624000000108, 4.574535699999998, -0.6347629999999995]),
qatom(atom.H, [-2.005704899999998, 3.1828212999999934, -1.4986813999999997]),
qatom(atom.H, [-0.4553125000000051, 1.626132399999996, -3.9852587999999995]),
qatom(atom.H, [0.7645607999999982, -1.5351274000000004, -4.638585599999999]),
qatom(atom.H, [-0.5290788000000077, -1.7738647000000043, -5.835475799999999]),
qatom(atom.H, [0.08415379999999573, -0.13767720000000594, -5.4999784]),
qatom(atom.H, [-3.224252100000001, -0.05788380000000615, -3.7818871999999994]),
qatom(atom.H, [-2.9283389, -0.8889474000000064, -5.323439499999999]),
qatom(atom.H, [-2.180016100000003, 0.6804971999999978, -5.0009067]),
qatom(atom.H, [-0.8253990999999985, -3.078628100000003, -3.7321659999999994]),
qatom(atom.H, [-3.147583300000008, -3.3258699000000007, -2.2916507999999993]),
qatom(atom.H, [-3.636378300000004, -2.0880843000000056, -3.4139858]),
qatom(atom.H, [-2.38726410000001, -4.742936100000001, -4.284653499999999]),
qatom(atom.H, [-4.1245428, -4.4852852, -4.0460121]),
qatom(atom.H, [-0.4865691000000112, -5.2415114, -0.8617134999999996]),
qatom(atom.H, [-2.1999495000000024, -4.865483000000005, -1.0966571999999992]),
qatom(atom.H, [-1.0460689000000087, -4.6461738, -2.4106639999999997]),
qatom(atom.H, [1.3459993999999966, -5.338374200000004, 2.0217800000000006]),
qatom(atom.H, [1.9459449000000006, -3.873494700000002, 1.2183165000000011]),
qatom(atom.H, [1.0986487999999923, -5.116307200000001, 0.2884094000000008]),
qatom(atom.H, [-1.1447166000000095, -5.445499700000006, 2.7065361]),
qatom(atom.H, [-1.2742866000000106, -5.738294700000004, 0.9912876000000006]),
qatom(atom.H, [-2.820320300000006, -3.5551464000000053, 2.497722200000001]),
qatom(atom.H, [-2.977800700000003, -3.8944494000000063, 0.7875445000000001]),
qatom(atom.H, [-1.1567318000000029, -2.7701423000000034, 3.1187549]),
qatom(atom.H, [1.6118507999999991, -3.3289986999999996, 4.098630900000001]),
qatom(atom.H, [0.6012247999999971, -4.728789000000006, 3.8536951000000004]),
qatom(atom.H, [1.5363968999999997, -1.8328954000000053, 2.056108600000001]),
qatom(atom.H, [-7.105435200000002, -5.079251900000003, 2.429699200000001]),
qatom(atom.H, [-6.109234700000002, -6.5051226, 2.8005588]),
qatom(atom.H, [-5.687192400000001, -6.826417200000002, 0.3597633]),
qatom(atom.H, [-8.6821068, -6.585791500000006, 1.0319721]),
qatom(atom.H, [-7.987757000000002, -7.558164099999999, -0.2864379999999995]),
qatom(atom.H, [-7.663979800000007, -7.995406200000005, 1.4052376000000004]),
qatom(atom.H, [-7.143846600000003, -2.5422742000000014, -0.8038361999999992]),
qatom(atom.H, [-7.035125800000003, -1.3638958000000017, 1.1402893]),
qatom(atom.H, [-5.2519352000000055, -1.5821381000000017, 2.437390700000001]),
qatom(atom.H, [-6.329112199999997, 0.8099206999999993, 0.7919471000000007]),
qatom(atom.H, [-4.7574769, -1.1454616000000044, -2.008103899999999]),
qatom(atom.H, [-7.723851300000007, -1.2187474000000051, -2.7603523999999995]),
qatom(atom.H, [-6.506868400000002, -0.21927450000000448, -3.5873182999999997]),
qatom(atom.H, [-6.351686600000008, -3.0911006000000043, -3.3732556999999996]),
qatom(atom.H, [-3.1464612999999986, -1.1301243999999997, -0.33305399999999974]),
qatom(atom.H, [-0.8279485999999991, 2.978634999999997, 1.3617245000000002]),
qatom(atom.H, [-2.3643975000000097, 6.0766025, 2.1542752]),
qatom(atom.H, [-1.9667433999999986, 5.186745799999997, 3.628250800000001]),
qatom(atom.H, [-0.8668084000000107, 5.1337323999999995, 2.2407159000000005]),
qatom(atom.H, [-4.498684800000007, 5.171475099999995, 3.738699900000001]),
qatom(atom.H, [-5.908565899999999, 4.737438299999994, 2.7496641000000013]),
qatom(atom.H, [-4.719805100000002, 5.913951399999995, 2.1571597000000002]),
qatom(atom.H, [-5.816285800000003, 2.6942022999999935, 1.631323300000001]),
qatom(atom.H, [2.5321792999999957, 0.07555289999999815, 0.21405840000000076]),
qatom(atom.H, [2.005473099999989, -1.556912600000004, -0.33290679999999995]),
qatom(atom.H, [-4.868566800000011, 5.392577299999999, -1.3461334999999996]),
qatom(atom.H, [-3.937648600000003, 4.348916799999998, -0.31117989999999995]),
qatom(atom.H, [-0.09170819999999935, 5.903140999999998, 7.395558800000001]),
qatom(atom.H, [1.5040446999999944, 5.403900099999994, 6.929723400000001]),
qatom(atom.H, [5.488272999999992, 1.269221299999998, 4.1105998]),
qatom(atom.H, [4.662873099999999, 0.7528920999999968, 2.6798168]),
qatom(atom.H, [0.12956419999999014, -3.624057200000003, 7.338353800000001]),
qatom(atom.H, [1.5370245999999952, -3.9257584000000065, 6.3705381]),
qatom(atom.H, [4.835979499999993, 5.2892704999999935, -1.1543238999999996]),
qatom(atom.H, [4.91895439999999, 6.0261309999999995, -2.7213648]),
qatom(atom.H, [-5.080055200000004, -2.5372588000000036, -5.302566]),
qatom(atom.H, [-4.502792800000009, -2.374908900000001, -6.949397899999999]),
qatom(atom.H, [-5.168583600000005, -3.885323100000001, 1.7600722000000006]),
qatom(atom.N, [4.508258900000001, 5.3315731, -2.1089972999999995]),
qatom(atom.N, [0.5043151999999935, 5.261037099999996, 6.887644800000001]),
qatom(atom.N, [0.5623695999999967, -3.662928200000003, 6.4239959]),
qatom(atom.N, [-5.071728300000004, -4.854335000000006, 2.068473]),
qatom(atom.N, [-4.406319699999997, -2.7936243000000047, -6.0321833]),
qatom(atom.N, [4.672151299999996, 0.844596199999998, 3.6860430000000006]),
qatom(atom.N, [-4.000871900000007, 4.907850199999999, -1.1547033999999998]),
qatom(atom.H, [2.0281718999999896, -0.18737320000000324, -1.4871809999999996]),
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
# orig frozen ... 100.00
# orig closed ... 257.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [357]
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
icmr.frozen = [100]
icmr.closed = [257]
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
#lct.PrintAllEps = False


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

hint.randomize=False
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

