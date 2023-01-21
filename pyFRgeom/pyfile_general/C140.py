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
qatom(atom.C, [3.546720, 0.053978, -14.770415]),
qatom(atom.C, [3.260557, 1.395327, -14.770719]),
qatom(atom.C, [2.813832, 2.045660, -13.568223]),
qatom(atom.C, [1.738133, 3.011694, -13.568363]),
qatom(atom.C, [1.043822, 3.385598, -14.770991]),
qatom(atom.C, [-0.320350, 3.527965, -14.770715]),
qatom(atom.C, [-1.076363, 3.304905, -13.567920]),
qatom(atom.C, [-2.328308, 2.582242, -13.567666]),
qatom(atom.C, [-2.899870, 2.038967, -14.770357]),
qatom(atom.C, [-3.458144, 0.785928, -14.770437]),
qatom(atom.C, [-3.479612, -0.002465, -13.567597]),
qatom(atom.C, [-3.178176, -1.415835, -13.567907]),
qatom(atom.C, [-2.836243, -2.126148, -14.770914]),
qatom(atom.C, [-1.815773, -3.043097, -14.771011]),
qatom(atom.C, [-1.073105, -3.307751, -13.568019]),
qatom(atom.C, [0.364348, -3.457457, -13.567793]),
qatom(atom.C, [1.145774, -3.352184, -14.770739]),
qatom(atom.C, [2.333690, -2.665896, -14.770548]),
qatom(atom.C, [2.814777, -2.041609, -13.567596]),
qatom(atom.C, [3.403316, -0.721485, -13.567661]),
qatom(atom.C, [3.440474, -0.003842, -12.340748]),
qatom(atom.C, [3.140472, 1.405756, -12.341094]),
qatom(atom.C, [2.769238, 2.017972, -11.098612]),
qatom(atom.C, [1.715213, 2.965166, -11.098696]),
qatom(atom.C, [1.066976, 3.268667, -12.341301]),
qatom(atom.C, [-0.366470, 3.417645, -12.341024]),
qatom(atom.C, [-1.062781, 3.253762, -11.098405]),
qatom(atom.C, [-2.289507, 2.544862, -11.098247]),
qatom(atom.C, [-2.780120, 2.023653, -12.340668]),
qatom(atom.C, [-3.366781, 0.706960, -12.340619]),
qatom(atom.C, [-3.426328, -0.006227, -11.098211]),
qatom(atom.C, [-3.131715, -1.391674, -11.098340]),
qatom(atom.C, [-2.786430, -2.018630, -12.340910]),
qatom(atom.C, [-1.714000, -2.982474, -12.340926]),
qatom(atom.C, [-1.053818, -3.259144, -11.098390]),
qatom(atom.C, [0.355072, -3.405371, -11.098308]),
qatom(atom.C, [1.058039, -3.270850, -12.340761]),
qatom(atom.C, [2.306226, -2.549516, -12.340750]),
qatom(atom.C, [2.773602, -2.007632, -11.098211]),
qatom(atom.C, [3.350248, -0.713585, -11.098245]),
qatom(atom.C, [3.440531, 0.003319, -9.856107]),
qatom(atom.C, [3.143756, 1.399942, -9.856257]),
qatom(atom.C, [2.793762, 2.028586, -8.626468]),
qatom(atom.C, [1.723032, 2.990717, -8.626508]),
qatom(atom.C, [1.060855, 3.271859, -9.856352]),
qatom(atom.C, [-0.359360, 3.419103, -9.856252]),
qatom(atom.C, [-1.064749, 3.280072, -8.626343]),
qatom(atom.C, [-2.310698, 2.559813, -8.626234]),
qatom(atom.C, [-2.783644, 2.017892, -9.855961]),
qatom(atom.C, [-3.365092, 0.713527, -9.855917]),
qatom(atom.C, [-3.451679, -0.000389, -8.626157]),
qatom(atom.C, [-3.152687, -1.407701, -8.626196]),
qatom(atom.C, [-2.782918, -2.024785, -9.856088]),
qatom(atom.C, [-1.720350, -2.979647, -9.856127]),
qatom(atom.C, [-1.067542, -3.281718, -8.626190]),
qatom(atom.C, [0.363529, -3.430039, -8.626162]),
qatom(atom.C, [1.064362, -3.268804, -9.855981]),
qatom(atom.C, [2.300887, -2.554030, -9.855927]),
qatom(atom.C, [2.790363, -2.027071, -8.626185]),
qatom(atom.C, [3.376347, -0.712810, -8.626250]),
qatom(atom.C, [3.441698, 0.005144, -7.392746]),
qatom(atom.C, [3.145590, 1.399173, -7.392823]),
qatom(atom.C, [2.782985, 2.026839, -6.150398]),
qatom(atom.C, [1.722448, 2.979944, -6.150425]),
qatom(atom.C, [1.059872, 3.273748, -7.392868]),
qatom(atom.C, [-0.357701, 3.420665, -7.392806]),
qatom(atom.C, [-1.066181, 3.269283, -6.150394]),
qatom(atom.C, [-2.300317, 2.555713, -6.150332]),
qatom(atom.C, [-2.785285, 2.017241, -7.392663]),
qatom(atom.C, [-3.365672, 0.715319, -7.392623]),
qatom(atom.C, [-3.441698, -0.005145, -6.150221]),
qatom(atom.C, [-3.145590, -1.399174, -6.150144]),
qatom(atom.C, [-2.782985, -2.026839, -7.392569]),
qatom(atom.C, [-1.722449, -2.979945, -7.392542]),
qatom(atom.C, [-1.059872, -3.273749, -6.150099]),
qatom(atom.C, [0.357701, -3.420665, -6.150161]),
qatom(atom.C, [1.066181, -3.269283, -7.392573]),
qatom(atom.C, [2.300317, -2.555713, -7.392635]),
qatom(atom.C, [2.785285, -2.017242, -6.150304]),
qatom(atom.C, [3.365672, -0.715320, -6.150344]),
qatom(atom.C, [3.451679, 0.000388, -4.916810]),
qatom(atom.C, [3.152687, 1.407700, -4.916770]),
qatom(atom.C, [2.782917, 2.024785, -3.686879]),
qatom(atom.C, [1.720349, 2.979646, -3.686840]),
qatom(atom.C, [1.067542, 3.281717, -4.916777]),
qatom(atom.C, [-0.363530, 3.430039, -4.916805]),
qatom(atom.C, [-1.064362, 3.268805, -3.686986]),
qatom(atom.C, [-2.300887, 2.554030, -3.687040]),
qatom(atom.C, [-2.790363, 2.027071, -4.916782]),
qatom(atom.C, [-3.376347, 0.712809, -4.916717]),
qatom(atom.C, [-3.440531, -0.003320, -3.686860]),
qatom(atom.C, [-3.143756, -1.399943, -3.686710]),
qatom(atom.C, [-2.793762, -2.028586, -4.916498]),
qatom(atom.C, [-1.723032, -2.990718, -4.916459]),
qatom(atom.C, [-1.060855, -3.271859, -3.686615]),
qatom(atom.C, [0.359360, -3.419103, -3.686715]),
qatom(atom.C, [1.064749, -3.280072, -4.916624]),
qatom(atom.C, [2.310698, -2.559813, -4.916733]),
qatom(atom.C, [2.783644, -2.017893, -3.687006]),
qatom(atom.C, [3.365092, -0.713528, -3.687049]),
qatom(atom.C, [3.426327, 0.006227, -2.444755]),
qatom(atom.C, [3.131714, 1.391673, -2.444626]),
qatom(atom.C, [2.786429, 2.018630, -1.202057]),
qatom(atom.C, [1.713999, 2.982474, -1.202041]),
qatom(atom.C, [1.053818, 3.259144, -2.444577]),
qatom(atom.C, [-0.355072, 3.405372, -2.444659]),
qatom(atom.C, [-1.058039, 3.270851, -1.202206]),
qatom(atom.C, [-2.306226, 2.549517, -1.202217]),
qatom(atom.C, [-2.773602, 2.007632, -2.444756]),
qatom(atom.C, [-3.350247, 0.713585, -2.444721]),
qatom(atom.C, [-3.440473, 0.003842, -1.202218]),
qatom(atom.C, [-3.140471, -1.405756, -1.201873]),
qatom(atom.C, [-2.769237, -2.017973, -2.444355]),
qatom(atom.C, [-1.715213, -2.965166, -2.444271]),
qatom(atom.C, [-1.066976, -3.268667, -1.201666]),
qatom(atom.C, [0.366470, -3.417646, -1.201943]),
qatom(atom.C, [1.062782, -3.253762, -2.444561]),
qatom(atom.C, [2.289508, -2.544862, -2.444720]),
qatom(atom.C, [2.780120, -2.023653, -1.202299]),
qatom(atom.C, [3.366781, -0.706960, -1.202348]),
qatom(atom.C, [3.479611, 0.002465, 0.024630]),
qatom(atom.C, [3.178175, 1.415835, 0.024940]),
qatom(atom.C, [2.836243, 2.126149, 1.227947]),
qatom(atom.C, [1.815772, 3.043098, 1.228044]),
qatom(atom.C, [1.073105, 3.307751, 0.025052]),
qatom(atom.C, [-0.364349, 3.457458, 0.024826]),
qatom(atom.C, [-1.145774, 3.352185, 1.227772]),
qatom(atom.C, [-2.333690, 2.665897, 1.227581]),
qatom(atom.C, [-2.814777, 2.041610, 0.024629]),
qatom(atom.C, [-3.403315, 0.721485, 0.024694]),
qatom(atom.C, [-3.546719, -0.053978, 1.227448]),
qatom(atom.C, [-3.260555, -1.395327, 1.227752]),
qatom(atom.C, [-2.813831, -2.045660, 0.025257]),
qatom(atom.C, [-1.738132, -3.011694, 0.025396]),
qatom(atom.C, [-1.043822, -3.385599, 1.228024]),
qatom(atom.C, [0.320351, -3.527965, 1.227748]),
qatom(atom.C, [1.076364, -3.304905, 0.024953]),
qatom(atom.C, [2.328308, -2.582242, 0.024699]),
qatom(atom.C, [2.899870, -2.038966, 1.227390]),
qatom(atom.C, [3.458143, -0.785927, 1.227471]),
qatom(atom.H, [-2.765474, 2.559589, -15.720457]),
qatom(atom.H, [-3.756650, 0.338992, -15.720672]),
qatom(atom.H, [-0.838178, 3.673762, -15.720908]),
qatom(atom.H, [1.580415, 3.421656, -15.721446]),
qatom(atom.H, [3.239437, 1.932834, -15.721043]),
qatom(atom.H, [3.747011, -0.445492, -15.720379]),
qatom(atom.H, [2.836924, -2.476923, -15.720638]),
qatom(atom.H, [0.732691, -3.695497, -15.721211]),
qatom(atom.H, [-1.482355, -3.464750, -15.721292]),
qatom(atom.H, [-3.290427, -1.838504, -15.721072]),
qatom(atom.H, [-3.239435, -1.932834, 2.178076]),
qatom(atom.H, [-3.747009, 0.445492, 2.177413]),
qatom(atom.H, [-2.836924, 2.476924, 2.177671]),
qatom(atom.H, [-0.732691, 3.695499, 2.178244]),
qatom(atom.H, [2.765473, -2.559589, 2.177490]),
qatom(atom.H, [3.756649, -0.338991, 2.177705]),
qatom(atom.H, [3.290426, 1.838504, 2.178105]),
qatom(atom.H, [1.482354, 3.464751, 2.178325]),
qatom(atom.H, [0.838179, -3.673762, 2.177941]),
qatom(atom.H, [-1.580415, -3.421656, 2.178480]),
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
qatom(atom.C, [3.546720, 0.053978, -14.770415]),
qatom(atom.C, [3.260557, 1.395327, -14.770719]),
qatom(atom.C, [2.813832, 2.045660, -13.568223]),
qatom(atom.C, [1.738133, 3.011694, -13.568363]),
qatom(atom.C, [1.043822, 3.385598, -14.770991]),
qatom(atom.C, [-0.320350, 3.527965, -14.770715]),
qatom(atom.C, [-1.076363, 3.304905, -13.567920]),
qatom(atom.C, [-2.328308, 2.582242, -13.567666]),
qatom(atom.C, [-2.899870, 2.038967, -14.770357]),
qatom(atom.C, [-3.458144, 0.785928, -14.770437]),
qatom(atom.C, [-3.479612, -0.002465, -13.567597]),
qatom(atom.C, [-3.178176, -1.415835, -13.567907]),
qatom(atom.C, [-2.836243, -2.126148, -14.770914]),
qatom(atom.C, [-1.815773, -3.043097, -14.771011]),
qatom(atom.C, [-1.073105, -3.307751, -13.568019]),
qatom(atom.C, [0.364348, -3.457457, -13.567793]),
qatom(atom.C, [1.145774, -3.352184, -14.770739]),
qatom(atom.C, [2.333690, -2.665896, -14.770548]),
qatom(atom.C, [2.814777, -2.041609, -13.567596]),
qatom(atom.C, [3.403316, -0.721485, -13.567661]),
qatom(atom.C, [3.440474, -0.003842, -12.340748]),
qatom(atom.C, [3.140472, 1.405756, -12.341094]),
qatom(atom.C, [2.769238, 2.017972, -11.098612]),
qatom(atom.C, [1.715213, 2.965166, -11.098696]),
qatom(atom.C, [1.066976, 3.268667, -12.341301]),
qatom(atom.C, [-0.366470, 3.417645, -12.341024]),
qatom(atom.C, [-1.062781, 3.253762, -11.098405]),
qatom(atom.C, [-2.289507, 2.544862, -11.098247]),
qatom(atom.C, [-2.780120, 2.023653, -12.340668]),
qatom(atom.C, [-3.366781, 0.706960, -12.340619]),
qatom(atom.C, [-3.426328, -0.006227, -11.098211]),
qatom(atom.C, [-3.131715, -1.391674, -11.098340]),
qatom(atom.C, [-2.786430, -2.018630, -12.340910]),
qatom(atom.C, [-1.714000, -2.982474, -12.340926]),
qatom(atom.C, [-1.053818, -3.259144, -11.098390]),
qatom(atom.C, [0.355072, -3.405371, -11.098308]),
qatom(atom.C, [1.058039, -3.270850, -12.340761]),
qatom(atom.C, [2.306226, -2.549516, -12.340750]),
qatom(atom.C, [2.773602, -2.007632, -11.098211]),
qatom(atom.C, [3.350248, -0.713585, -11.098245]),
qatom(atom.C, [3.440531, 0.003319, -9.856107]),
qatom(atom.C, [3.143756, 1.399942, -9.856257]),
qatom(atom.C, [2.793762, 2.028586, -8.626468]),
qatom(atom.C, [1.723032, 2.990717, -8.626508]),
qatom(atom.C, [1.060855, 3.271859, -9.856352]),
qatom(atom.C, [-0.359360, 3.419103, -9.856252]),
qatom(atom.C, [-1.064749, 3.280072, -8.626343]),
qatom(atom.C, [-2.310698, 2.559813, -8.626234]),
qatom(atom.C, [-2.783644, 2.017892, -9.855961]),
qatom(atom.C, [-3.365092, 0.713527, -9.855917]),
qatom(atom.C, [-3.451679, -0.000389, -8.626157]),
qatom(atom.C, [-3.152687, -1.407701, -8.626196]),
qatom(atom.C, [-2.782918, -2.024785, -9.856088]),
qatom(atom.C, [-1.720350, -2.979647, -9.856127]),
qatom(atom.C, [-1.067542, -3.281718, -8.626190]),
qatom(atom.C, [0.363529, -3.430039, -8.626162]),
qatom(atom.C, [1.064362, -3.268804, -9.855981]),
qatom(atom.C, [2.300887, -2.554030, -9.855927]),
qatom(atom.C, [2.790363, -2.027071, -8.626185]),
qatom(atom.C, [3.376347, -0.712810, -8.626250]),
qatom(atom.C, [3.441698, 0.005144, -7.392746]),
qatom(atom.C, [3.145590, 1.399173, -7.392823]),
qatom(atom.C, [2.782985, 2.026839, -6.150398]),
qatom(atom.C, [1.722448, 2.979944, -6.150425]),
qatom(atom.C, [1.059872, 3.273748, -7.392868]),
qatom(atom.C, [-0.357701, 3.420665, -7.392806]),
qatom(atom.C, [-1.066181, 3.269283, -6.150394]),
qatom(atom.C, [-2.300317, 2.555713, -6.150332]),
qatom(atom.C, [-2.785285, 2.017241, -7.392663]),
qatom(atom.C, [-3.365672, 0.715319, -7.392623]),
qatom(atom.C, [-3.441698, -0.005145, -6.150221]),
qatom(atom.C, [-3.145590, -1.399174, -6.150144]),
qatom(atom.C, [-2.782985, -2.026839, -7.392569]),
qatom(atom.C, [-1.722449, -2.979945, -7.392542]),
qatom(atom.C, [-1.059872, -3.273749, -6.150099]),
qatom(atom.C, [0.357701, -3.420665, -6.150161]),
qatom(atom.C, [1.066181, -3.269283, -7.392573]),
qatom(atom.C, [2.300317, -2.555713, -7.392635]),
qatom(atom.C, [2.785285, -2.017242, -6.150304]),
qatom(atom.C, [3.365672, -0.715320, -6.150344]),
qatom(atom.C, [3.451679, 0.000388, -4.916810]),
qatom(atom.C, [3.152687, 1.407700, -4.916770]),
qatom(atom.C, [2.782917, 2.024785, -3.686879]),
qatom(atom.C, [1.720349, 2.979646, -3.686840]),
qatom(atom.C, [1.067542, 3.281717, -4.916777]),
qatom(atom.C, [-0.363530, 3.430039, -4.916805]),
qatom(atom.C, [-1.064362, 3.268805, -3.686986]),
qatom(atom.C, [-2.300887, 2.554030, -3.687040]),
qatom(atom.C, [-2.790363, 2.027071, -4.916782]),
qatom(atom.C, [-3.376347, 0.712809, -4.916717]),
qatom(atom.C, [-3.440531, -0.003320, -3.686860]),
qatom(atom.C, [-3.143756, -1.399943, -3.686710]),
qatom(atom.C, [-2.793762, -2.028586, -4.916498]),
qatom(atom.C, [-1.723032, -2.990718, -4.916459]),
qatom(atom.C, [-1.060855, -3.271859, -3.686615]),
qatom(atom.C, [0.359360, -3.419103, -3.686715]),
qatom(atom.C, [1.064749, -3.280072, -4.916624]),
qatom(atom.C, [2.310698, -2.559813, -4.916733]),
qatom(atom.C, [2.783644, -2.017893, -3.687006]),
qatom(atom.C, [3.365092, -0.713528, -3.687049]),
qatom(atom.C, [3.426327, 0.006227, -2.444755]),
qatom(atom.C, [3.131714, 1.391673, -2.444626]),
qatom(atom.C, [2.786429, 2.018630, -1.202057]),
qatom(atom.C, [1.713999, 2.982474, -1.202041]),
qatom(atom.C, [1.053818, 3.259144, -2.444577]),
qatom(atom.C, [-0.355072, 3.405372, -2.444659]),
qatom(atom.C, [-1.058039, 3.270851, -1.202206]),
qatom(atom.C, [-2.306226, 2.549517, -1.202217]),
qatom(atom.C, [-2.773602, 2.007632, -2.444756]),
qatom(atom.C, [-3.350247, 0.713585, -2.444721]),
qatom(atom.C, [-3.440473, 0.003842, -1.202218]),
qatom(atom.C, [-3.140471, -1.405756, -1.201873]),
qatom(atom.C, [-2.769237, -2.017973, -2.444355]),
qatom(atom.C, [-1.715213, -2.965166, -2.444271]),
qatom(atom.C, [-1.066976, -3.268667, -1.201666]),
qatom(atom.C, [0.366470, -3.417646, -1.201943]),
qatom(atom.C, [1.062782, -3.253762, -2.444561]),
qatom(atom.C, [2.289508, -2.544862, -2.444720]),
qatom(atom.C, [2.780120, -2.023653, -1.202299]),
qatom(atom.C, [3.366781, -0.706960, -1.202348]),
qatom(atom.C, [3.479611, 0.002465, 0.024630]),
qatom(atom.C, [3.178175, 1.415835, 0.024940]),
qatom(atom.C, [2.836243, 2.126149, 1.227947]),
qatom(atom.C, [1.815772, 3.043098, 1.228044]),
qatom(atom.C, [1.073105, 3.307751, 0.025052]),
qatom(atom.C, [-0.364349, 3.457458, 0.024826]),
qatom(atom.C, [-1.145774, 3.352185, 1.227772]),
qatom(atom.C, [-2.333690, 2.665897, 1.227581]),
qatom(atom.C, [-2.814777, 2.041610, 0.024629]),
qatom(atom.C, [-3.403315, 0.721485, 0.024694]),
qatom(atom.C, [-3.546719, -0.053978, 1.227448]),
qatom(atom.C, [-3.260555, -1.395327, 1.227752]),
qatom(atom.C, [-2.813831, -2.045660, 0.025257]),
qatom(atom.C, [-1.738132, -3.011694, 0.025396]),
qatom(atom.C, [-1.043822, -3.385599, 1.228024]),
qatom(atom.C, [0.320351, -3.527965, 1.227748]),
qatom(atom.C, [1.076364, -3.304905, 0.024953]),
qatom(atom.C, [2.328308, -2.582242, 0.024699]),
qatom(atom.C, [2.899870, -2.038966, 1.227390]),
qatom(atom.C, [3.458143, -0.785927, 1.227471]),
qatom(atom.H, [-2.765474, 2.559589, -15.720457]),
qatom(atom.H, [-3.756650, 0.338992, -15.720672]),
qatom(atom.H, [-0.838178, 3.673762, -15.720908]),
qatom(atom.H, [1.580415, 3.421656, -15.721446]),
qatom(atom.H, [3.239437, 1.932834, -15.721043]),
qatom(atom.H, [3.747011, -0.445492, -15.720379]),
qatom(atom.H, [2.836924, -2.476923, -15.720638]),
qatom(atom.H, [0.732691, -3.695497, -15.721211]),
qatom(atom.H, [-1.482355, -3.464750, -15.721292]),
qatom(atom.H, [-3.290427, -1.838504, -15.721072]),
qatom(atom.H, [-3.239435, -1.932834, 2.178076]),
qatom(atom.H, [-3.747009, 0.445492, 2.177413]),
qatom(atom.H, [-2.836924, 2.476924, 2.177671]),
qatom(atom.H, [-0.732691, 3.695499, 2.178244]),
qatom(atom.H, [2.765473, -2.559589, 2.177490]),
qatom(atom.H, [3.756649, -0.338991, 2.177705]),
qatom(atom.H, [3.290426, 1.838504, 2.178105]),
qatom(atom.H, [1.482354, 3.464751, 2.178325]),
qatom(atom.H, [0.838179, -3.673762, 2.177941]),
qatom(atom.H, [-1.580415, -3.421656, 2.178480]),
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
# orig frozen ... 140.00
# orig closed ... 290.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [430]
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
icmr.frozen = [140]
icmr.closed = [290]
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
lct.PrintAllEps = False


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

