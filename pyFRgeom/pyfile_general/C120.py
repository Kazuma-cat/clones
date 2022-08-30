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
qatom(atom.C, [3.593314, 0.035187, -12.270446]),
qatom(atom.C, [3.307390, 1.387260, -12.272973]),
qatom(atom.C, [2.866900, 2.038256, -11.084104]),
qatom(atom.C, [1.779477, 3.018464, -11.088945]),
qatom(atom.C, [1.092204, 3.383560, -12.282799]),
qatom(atom.C, [-0.282078, 3.529719, -12.287407]),
qatom(atom.C, [-1.038576, 3.317559, -11.098489]),
qatom(atom.C, [-2.307596, 2.588134, -11.101919]),
qatom(atom.C, [-2.866771, 2.044021, -12.294527]),
qatom(atom.C, [-3.431468, 0.782399, -12.295345]),
qatom(atom.C, [-3.465081, 0.001598, -11.103378]),
qatom(atom.C, [-3.162524, -1.430101, -11.101294]),
qatom(atom.C, [-2.814611, -2.133826, -12.290903]),
qatom(atom.C, [-1.788026, -3.059656, -12.286603]),
qatom(atom.C, [-1.057885, -3.328613, -11.092403]),
qatom(atom.C, [0.397337, -3.482911, -11.087047]),
qatom(atom.C, [1.176028, -3.374369, -12.275909]),
qatom(atom.C, [2.374334, -2.685160, -12.272219]),
qatom(atom.C, [2.854009, -2.069674, -11.079679]),
qatom(atom.C, [3.452346, -0.734044, -11.078946]),
qatom(atom.C, [3.466481, -0.015227, -9.854214]),
qatom(atom.C, [3.169834, 1.390771, -9.856894]),
qatom(atom.C, [2.804628, 2.010471, -8.610183]),
qatom(atom.C, [1.746375, 2.965094, -8.614857]),
qatom(atom.C, [1.098387, 3.258949, -9.866008]),
qatom(atom.C, [-0.330566, 3.410260, -9.870784]),
qatom(atom.C, [-1.033993, 3.259305, -8.624401]),
qatom(atom.C, [-2.269013, 2.548582, -8.627818]),
qatom(atom.C, [-2.748496, 2.019697, -9.877473]),
qatom(atom.C, [-3.335686, 0.707831, -9.878222]),
qatom(atom.C, [-3.411556, -0.003177, -8.629340]),
qatom(atom.C, [-3.117764, -1.397044, -8.627097]),
qatom(atom.C, [-2.759840, -2.020686, -9.873894]),
qatom(atom.C, [-1.692391, -2.983693, -9.869314]),
qatom(atom.C, [-1.041107, -3.270360, -8.618228]),
qatom(atom.C, [0.375532, -3.420168, -8.613195]),
qatom(atom.C, [1.081084, -3.277563, -9.859422]),
qatom(atom.C, [2.326973, -2.560667, -9.855761]),
qatom(atom.C, [2.799185, -2.025473, -8.606039]),
qatom(atom.C, [3.381385, -0.725054, -8.605275]),
qatom(atom.C, [3.476343, -0.013282, -7.376277]),
qatom(atom.C, [3.178306, 1.401632, -7.378764]),
qatom(atom.C, [2.809156, 2.021255, -6.152913]),
qatom(atom.C, [1.744888, 2.981290, -6.157511]),
qatom(atom.C, [1.096551, 3.279576, -7.387802]),
qatom(atom.C, [-0.341398, 3.431455, -7.392795]),
qatom(atom.C, [-1.046041, 3.276395, -6.167303]),
qatom(atom.C, [-2.287915, 2.561451, -6.170865]),
qatom(atom.C, [-2.770886, 2.033102, -7.399616]),
qatom(atom.C, [-3.362165, 0.713271, -7.400358]),
qatom(atom.C, [-3.434961, -0.000034, -6.172300]),
qatom(atom.C, [-3.139682, -1.401803, -6.169972]),
qatom(atom.C, [-2.784162, -2.029164, -7.395896]),
qatom(atom.C, [-1.709835, -2.998119, -7.391296]),
qatom(atom.C, [-1.055247, -3.282209, -6.160996]),
qatom(atom.C, [0.369368, -3.432738, -6.155957]),
qatom(atom.C, [1.077403, -3.293071, -7.381361]),
qatom(atom.C, [2.331010, -2.571574, -7.377679]),
qatom(atom.C, [2.802055, -2.032460, -6.148952]),
qatom(atom.C, [3.387721, -0.724787, -6.148231]),
qatom(atom.C, [3.460494, -0.005526, -4.906310]),
qatom(atom.C, [3.165214, 1.396243, -4.908637]),
qatom(atom.C, [2.809694, 2.023603, -3.682713]),
qatom(atom.C, [1.735367, 2.992559, -3.687314]),
qatom(atom.C, [1.080779, 3.276649, -4.917614]),
qatom(atom.C, [-0.343835, 3.427178, -4.922653]),
qatom(atom.C, [-1.051871, 3.287512, -3.697249]),
qatom(atom.C, [-2.305479, 2.566016, -3.700932]),
qatom(atom.C, [-2.776522, 2.026901, -4.929660]),
qatom(atom.C, [-3.362187, 0.719228, -4.930380]),
qatom(atom.C, [-3.450808, 0.007724, -3.702333]),
qatom(atom.C, [-3.152771, -1.407190, -3.699844]),
qatom(atom.C, [-2.783621, -2.026814, -4.925697]),
qatom(atom.C, [-1.719355, -2.986849, -4.921099]),
qatom(atom.C, [-1.071017, -3.285134, -3.690806]),
qatom(atom.C, [0.366931, -3.437014, -3.685815]),
qatom(atom.C, [1.071574, -3.281954, -4.911308]),
qatom(atom.C, [2.313448, -2.567010, -4.907747]),
qatom(atom.C, [2.796420, -2.038663, -3.678995]),
qatom(atom.C, [3.387698, -0.718831, -3.678252]),
qatom(atom.C, [3.437089, -0.002383, -2.449270]),
qatom(atom.C, [3.143295, 1.391483, -2.451512]),
qatom(atom.C, [2.785366, 2.015122, -1.204716]),
qatom(atom.C, [1.717919, 2.978127, -1.209296]),
qatom(atom.C, [1.066639, 3.264799, -2.460382]),
qatom(atom.C, [-0.350001, 3.414609, -2.465415]),
qatom(atom.C, [-1.055558, 3.272010, -1.219189]),
qatom(atom.C, [-2.301448, 2.555114, -1.222852]),
qatom(atom.C, [-2.773656, 2.019917, -2.472574]),
qatom(atom.C, [-3.355854, 0.719496, -2.473335]),
qatom(atom.C, [-3.440946, 0.009669, -1.224396]),
qatom(atom.C, [-3.144297, -1.396323, -1.221715]),
qatom(atom.C, [-2.779093, -2.016028, -2.468425]),
qatom(atom.C, [-1.720840, -2.970652, -2.463752]),
qatom(atom.C, [-1.072849, -3.264506, -1.212601]),
qatom(atom.C, [0.356102, -3.415819, -1.207827]),
qatom(atom.C, [1.059527, -3.264867, -2.454210]),
qatom(atom.C, [2.294549, -2.554145, -2.450794]),
qatom(atom.C, [2.774036, -2.025263, -1.201139]),
qatom(atom.C, [3.361224, -0.713395, -1.200388]),
qatom(atom.C, [3.490622, -0.007163, 0.024767]),
qatom(atom.C, [3.188050, 1.424532, 0.022686]),
qatom(atom.C, [2.840122, 2.128240, 1.212293]),
qatom(atom.C, [1.813533, 3.054073, 1.207992]),
qatom(atom.C, [1.083407, 3.323046, 0.013793]),
qatom(atom.C, [-0.371812, 3.477360, 0.008437]),
qatom(atom.C, [-1.150514, 3.368836, 1.197294]),
qatom(atom.C, [-2.348820, 2.679628, 1.193603]),
qatom(atom.C, [-2.828488, 2.064126, 0.001065]),
qatom(atom.C, [-3.426815, 0.728495, 0.000337]),
qatom(atom.C, [-3.567781, -0.040735, 1.191829]),
qatom(atom.C, [-3.281854, -1.392816, 1.194358]),
qatom(atom.C, [-2.841364, -2.043812, 0.005498]),
qatom(atom.C, [-1.753940, -3.024020, 0.010336]),
qatom(atom.C, [-1.066666, -3.389110, 1.204186]),
qatom(atom.C, [0.307621, -3.535270, 1.208793]),
qatom(atom.C, [1.064118, -3.323118, 0.019878]),
qatom(atom.C, [2.333141, -2.593703, 0.023306]),
qatom(atom.C, [2.892331, -2.049596, 1.215913]),
qatom(atom.C, [3.457026, -0.787973, 1.216730]),
qatom(atom.H, [3.724005, -0.336286, 2.174114]),
qatom(atom.H, [3.266207, 1.825358, 2.170739]),
qatom(atom.H, [1.464839, 3.451375, 2.163351]),
qatom(atom.H, [-0.732859, 3.683983, 2.155548]),
qatom(atom.H, [-2.834838, 2.472170, 2.148782]),
qatom(atom.H, [-3.741059, 0.458161, 2.147415]),
qatom(atom.H, [-3.238827, -1.915705, 2.152134]),
qatom(atom.H, [-1.595656, -3.395601, 2.159637]),
qatom(atom.H, [0.817077, -3.652058, 2.167516]),
qatom(atom.H, [2.731255, -2.550161, 2.172622]),
qatom(atom.H, [1.621224, 3.390065, -13.238233]),
qatom(atom.H, [-0.791567, 3.646528, -13.246110]),
qatom(atom.H, [3.766615, -0.463751, -13.226006]),
qatom(atom.H, [3.264367, 1.910190, -13.230727]),
qatom(atom.H, [0.758344, -3.689507, -13.234153]),
qatom(atom.H, [2.860328, -2.477692, -13.227407]),
qatom(atom.H, [-3.240742, -1.830945, -13.249328]),
qatom(atom.H, [-1.439332, -3.457002, -13.241944]),
qatom(atom.H, [-2.705677, 2.544576, -13.251239]),
qatom(atom.H, [-3.698435, 0.330688, -13.252721]),
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
qatom(atom.C, [3.593314, 0.035187, -12.270446]),
qatom(atom.C, [3.307390, 1.387260, -12.272973]),
qatom(atom.C, [2.866900, 2.038256, -11.084104]),
qatom(atom.C, [1.779477, 3.018464, -11.088945]),
qatom(atom.C, [1.092204, 3.383560, -12.282799]),
qatom(atom.C, [-0.282078, 3.529719, -12.287407]),
qatom(atom.C, [-1.038576, 3.317559, -11.098489]),
qatom(atom.C, [-2.307596, 2.588134, -11.101919]),
qatom(atom.C, [-2.866771, 2.044021, -12.294527]),
qatom(atom.C, [-3.431468, 0.782399, -12.295345]),
qatom(atom.C, [-3.465081, 0.001598, -11.103378]),
qatom(atom.C, [-3.162524, -1.430101, -11.101294]),
qatom(atom.C, [-2.814611, -2.133826, -12.290903]),
qatom(atom.C, [-1.788026, -3.059656, -12.286603]),
qatom(atom.C, [-1.057885, -3.328613, -11.092403]),
qatom(atom.C, [0.397337, -3.482911, -11.087047]),
qatom(atom.C, [1.176028, -3.374369, -12.275909]),
qatom(atom.C, [2.374334, -2.685160, -12.272219]),
qatom(atom.C, [2.854009, -2.069674, -11.079679]),
qatom(atom.C, [3.452346, -0.734044, -11.078946]),
qatom(atom.C, [3.466481, -0.015227, -9.854214]),
qatom(atom.C, [3.169834, 1.390771, -9.856894]),
qatom(atom.C, [2.804628, 2.010471, -8.610183]),
qatom(atom.C, [1.746375, 2.965094, -8.614857]),
qatom(atom.C, [1.098387, 3.258949, -9.866008]),
qatom(atom.C, [-0.330566, 3.410260, -9.870784]),
qatom(atom.C, [-1.033993, 3.259305, -8.624401]),
qatom(atom.C, [-2.269013, 2.548582, -8.627818]),
qatom(atom.C, [-2.748496, 2.019697, -9.877473]),
qatom(atom.C, [-3.335686, 0.707831, -9.878222]),
qatom(atom.C, [-3.411556, -0.003177, -8.629340]),
qatom(atom.C, [-3.117764, -1.397044, -8.627097]),
qatom(atom.C, [-2.759840, -2.020686, -9.873894]),
qatom(atom.C, [-1.692391, -2.983693, -9.869314]),
qatom(atom.C, [-1.041107, -3.270360, -8.618228]),
qatom(atom.C, [0.375532, -3.420168, -8.613195]),
qatom(atom.C, [1.081084, -3.277563, -9.859422]),
qatom(atom.C, [2.326973, -2.560667, -9.855761]),
qatom(atom.C, [2.799185, -2.025473, -8.606039]),
qatom(atom.C, [3.381385, -0.725054, -8.605275]),
qatom(atom.C, [3.476343, -0.013282, -7.376277]),
qatom(atom.C, [3.178306, 1.401632, -7.378764]),
qatom(atom.C, [2.809156, 2.021255, -6.152913]),
qatom(atom.C, [1.744888, 2.981290, -6.157511]),
qatom(atom.C, [1.096551, 3.279576, -7.387802]),
qatom(atom.C, [-0.341398, 3.431455, -7.392795]),
qatom(atom.C, [-1.046041, 3.276395, -6.167303]),
qatom(atom.C, [-2.287915, 2.561451, -6.170865]),
qatom(atom.C, [-2.770886, 2.033102, -7.399616]),
qatom(atom.C, [-3.362165, 0.713271, -7.400358]),
qatom(atom.C, [-3.434961, -0.000034, -6.172300]),
qatom(atom.C, [-3.139682, -1.401803, -6.169972]),
qatom(atom.C, [-2.784162, -2.029164, -7.395896]),
qatom(atom.C, [-1.709835, -2.998119, -7.391296]),
qatom(atom.C, [-1.055247, -3.282209, -6.160996]),
qatom(atom.C, [0.369368, -3.432738, -6.155957]),
qatom(atom.C, [1.077403, -3.293071, -7.381361]),
qatom(atom.C, [2.331010, -2.571574, -7.377679]),
qatom(atom.C, [2.802055, -2.032460, -6.148952]),
qatom(atom.C, [3.387721, -0.724787, -6.148231]),
qatom(atom.C, [3.460494, -0.005526, -4.906310]),
qatom(atom.C, [3.165214, 1.396243, -4.908637]),
qatom(atom.C, [2.809694, 2.023603, -3.682713]),
qatom(atom.C, [1.735367, 2.992559, -3.687314]),
qatom(atom.C, [1.080779, 3.276649, -4.917614]),
qatom(atom.C, [-0.343835, 3.427178, -4.922653]),
qatom(atom.C, [-1.051871, 3.287512, -3.697249]),
qatom(atom.C, [-2.305479, 2.566016, -3.700932]),
qatom(atom.C, [-2.776522, 2.026901, -4.929660]),
qatom(atom.C, [-3.362187, 0.719228, -4.930380]),
qatom(atom.C, [-3.450808, 0.007724, -3.702333]),
qatom(atom.C, [-3.152771, -1.407190, -3.699844]),
qatom(atom.C, [-2.783621, -2.026814, -4.925697]),
qatom(atom.C, [-1.719355, -2.986849, -4.921099]),
qatom(atom.C, [-1.071017, -3.285134, -3.690806]),
qatom(atom.C, [0.366931, -3.437014, -3.685815]),
qatom(atom.C, [1.071574, -3.281954, -4.911308]),
qatom(atom.C, [2.313448, -2.567010, -4.907747]),
qatom(atom.C, [2.796420, -2.038663, -3.678995]),
qatom(atom.C, [3.387698, -0.718831, -3.678252]),
qatom(atom.C, [3.437089, -0.002383, -2.449270]),
qatom(atom.C, [3.143295, 1.391483, -2.451512]),
qatom(atom.C, [2.785366, 2.015122, -1.204716]),
qatom(atom.C, [1.717919, 2.978127, -1.209296]),
qatom(atom.C, [1.066639, 3.264799, -2.460382]),
qatom(atom.C, [-0.350001, 3.414609, -2.465415]),
qatom(atom.C, [-1.055558, 3.272010, -1.219189]),
qatom(atom.C, [-2.301448, 2.555114, -1.222852]),
qatom(atom.C, [-2.773656, 2.019917, -2.472574]),
qatom(atom.C, [-3.355854, 0.719496, -2.473335]),
qatom(atom.C, [-3.440946, 0.009669, -1.224396]),
qatom(atom.C, [-3.144297, -1.396323, -1.221715]),
qatom(atom.C, [-2.779093, -2.016028, -2.468425]),
qatom(atom.C, [-1.720840, -2.970652, -2.463752]),
qatom(atom.C, [-1.072849, -3.264506, -1.212601]),
qatom(atom.C, [0.356102, -3.415819, -1.207827]),
qatom(atom.C, [1.059527, -3.264867, -2.454210]),
qatom(atom.C, [2.294549, -2.554145, -2.450794]),
qatom(atom.C, [2.774036, -2.025263, -1.201139]),
qatom(atom.C, [3.361224, -0.713395, -1.200388]),
qatom(atom.C, [3.490622, -0.007163, 0.024767]),
qatom(atom.C, [3.188050, 1.424532, 0.022686]),
qatom(atom.C, [2.840122, 2.128240, 1.212293]),
qatom(atom.C, [1.813533, 3.054073, 1.207992]),
qatom(atom.C, [1.083407, 3.323046, 0.013793]),
qatom(atom.C, [-0.371812, 3.477360, 0.008437]),
qatom(atom.C, [-1.150514, 3.368836, 1.197294]),
qatom(atom.C, [-2.348820, 2.679628, 1.193603]),
qatom(atom.C, [-2.828488, 2.064126, 0.001065]),
qatom(atom.C, [-3.426815, 0.728495, 0.000337]),
qatom(atom.C, [-3.567781, -0.040735, 1.191829]),
qatom(atom.C, [-3.281854, -1.392816, 1.194358]),
qatom(atom.C, [-2.841364, -2.043812, 0.005498]),
qatom(atom.C, [-1.753940, -3.024020, 0.010336]),
qatom(atom.C, [-1.066666, -3.389110, 1.204186]),
qatom(atom.C, [0.307621, -3.535270, 1.208793]),
qatom(atom.C, [1.064118, -3.323118, 0.019878]),
qatom(atom.C, [2.333141, -2.593703, 0.023306]),
qatom(atom.C, [2.892331, -2.049596, 1.215913]),
qatom(atom.C, [3.457026, -0.787973, 1.216730]),
qatom(atom.H, [3.724005, -0.336286, 2.174114]),
qatom(atom.H, [3.266207, 1.825358, 2.170739]),
qatom(atom.H, [1.464839, 3.451375, 2.163351]),
qatom(atom.H, [-0.732859, 3.683983, 2.155548]),
qatom(atom.H, [-2.834838, 2.472170, 2.148782]),
qatom(atom.H, [-3.741059, 0.458161, 2.147415]),
qatom(atom.H, [-3.238827, -1.915705, 2.152134]),
qatom(atom.H, [-1.595656, -3.395601, 2.159637]),
qatom(atom.H, [0.817077, -3.652058, 2.167516]),
qatom(atom.H, [2.731255, -2.550161, 2.172622]),
qatom(atom.H, [1.621224, 3.390065, -13.238233]),
qatom(atom.H, [-0.791567, 3.646528, -13.246110]),
qatom(atom.H, [3.766615, -0.463751, -13.226006]),
qatom(atom.H, [3.264367, 1.910190, -13.230727]),
qatom(atom.H, [0.758344, -3.689507, -13.234153]),
qatom(atom.H, [2.860328, -2.477692, -13.227407]),
qatom(atom.H, [-3.240742, -1.830945, -13.249328]),
qatom(atom.H, [-1.439332, -3.457002, -13.241944]),
qatom(atom.H, [-2.705677, 2.544576, -13.251239]),
qatom(atom.H, [-3.698435, 0.330688, -13.252721]),
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
# orig frozen ... 120.00
# orig closed ... 250.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [370]
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
icmr.frozen = [120]
icmr.closed = [250]
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

