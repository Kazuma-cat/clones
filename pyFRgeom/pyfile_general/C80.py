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
qatom(atom.C, [-2.300974, -3.731013, 1.165922]),
qatom(atom.C, [-2.453048, -2.582743, -2.833581]),
qatom(atom.C, [-6.459486, -2.187114, -3.901559]),
qatom(atom.C, [-8.790078, -3.090444, -0.568267]),
qatom(atom.C, [-6.212307, -4.044809, 2.562582]),
qatom(atom.C, [-3.270968, -3.977055, 2.099731]),
qatom(atom.C, [-1.830855, -2.931044, -1.664985]),
qatom(atom.C, [-5.107735, -2.156494, -4.115422]),
qatom(atom.C, [-8.572858, -2.722501, -1.868757]),
qatom(atom.C, [-7.432095, -3.849759, 1.973291]),
qatom(atom.C, [-1.746303, -1.990372, -0.574578]),
qatom(atom.C, [-4.312968, -1.064880, -3.608339]),
qatom(atom.C, [-8.126327, -1.387648, -2.185419]),
qatom(atom.C, [-7.919794, -2.514320, 1.729776]),
qatom(atom.C, [-3.978136, -2.885768, 2.723052]),
qatom(atom.C, [-1.973876, -2.376784, 0.792351]),
qatom(atom.C, [-3.031035, -1.270248, -2.990189]),
qatom(atom.C, [-7.107011, -1.128874, -3.166457]),
qatom(atom.C, [-8.574313, -2.148095, 0.502687]),
qatom(atom.C, [-5.398209, -2.918197, 2.947020]),
qatom(atom.C, [-2.303776, -1.360336, 1.734060]),
qatom(atom.C, [-2.517755, -0.244515, -2.145501]),
qatom(atom.C, [-6.425384, 0.120835, -3.117704]),
qatom(atom.C, [-8.628383, -0.767963, 0.154309]),
qatom(atom.C, [-6.077215, -1.683342, 3.152582]),
qatom(atom.C, [-3.325754, -1.619851, 2.718063]),
qatom(atom.C, [-1.862728, -0.611694, -0.913848]),
qatom(atom.C, [-5.001421, 0.153389, -3.343148]),
qatom(atom.C, [-8.399556, -0.380231, -1.216194]),
qatom(atom.C, [-7.362837, -1.477671, 2.532606]),
qatom(atom.C, [-1.743990, 0.382068, 0.108376]),
qatom(atom.C, [-4.272358, 1.294189, -2.881351]),
qatom(atom.C, [-8.030002, 0.976161, -1.480041]),
qatom(atom.C, [-7.828913, -0.134056, 2.379452]),
qatom(atom.C, [-3.944899, -0.500289, 3.357571]),
qatom(atom.C, [-1.968665, 0.001646, 1.453488]),
qatom(atom.C, [-3.010306, 1.092355, -2.273485]),
qatom(atom.C, [-7.026943, 1.230927, -2.445776]),
qatom(atom.C, [-8.471926, 0.226317, 1.170801]),
qatom(atom.C, [-5.342525, -0.532218, 3.578488]),
qatom(atom.C, [-2.271472, 1.028230, 2.416511]),
qatom(atom.C, [-2.472564, 2.138450, -1.442992]),
qatom(atom.C, [-6.356588, 2.504683, -2.421108]),
qatom(atom.C, [-8.557498, 1.622324, 0.828095]),
qatom(atom.C, [-6.029123, 0.710201, 3.817826]),
qatom(atom.C, [-3.274538, 0.773463, 3.382251]),
qatom(atom.C, [-1.829547, 1.778074, -0.234333]),
qatom(atom.C, [-4.958954, 2.536612, -2.642029]),
qatom(atom.C, [-8.332822, 2.002748, -0.517025]),
qatom(atom.C, [-7.291182, 0.912037, 3.209956]),
qatom(atom.C, [-1.673098, 2.772348, 0.782154]),
qatom(atom.C, [-4.224267, 3.687727, -2.216120]),
qatom(atom.C, [-7.997708, 3.364720, -0.797595]),
qatom(atom.C, [-7.783727, 2.248899, 3.081968]),
qatom(atom.C, [-3.876096, 1.883550, 4.054170]),
qatom(atom.C, [-1.901924, 2.384615, 2.152661]),
qatom(atom.C, [-2.938642, 3.482056, -1.596142]),
qatom(atom.C, [-6.975727, 3.624237, -1.781599]),
qatom(atom.C, [-8.438754, 2.616079, 1.850314]),
qatom(atom.C, [-5.300061, 1.850995, 4.279616]),
qatom(atom.C, [-2.175171, 3.392038, 3.121882]),
qatom(atom.C, [-2.381700, 4.518706, -0.793292]),
qatom(atom.C, [-6.323331, 4.890154, -1.786569]),
qatom(atom.C, [-8.555163, 3.994764, 1.511038]),
qatom(atom.C, [-5.988516, 3.069273, 4.544794]),
qatom(atom.C, [-3.194475, 3.133270, 4.102905]),
qatom(atom.C, [-1.727191, 4.152486, 0.433780]),
qatom(atom.C, [-4.903277, 4.922582, -2.010539]),
qatom(atom.C, [-8.327595, 4.381171, 0.144126]),
qatom(atom.C, [-7.270432, 3.274639, 3.926650]),
qatom(atom.C, [-1.511408, 5.094844, 1.504743]),
qatom(atom.C, [-4.089167, 6.049209, -1.626112]),
qatom(atom.C, [-8.000504, 5.735411, -0.229455]),
qatom(atom.C, [-7.848432, 4.587139, 3.770046]),
qatom(atom.C, [-3.842001, 4.191512, 4.838025]),
qatom(atom.C, [-1.728622, 4.726903, 2.805222]),
qatom(atom.C, [-2.869392, 5.854162, -1.036823]),
qatom(atom.C, [-7.030513, 5.981452, -1.163253]),
qatom(atom.C, [-8.470621, 4.935439, 2.601455]),
qatom(atom.C, [-5.193743, 4.160891, 5.051891]),
qatom(atom.H, [-1.871872, -4.568455, 0.611688]),
qatom(atom.H, [-2.627104, -3.349279, -3.592066]),
qatom(atom.H, [-7.021189, -3.082747, -4.175719]),
qatom(atom.H, [-8.999871, -4.137220, -0.338164]),
qatom(atom.H, [-5.802781, -5.055956, 2.615217]),
qatom(atom.H, [-3.597098, -5.005279, 2.270621]),
qatom(atom.H, [-1.518324, -3.966650, -1.515791]),
qatom(atom.H, [-4.618429, -3.029330, -4.552906]),
qatom(atom.H, [-8.613292, -3.484087, -2.650958]),
qatom(atom.H, [-7.970153, -4.709453, 1.568361]),
qatom(atom.H, [-1.301572, 6.141601, 1.274593]),
qatom(atom.H, [-4.498713, 7.060345, -1.678814]),
qatom(atom.H, [-8.429640, 6.572843, 0.324767]),
qatom(atom.H, [-7.674390, 5.353665, 4.528544]),
qatom(atom.H, [-3.280265, 5.087121, 5.112196]),
qatom(atom.H, [-1.688152, 5.488450, 3.587458]),
qatom(atom.H, [-2.331273, 6.713826, -0.631913]),
qatom(atom.H, [-6.704377, 7.009666, -1.334189]),
qatom(atom.H, [-8.783173, 5.971038, 2.452260]),
qatom(atom.H, [-5.683060, 5.033707, 5.489403]),
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
qatom(atom.C, [-2.300974, -3.731013, 1.165922]),
qatom(atom.C, [-2.453048, -2.582743, -2.833581]),
qatom(atom.C, [-6.459486, -2.187114, -3.901559]),
qatom(atom.C, [-8.790078, -3.090444, -0.568267]),
qatom(atom.C, [-6.212307, -4.044809, 2.562582]),
qatom(atom.C, [-3.270968, -3.977055, 2.099731]),
qatom(atom.C, [-1.830855, -2.931044, -1.664985]),
qatom(atom.C, [-5.107735, -2.156494, -4.115422]),
qatom(atom.C, [-8.572858, -2.722501, -1.868757]),
qatom(atom.C, [-7.432095, -3.849759, 1.973291]),
qatom(atom.C, [-1.746303, -1.990372, -0.574578]),
qatom(atom.C, [-4.312968, -1.064880, -3.608339]),
qatom(atom.C, [-8.126327, -1.387648, -2.185419]),
qatom(atom.C, [-7.919794, -2.514320, 1.729776]),
qatom(atom.C, [-3.978136, -2.885768, 2.723052]),
qatom(atom.C, [-1.973876, -2.376784, 0.792351]),
qatom(atom.C, [-3.031035, -1.270248, -2.990189]),
qatom(atom.C, [-7.107011, -1.128874, -3.166457]),
qatom(atom.C, [-8.574313, -2.148095, 0.502687]),
qatom(atom.C, [-5.398209, -2.918197, 2.947020]),
qatom(atom.C, [-2.303776, -1.360336, 1.734060]),
qatom(atom.C, [-2.517755, -0.244515, -2.145501]),
qatom(atom.C, [-6.425384, 0.120835, -3.117704]),
qatom(atom.C, [-8.628383, -0.767963, 0.154309]),
qatom(atom.C, [-6.077215, -1.683342, 3.152582]),
qatom(atom.C, [-3.325754, -1.619851, 2.718063]),
qatom(atom.C, [-1.862728, -0.611694, -0.913848]),
qatom(atom.C, [-5.001421, 0.153389, -3.343148]),
qatom(atom.C, [-8.399556, -0.380231, -1.216194]),
qatom(atom.C, [-7.362837, -1.477671, 2.532606]),
qatom(atom.C, [-1.743990, 0.382068, 0.108376]),
qatom(atom.C, [-4.272358, 1.294189, -2.881351]),
qatom(atom.C, [-8.030002, 0.976161, -1.480041]),
qatom(atom.C, [-7.828913, -0.134056, 2.379452]),
qatom(atom.C, [-3.944899, -0.500289, 3.357571]),
qatom(atom.C, [-1.968665, 0.001646, 1.453488]),
qatom(atom.C, [-3.010306, 1.092355, -2.273485]),
qatom(atom.C, [-7.026943, 1.230927, -2.445776]),
qatom(atom.C, [-8.471926, 0.226317, 1.170801]),
qatom(atom.C, [-5.342525, -0.532218, 3.578488]),
qatom(atom.C, [-2.271472, 1.028230, 2.416511]),
qatom(atom.C, [-2.472564, 2.138450, -1.442992]),
qatom(atom.C, [-6.356588, 2.504683, -2.421108]),
qatom(atom.C, [-8.557498, 1.622324, 0.828095]),
qatom(atom.C, [-6.029123, 0.710201, 3.817826]),
qatom(atom.C, [-3.274538, 0.773463, 3.382251]),
qatom(atom.C, [-1.829547, 1.778074, -0.234333]),
qatom(atom.C, [-4.958954, 2.536612, -2.642029]),
qatom(atom.C, [-8.332822, 2.002748, -0.517025]),
qatom(atom.C, [-7.291182, 0.912037, 3.209956]),
qatom(atom.C, [-1.673098, 2.772348, 0.782154]),
qatom(atom.C, [-4.224267, 3.687727, -2.216120]),
qatom(atom.C, [-7.997708, 3.364720, -0.797595]),
qatom(atom.C, [-7.783727, 2.248899, 3.081968]),
qatom(atom.C, [-3.876096, 1.883550, 4.054170]),
qatom(atom.C, [-1.901924, 2.384615, 2.152661]),
qatom(atom.C, [-2.938642, 3.482056, -1.596142]),
qatom(atom.C, [-6.975727, 3.624237, -1.781599]),
qatom(atom.C, [-8.438754, 2.616079, 1.850314]),
qatom(atom.C, [-5.300061, 1.850995, 4.279616]),
qatom(atom.C, [-2.175171, 3.392038, 3.121882]),
qatom(atom.C, [-2.381700, 4.518706, -0.793292]),
qatom(atom.C, [-6.323331, 4.890154, -1.786569]),
qatom(atom.C, [-8.555163, 3.994764, 1.511038]),
qatom(atom.C, [-5.988516, 3.069273, 4.544794]),
qatom(atom.C, [-3.194475, 3.133270, 4.102905]),
qatom(atom.C, [-1.727191, 4.152486, 0.433780]),
qatom(atom.C, [-4.903277, 4.922582, -2.010539]),
qatom(atom.C, [-8.327595, 4.381171, 0.144126]),
qatom(atom.C, [-7.270432, 3.274639, 3.926650]),
qatom(atom.C, [-1.511408, 5.094844, 1.504743]),
qatom(atom.C, [-4.089167, 6.049209, -1.626112]),
qatom(atom.C, [-8.000504, 5.735411, -0.229455]),
qatom(atom.C, [-7.848432, 4.587139, 3.770046]),
qatom(atom.C, [-3.842001, 4.191512, 4.838025]),
qatom(atom.C, [-1.728622, 4.726903, 2.805222]),
qatom(atom.C, [-2.869392, 5.854162, -1.036823]),
qatom(atom.C, [-7.030513, 5.981452, -1.163253]),
qatom(atom.C, [-8.470621, 4.935439, 2.601455]),
qatom(atom.C, [-5.193743, 4.160891, 5.051891]),
qatom(atom.H, [-1.871872, -4.568455, 0.611688]),
qatom(atom.H, [-2.627104, -3.349279, -3.592066]),
qatom(atom.H, [-7.021189, -3.082747, -4.175719]),
qatom(atom.H, [-8.999871, -4.137220, -0.338164]),
qatom(atom.H, [-5.802781, -5.055956, 2.615217]),
qatom(atom.H, [-3.597098, -5.005279, 2.270621]),
qatom(atom.H, [-1.518324, -3.966650, -1.515791]),
qatom(atom.H, [-4.618429, -3.029330, -4.552906]),
qatom(atom.H, [-8.613292, -3.484087, -2.650958]),
qatom(atom.H, [-7.970153, -4.709453, 1.568361]),
qatom(atom.H, [-1.301572, 6.141601, 1.274593]),
qatom(atom.H, [-4.498713, 7.060345, -1.678814]),
qatom(atom.H, [-8.429640, 6.572843, 0.324767]),
qatom(atom.H, [-7.674390, 5.353665, 4.528544]),
qatom(atom.H, [-3.280265, 5.087121, 5.112196]),
qatom(atom.H, [-1.688152, 5.488450, 3.587458]),
qatom(atom.H, [-2.331273, 6.713826, -0.631913]),
qatom(atom.H, [-6.704377, 7.009666, -1.334189]),
qatom(atom.H, [-8.783173, 5.971038, 2.452260]),
qatom(atom.H, [-5.683060, 5.033707, 5.489403]),
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
# orig frozen ... 80.00
# orig closed ... 170.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [250]
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
icmr.frozen = [80]
icmr.closed = [170]
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

