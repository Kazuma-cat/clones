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
qatom(atom.Co, [-0.9156048, 0.0390834, -0.8642740]),
qatom(atom.C, [0.3665174, 1.6903791, 1.0660676]),
qatom(atom.C, [-0.0384760, 2.4624005, 2.3783015]),
qatom(atom.C, [-1.0630251, 1.4797041, 3.0443511]),
qatom(atom.C, [-1.6328711, 0.7592732, 1.8468534]),
qatom(atom.C, [-2.8803257, 0.0526293, 1.8192497]),
qatom(atom.C, [-3.1077783, -0.9036283, 0.8552874]),
qatom(atom.C, [-4.2975111, -1.8664618, 0.7685267]),
qatom(atom.C, [-3.6635935, -3.0128677, -0.0797851]),
qatom(atom.C, [-2.7053166, -2.2274905, -0.9184122]),
qatom(atom.C, [-2.3619738, -2.5404416, -2.2228580]),
qatom(atom.C, [-1.5068514, -1.8012082, -3.0204920]),
qatom(atom.C, [-1.3146628, -2.0277333, -4.5059591]),
qatom(atom.C, [0.0467434, -1.3175307, -4.7337671]),
qatom(atom.C, [0.0791933, -0.3142073, -3.5957140]),
qatom(atom.C, [0.8961095, 0.7980502, -3.5663467]),
qatom(atom.C, [0.9767361, 1.6354745, -2.4074024]),
qatom(atom.C, [1.7628143, 2.9438419, -2.2726263]),
qatom(atom.C, [1.7268775, 3.1724682, -0.7239843]),
qatom(atom.C, [0.4493205, 2.4532805, -0.2836693]),
qatom(atom.C, [1.6218384, 0.8258558, 1.2210557]),
qatom(atom.C, [1.1373862, 2.7947044, 3.3015467]),
qatom(atom.C, [-0.8036806, 3.7617507, 2.0110994]),
qatom(atom.C, [-1.2456256, 4.5495292, 3.2410620]),
qatom(atom.C, [-0.4296178, 0.4823019, 4.0452141]),
qatom(atom.C, [-1.4174497, -0.5143578, 4.6739381]),
qatom(atom.C, [-0.6599214, -1.6191242, 5.3897654]),
qatom(atom.C, [-3.9431317, 0.4422984, 2.8299313]),
qatom(atom.C, [-4.9238221, -2.3632534, 2.0763046]),
qatom(atom.C, [-5.3822613, -1.1431967, -0.0977469]),
qatom(atom.C, [-6.6299787, -1.9975127, -0.3139350]),
qatom(atom.C, [-2.9428304, -4.1194357, 0.7343337]),
qatom(atom.C, [-1.8503792, -3.6906067, 1.7233496]),
qatom(atom.C, [-0.4850295, -3.4089933, 1.1043487]),
qatom(atom.C, [-2.4196029, -1.2163185, -5.2322391]),
qatom(atom.C, [-1.3944384, -3.4888912, -4.9562887]),
qatom(atom.C, [1.2841691, -2.2478517, -4.7103071]),
qatom(atom.C, [1.5431194, -2.9675111, -3.3773526]),
qatom(atom.C, [2.3500051, -2.1418972, -2.3853809]),
qatom(atom.C, [1.7162865, 1.1171240, -4.7991610]),
qatom(atom.C, [0.9754783, 4.0367478, -3.0322276]),
qatom(atom.C, [1.8613134, 4.6579541, -0.3523038]),
qatom(atom.C, [2.4797273, 4.9737219, 1.0034182]),
qatom(atom.C, [3.2371905, 2.9337849, -2.7399280]),
qatom(atom.C, [4.0214001, 1.6399711, -2.5050026]),
qatom(atom.C, [4.5647168, 1.3936498, -1.1025811]),
qatom(atom.C, [5.4915665, -0.3723420, 0.3438270]),
qatom(atom.C, [4.9914001, -1.7235003, 0.8567065]),
qatom(atom.C, [5.8454664, -2.2357298, 2.0104216]),
qatom(atom.N, [-0.8195824, 0.8147177, 0.8209597]),
qatom(atom.N, [-2.2850331, -1.1229302, -0.2508607]),
qatom(atom.N, [-0.7859032, -0.7294625, -2.5929226]),
qatom(atom.N, [0.2829723, 1.3909292, -1.3165220]),
qatom(atom.N, [-0.5447553, 5.6874445, 3.4536290]),
qatom(atom.N, [-0.7544505, -1.6514796, 6.7395263]),
qatom(atom.N, [-7.7878748, -1.4780617, 0.1827468]),
qatom(atom.N, [0.4167470, -2.8507918, 1.9421581]),
qatom(atom.N, [1.9022966, -2.1472008, -1.1171428]),
qatom(atom.N, [3.6793118, 4.4025420, 1.2459088]),
qatom(atom.N, [4.7620496, 0.0860942, -0.8292794]),
qatom(atom.O, [-2.1655355, 4.1654505, 3.9706803]),
qatom(atom.O, [0.0239288, -2.4416460, 4.7676561]),
qatom(atom.O, [-6.5929413, -3.0856840, -0.8819590]),
qatom(atom.O, [-0.2286888, -3.6903342, -0.0769724]),
qatom(atom.O, [3.3793237, -1.5383986, -2.7446481]),
qatom(atom.O, [1.9254714, 5.7309896, 1.8116461]),
qatom(atom.O, [4.8685297, 2.3046686, -0.3110650]),
qatom(atom.O, [3.5933887, -1.6454314, 1.2453991]),
qatom(atom.H, [-1.8165024, 2.0714838, 3.5727974]),
qatom(atom.H, [-4.4331446, -3.4945989, -0.6869441]),
qatom(atom.H, [-2.8302490, -3.4153763, -2.6583485]),
qatom(atom.H, [0.0398767, -0.8121672, -5.7041901]),
qatom(atom.H, [2.5806007, 2.6271060, -0.3178848]),
qatom(atom.H, [-0.4192139, 3.1175909, -0.3594303]),
qatom(atom.H, [2.4928328, 1.4447677, 1.4531184]),
qatom(atom.H, [1.8163042, 0.2900014, 0.2898093]),
qatom(atom.H, [1.4837695, 0.0891964, 2.0140417]),
qatom(atom.H, [1.7142524, 1.9060418, 3.5648837]),
qatom(atom.H, [1.8114296, 3.5175975, 2.8430687]),
qatom(atom.H, [0.7647714, 3.2400763, 4.2291178]),
qatom(atom.H, [-1.7065109, 3.5098231, 1.4433461]),
qatom(atom.H, [-0.1671508, 4.3965124, 1.3923655]),
qatom(atom.H, [0.3529294, -0.0999976, 3.5517856]),
qatom(atom.H, [0.0456637, 1.0577702, 4.8450763]),
qatom(atom.H, [-1.9926792, -1.0067123, 3.8844485]),
qatom(atom.H, [-2.1189581, 0.0006125, 5.3381720]),
qatom(atom.H, [-4.9215616, 0.5041334, 2.3468710]),
qatom(atom.H, [-4.0385180, -0.2533678, 3.6689613]),
qatom(atom.H, [-3.7262959, 1.4305623, 3.2407368]),
qatom(atom.H, [-5.5739419, -1.6128585, 2.5291572]),
qatom(atom.H, [-4.1712378, -2.6516067, 2.8134529]),
qatom(atom.H, [-5.5399638, -3.2412221, 1.8598614]),
qatom(atom.H, [-5.6377302, -0.1899235, 0.3767939]),
qatom(atom.H, [-4.9593675, -0.9224896, -1.0839751]),
qatom(atom.H, [-2.5028394, -4.8210416, 0.0186741]),
qatom(atom.H, [-3.7134795, -4.6676928, 1.2854038]),
qatom(atom.H, [-2.1467417, -2.8178695, 2.3142436]),
qatom(atom.H, [-1.6981339, -4.5005317, 2.4487405]),
qatom(atom.H, [-3.4115532, -1.5938760, -4.9672248]),
qatom(atom.H, [-2.2899726, -1.3063537, -6.3158819]),
qatom(atom.H, [-2.3664117, -0.1565594, -4.9617698]),
qatom(atom.H, [-2.4116631, -3.8711594, -4.8260526]),
qatom(atom.H, [-1.1539594, -3.5646041, -6.0214633]),
qatom(atom.H, [-0.7146679, -4.1392328, -4.4011219]),
qatom(atom.H, [2.1773455, -1.6666568, -4.9580199]),
qatom(atom.H, [1.1569958, -2.9882239, -5.5059456]),
qatom(atom.H, [0.6194941, -3.3176386, -2.9074338]),
qatom(atom.H, [2.1538943, -3.8563159, -3.5785735]),
qatom(atom.H, [2.6979101, 0.6316441, -4.7800540]),
qatom(atom.H, [1.8787625, 2.1893761, -4.9033744]),
qatom(atom.H, [1.2036963, 0.7837795, -5.7034044]),
qatom(atom.H, [-0.0272702, 4.1698266, -2.6134627]),
qatom(atom.H, [1.5000327, 4.9956524, -2.9858479]),
qatom(atom.H, [0.8644494, 3.7697529, -4.0862376]),
qatom(atom.H, [0.8994554, 5.1730484, -0.4006657]),
qatom(atom.H, [2.5166511, 5.1362645, -1.0917678]),
qatom(atom.H, [3.2863331, 3.1730193, -3.8052827]),
qatom(atom.H, [3.7482476, 3.7577391, -2.2248300]),
qatom(atom.H, [4.9136128, 1.6653121, -3.1454194]),
qatom(atom.H, [3.4557199, 0.7582279, -2.8163592]),
qatom(atom.H, [5.3961408, 0.3951185, 1.1205701]),
qatom(atom.H, [6.5619833, -0.4620077, 0.1120318]),
qatom(atom.H, [4.9911340, -2.4523213, 0.0386879]),
qatom(atom.H, [5.4487259, -3.1848191, 2.3787979]),
qatom(atom.H, [6.8796686, -2.3920361, 1.6873025]),
qatom(atom.H, [5.8532478, -1.5153717, 2.8372898]),
qatom(atom.H, [-0.7578490, 6.2423191, 4.2724003]),
qatom(atom.H, [0.2712639, 5.9163309, 2.8865228]),
qatom(atom.H, [-0.2568009, -2.3686796, 7.2518537]),
qatom(atom.H, [-1.3134935, -0.9868467, 7.2538637]),
qatom(atom.H, [-7.8375631, -0.5520369, 0.5804760]),
qatom(atom.H, [-8.6514562, -1.9798049, 0.0184000]),
qatom(atom.H, [0.2178448, -2.7140175, 2.9409476]),
qatom(atom.H, [1.3849857, -2.7870769, 1.6471751]),
qatom(atom.H, [2.4953545, -1.7645308, -0.3797860]),
qatom(atom.H, [1.1251287, -2.7599281, -0.8267405]),
qatom(atom.H, [4.1453710, 3.7679030, 0.5902422]),
qatom(atom.H, [4.1524339, 4.6439258, 2.1070555]),
qatom(atom.H, [4.4212901, -0.5988634, -1.5228228]),
qatom(atom.H, [3.5084057, -0.9214013, 1.8876177]),
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
qatom(atom.Co, [-0.9156048, 0.0390834, -0.8642740]),
qatom(atom.C, [0.3665174, 1.6903791, 1.0660676]),
qatom(atom.C, [-0.0384760, 2.4624005, 2.3783015]),
qatom(atom.C, [-1.0630251, 1.4797041, 3.0443511]),
qatom(atom.C, [-1.6328711, 0.7592732, 1.8468534]),
qatom(atom.C, [-2.8803257, 0.0526293, 1.8192497]),
qatom(atom.C, [-3.1077783, -0.9036283, 0.8552874]),
qatom(atom.C, [-4.2975111, -1.8664618, 0.7685267]),
qatom(atom.C, [-3.6635935, -3.0128677, -0.0797851]),
qatom(atom.C, [-2.7053166, -2.2274905, -0.9184122]),
qatom(atom.C, [-2.3619738, -2.5404416, -2.2228580]),
qatom(atom.C, [-1.5068514, -1.8012082, -3.0204920]),
qatom(atom.C, [-1.3146628, -2.0277333, -4.5059591]),
qatom(atom.C, [0.0467434, -1.3175307, -4.7337671]),
qatom(atom.C, [0.0791933, -0.3142073, -3.5957140]),
qatom(atom.C, [0.8961095, 0.7980502, -3.5663467]),
qatom(atom.C, [0.9767361, 1.6354745, -2.4074024]),
qatom(atom.C, [1.7628143, 2.9438419, -2.2726263]),
qatom(atom.C, [1.7268775, 3.1724682, -0.7239843]),
qatom(atom.C, [0.4493205, 2.4532805, -0.2836693]),
qatom(atom.C, [1.6218384, 0.8258558, 1.2210557]),
qatom(atom.C, [1.1373862, 2.7947044, 3.3015467]),
qatom(atom.C, [-0.8036806, 3.7617507, 2.0110994]),
qatom(atom.C, [-1.2456256, 4.5495292, 3.2410620]),
qatom(atom.C, [-0.4296178, 0.4823019, 4.0452141]),
qatom(atom.C, [-1.4174497, -0.5143578, 4.6739381]),
qatom(atom.C, [-0.6599214, -1.6191242, 5.3897654]),
qatom(atom.C, [-3.9431317, 0.4422984, 2.8299313]),
qatom(atom.C, [-4.9238221, -2.3632534, 2.0763046]),
qatom(atom.C, [-5.3822613, -1.1431967, -0.0977469]),
qatom(atom.C, [-6.6299787, -1.9975127, -0.3139350]),
qatom(atom.C, [-2.9428304, -4.1194357, 0.7343337]),
qatom(atom.C, [-1.8503792, -3.6906067, 1.7233496]),
qatom(atom.C, [-0.4850295, -3.4089933, 1.1043487]),
qatom(atom.C, [-2.4196029, -1.2163185, -5.2322391]),
qatom(atom.C, [-1.3944384, -3.4888912, -4.9562887]),
qatom(atom.C, [1.2841691, -2.2478517, -4.7103071]),
qatom(atom.C, [1.5431194, -2.9675111, -3.3773526]),
qatom(atom.C, [2.3500051, -2.1418972, -2.3853809]),
qatom(atom.C, [1.7162865, 1.1171240, -4.7991610]),
qatom(atom.C, [0.9754783, 4.0367478, -3.0322276]),
qatom(atom.C, [1.8613134, 4.6579541, -0.3523038]),
qatom(atom.C, [2.4797273, 4.9737219, 1.0034182]),
qatom(atom.C, [3.2371905, 2.9337849, -2.7399280]),
qatom(atom.C, [4.0214001, 1.6399711, -2.5050026]),
qatom(atom.C, [4.5647168, 1.3936498, -1.1025811]),
qatom(atom.C, [5.4915665, -0.3723420, 0.3438270]),
qatom(atom.C, [4.9914001, -1.7235003, 0.8567065]),
qatom(atom.C, [5.8454664, -2.2357298, 2.0104216]),
qatom(atom.N, [-0.8195824, 0.8147177, 0.8209597]),
qatom(atom.N, [-2.2850331, -1.1229302, -0.2508607]),
qatom(atom.N, [-0.7859032, -0.7294625, -2.5929226]),
qatom(atom.N, [0.2829723, 1.3909292, -1.3165220]),
qatom(atom.N, [-0.5447553, 5.6874445, 3.4536290]),
qatom(atom.N, [-0.7544505, -1.6514796, 6.7395263]),
qatom(atom.N, [-7.7878748, -1.4780617, 0.1827468]),
qatom(atom.N, [0.4167470, -2.8507918, 1.9421581]),
qatom(atom.N, [1.9022966, -2.1472008, -1.1171428]),
qatom(atom.N, [3.6793118, 4.4025420, 1.2459088]),
qatom(atom.N, [4.7620496, 0.0860942, -0.8292794]),
qatom(atom.O, [-2.1655355, 4.1654505, 3.9706803]),
qatom(atom.O, [0.0239288, -2.4416460, 4.7676561]),
qatom(atom.O, [-6.5929413, -3.0856840, -0.8819590]),
qatom(atom.O, [-0.2286888, -3.6903342, -0.0769724]),
qatom(atom.O, [3.3793237, -1.5383986, -2.7446481]),
qatom(atom.O, [1.9254714, 5.7309896, 1.8116461]),
qatom(atom.O, [4.8685297, 2.3046686, -0.3110650]),
qatom(atom.O, [3.5933887, -1.6454314, 1.2453991]),
qatom(atom.H, [-1.8165024, 2.0714838, 3.5727974]),
qatom(atom.H, [-4.4331446, -3.4945989, -0.6869441]),
qatom(atom.H, [-2.8302490, -3.4153763, -2.6583485]),
qatom(atom.H, [0.0398767, -0.8121672, -5.7041901]),
qatom(atom.H, [2.5806007, 2.6271060, -0.3178848]),
qatom(atom.H, [-0.4192139, 3.1175909, -0.3594303]),
qatom(atom.H, [2.4928328, 1.4447677, 1.4531184]),
qatom(atom.H, [1.8163042, 0.2900014, 0.2898093]),
qatom(atom.H, [1.4837695, 0.0891964, 2.0140417]),
qatom(atom.H, [1.7142524, 1.9060418, 3.5648837]),
qatom(atom.H, [1.8114296, 3.5175975, 2.8430687]),
qatom(atom.H, [0.7647714, 3.2400763, 4.2291178]),
qatom(atom.H, [-1.7065109, 3.5098231, 1.4433461]),
qatom(atom.H, [-0.1671508, 4.3965124, 1.3923655]),
qatom(atom.H, [0.3529294, -0.0999976, 3.5517856]),
qatom(atom.H, [0.0456637, 1.0577702, 4.8450763]),
qatom(atom.H, [-1.9926792, -1.0067123, 3.8844485]),
qatom(atom.H, [-2.1189581, 0.0006125, 5.3381720]),
qatom(atom.H, [-4.9215616, 0.5041334, 2.3468710]),
qatom(atom.H, [-4.0385180, -0.2533678, 3.6689613]),
qatom(atom.H, [-3.7262959, 1.4305623, 3.2407368]),
qatom(atom.H, [-5.5739419, -1.6128585, 2.5291572]),
qatom(atom.H, [-4.1712378, -2.6516067, 2.8134529]),
qatom(atom.H, [-5.5399638, -3.2412221, 1.8598614]),
qatom(atom.H, [-5.6377302, -0.1899235, 0.3767939]),
qatom(atom.H, [-4.9593675, -0.9224896, -1.0839751]),
qatom(atom.H, [-2.5028394, -4.8210416, 0.0186741]),
qatom(atom.H, [-3.7134795, -4.6676928, 1.2854038]),
qatom(atom.H, [-2.1467417, -2.8178695, 2.3142436]),
qatom(atom.H, [-1.6981339, -4.5005317, 2.4487405]),
qatom(atom.H, [-3.4115532, -1.5938760, -4.9672248]),
qatom(atom.H, [-2.2899726, -1.3063537, -6.3158819]),
qatom(atom.H, [-2.3664117, -0.1565594, -4.9617698]),
qatom(atom.H, [-2.4116631, -3.8711594, -4.8260526]),
qatom(atom.H, [-1.1539594, -3.5646041, -6.0214633]),
qatom(atom.H, [-0.7146679, -4.1392328, -4.4011219]),
qatom(atom.H, [2.1773455, -1.6666568, -4.9580199]),
qatom(atom.H, [1.1569958, -2.9882239, -5.5059456]),
qatom(atom.H, [0.6194941, -3.3176386, -2.9074338]),
qatom(atom.H, [2.1538943, -3.8563159, -3.5785735]),
qatom(atom.H, [2.6979101, 0.6316441, -4.7800540]),
qatom(atom.H, [1.8787625, 2.1893761, -4.9033744]),
qatom(atom.H, [1.2036963, 0.7837795, -5.7034044]),
qatom(atom.H, [-0.0272702, 4.1698266, -2.6134627]),
qatom(atom.H, [1.5000327, 4.9956524, -2.9858479]),
qatom(atom.H, [0.8644494, 3.7697529, -4.0862376]),
qatom(atom.H, [0.8994554, 5.1730484, -0.4006657]),
qatom(atom.H, [2.5166511, 5.1362645, -1.0917678]),
qatom(atom.H, [3.2863331, 3.1730193, -3.8052827]),
qatom(atom.H, [3.7482476, 3.7577391, -2.2248300]),
qatom(atom.H, [4.9136128, 1.6653121, -3.1454194]),
qatom(atom.H, [3.4557199, 0.7582279, -2.8163592]),
qatom(atom.H, [5.3961408, 0.3951185, 1.1205701]),
qatom(atom.H, [6.5619833, -0.4620077, 0.1120318]),
qatom(atom.H, [4.9911340, -2.4523213, 0.0386879]),
qatom(atom.H, [5.4487259, -3.1848191, 2.3787979]),
qatom(atom.H, [6.8796686, -2.3920361, 1.6873025]),
qatom(atom.H, [5.8532478, -1.5153717, 2.8372898]),
qatom(atom.H, [-0.7578490, 6.2423191, 4.2724003]),
qatom(atom.H, [0.2712639, 5.9163309, 2.8865228]),
qatom(atom.H, [-0.2568009, -2.3686796, 7.2518537]),
qatom(atom.H, [-1.3134935, -0.9868467, 7.2538637]),
qatom(atom.H, [-7.8375631, -0.5520369, 0.5804760]),
qatom(atom.H, [-8.6514562, -1.9798049, 0.0184000]),
qatom(atom.H, [0.2178448, -2.7140175, 2.9409476]),
qatom(atom.H, [1.3849857, -2.7870769, 1.6471751]),
qatom(atom.H, [2.4953545, -1.7645308, -0.3797860]),
qatom(atom.H, [1.1251287, -2.7599281, -0.8267405]),
qatom(atom.H, [4.1453710, 3.7679030, 0.5902422]),
qatom(atom.H, [4.1524339, 4.6439258, 2.1070555]),
qatom(atom.H, [4.4212901, -0.5988634, -1.5228228]),
qatom(atom.H, [3.5084057, -0.9214013, 1.8876177]),
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
# orig frozen ... 72.00
# orig closed ... 192.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [264]
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
icmr.frozen = [72]
icmr.closed = [192]
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

