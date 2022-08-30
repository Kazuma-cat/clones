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
qatom(atom.Co, [-0.9277729, 0.0805031, -0.8561488]),
qatom(atom.C, [0.4265030, 1.6523316, 1.1027855]),
qatom(atom.C, [0.0281739, 2.4224724, 2.4165995]),
qatom(atom.C, [-1.0022402, 1.4443501, 3.0801412]),
qatom(atom.C, [-1.5804059, 0.7398974, 1.8780538]),
qatom(atom.C, [-2.8309111, 0.0406520, 1.8489881]),
qatom(atom.C, [-3.0434376, -0.9325687, 0.8994039]),
qatom(atom.C, [-4.2199354, -1.9103777, 0.8224602]),
qatom(atom.C, [-3.5722711, -3.0540525, -0.0194319]),
qatom(atom.C, [-2.6248730, -2.2591399, -0.8622830]),
qatom(atom.C, [-2.2924287, -2.5641413, -2.1711145]),
qatom(atom.C, [-1.4371250, -1.8273147, -2.9691484]),
qatom(atom.C, [-1.2464310, -2.0576109, -4.4537679]),
qatom(atom.C, [0.1133556, -1.3467357, -4.6853053]),
qatom(atom.C, [0.1446133, -0.3417593, -3.5488608]),
qatom(atom.C, [0.9586118, 0.7723024, -3.5243931]),
qatom(atom.C, [1.0499397, 1.6008303, -2.3614808]),
qatom(atom.C, [1.8468023, 2.9013842, -2.2212166]),
qatom(atom.C, [1.8099475, 3.1253270, -0.6726045]),
qatom(atom.C, [0.5246009, 2.4156640, -0.2414727]),
qatom(atom.C, [1.6679524, 0.7676714, 1.2605719]),
qatom(atom.C, [1.2053604, 2.7443855, 3.3414963]),
qatom(atom.C, [-0.7291659, 3.7262936, 2.0495005]),
qatom(atom.C, [-1.1734088, 4.5128815, 3.2787938]),
qatom(atom.C, [-0.3782338, 0.4402692, 4.0796002]),
qatom(atom.C, [-1.3744584, -0.5498837, 4.7043723]),
qatom(atom.C, [-0.6265010, -1.6564357, 5.4283219]),
qatom(atom.C, [-3.8961661, 0.4375759, 2.8526784]),
qatom(atom.C, [-4.8361040, -2.4023746, 2.1365290]),
qatom(atom.C, [-5.3140168, -1.2071950, -0.0485053]),
qatom(atom.C, [-6.5502642, -2.0789548, -0.2591295]),
qatom(atom.C, [-2.8429314, -4.1513565, 0.7982545]),
qatom(atom.C, [-1.7513566, -3.7091195, 1.7817173]),
qatom(atom.C, [-0.3866717, -3.4326857, 1.1577552]),
qatom(atom.C, [-2.3528472, -1.2442199, -5.1760886]),
qatom(atom.C, [-1.3278575, -3.5184621, -4.9039901]),
qatom(atom.C, [1.3523217, -2.2752463, -4.6725743]),
qatom(atom.C, [1.6211320, -3.0027257, -3.3461796]),
qatom(atom.C, [2.4452178, -2.1875533, -2.3591248]),
qatom(atom.C, [1.7749875, 1.0925373, -4.7587091]),
qatom(atom.C, [1.0608380, 4.0006177, -2.9741460]),
qatom(atom.C, [1.9525642, 4.6093499, -0.2973440]),
qatom(atom.C, [2.5697224, 4.9189710, 1.0601976]),
qatom(atom.C, [3.3193383, 2.8879608, -2.6921785]),
qatom(atom.C, [4.0983210, 1.5899895, -2.4649134]),
qatom(atom.C, [4.6467666, 1.3374698, -1.0654833]),
qatom(atom.C, [5.5919510, -0.4325673, 0.3640619]),
qatom(atom.C, [5.0764722, -1.7702491, 0.8971864]),
qatom(atom.C, [5.9289775, -2.2774463, 2.0543099]),
qatom(atom.N, [-0.7743989, 0.7950721, 0.8464786]),
qatom(atom.N, [-2.2094081, -1.1514044, -0.1979500]),
qatom(atom.N, [-0.7145177, -0.7556392, -2.5403982]),
qatom(atom.N, [0.3560117, 1.3534216, -1.2714341]),
qatom(atom.N, [-0.4651440, 5.6443715, 3.5007580]),
qatom(atom.N, [-0.7551032, -1.7022634, 6.7749029]),
qatom(atom.N, [-7.7138236, -1.5742351, 0.2394966]),
qatom(atom.N, [0.5201067, -2.8838183, 1.9958533]),
qatom(atom.N, [2.0234131, -2.2146508, -1.0846081]),
qatom(atom.N, [3.7662205, 4.3413524, 1.3028990]),
qatom(atom.N, [4.8564247, 0.0292602, -0.8038494]),
qatom(atom.O, [-2.1012471, 4.1329135, 4.0007186]),
qatom(atom.O, [0.0762708, -2.4699767, 4.8158973]),
qatom(atom.O, [-6.4996290, -3.1680580, -0.8244533]),
qatom(atom.O, [-0.1366775, -3.7110172, -0.0254495]),
qatom(atom.O, [3.4662004, -1.5757994, -2.7306513]),
qatom(atom.O, [2.0175651, 5.6767567, 1.8693700]),
qatom(atom.O, [4.9440610, 2.2448631, -0.2673251]),
qatom(atom.O, [3.6811549, -1.6694021, 1.2898794]),
qatom(atom.C, [-2.3771894, 1.2474442, -1.4619199]),
qatom(atom.H, [-1.7526255, 2.0400242, 3.6093084]),
qatom(atom.H, [-4.3361745, -3.5448350, -0.6264898]),
qatom(atom.H, [-2.7621732, -3.4386060, -2.6063052]),
qatom(atom.H, [0.1009956, -0.8391377, -5.6546238]),
qatom(atom.H, [2.6585714, 2.5731435, -0.2652841]),
qatom(atom.H, [-0.3405929, 3.0836373, -0.3275189]),
qatom(atom.H, [2.5448525, 1.3748455, 1.5020072]),
qatom(atom.H, [1.8604911, 0.2345967, 0.3277449]),
qatom(atom.H, [1.5160074, 0.0278827, 2.0478195]),
qatom(atom.H, [1.7736251, 1.8503142, 3.6051780]),
qatom(atom.H, [1.8866260, 3.4615650, 2.8850260]),
qatom(atom.H, [0.8349424, 3.1923822, 4.2687225]),
qatom(atom.H, [-1.6299024, 3.4795650, 1.4761144]),
qatom(atom.H, [-0.0864746, 4.3589062, 1.4349684]),
qatom(atom.H, [0.4013840, -0.1472367, 3.5881982]),
qatom(atom.H, [0.0990334, 1.0106609, 4.8819829]),
qatom(atom.H, [-1.9476353, -1.0417226, 3.9127188]),
qatom(atom.H, [-2.0779231, -0.0304162, 5.3630299]),
qatom(atom.H, [-4.8753772, 0.4799740, 2.3693789]),
qatom(atom.H, [-3.9829096, -0.2446500, 3.7035248]),
qatom(atom.H, [-3.6873999, 1.4349097, 3.2458056]),
qatom(atom.H, [-5.4909939, -1.6539178, 2.5859800]),
qatom(atom.H, [-4.0771333, -2.6772879, 2.8724136]),
qatom(atom.H, [-5.4451629, -3.2878333, 1.9310195]),
qatom(atom.H, [-5.5814018, -0.2534141, 0.4180296]),
qatom(atom.H, [-4.8936990, -0.9878035, -1.0358852]),
qatom(atom.H, [-2.3995774, -4.8533323, 0.0850108]),
qatom(atom.H, [-3.6086998, -4.7022711, 1.3534778]),
qatom(atom.H, [-2.0486082, -2.8286186, 2.3606051]),
qatom(atom.H, [-1.5979754, -4.5083432, 2.5184329]),
qatom(atom.H, [-3.3443689, -1.6231172, -4.9112720]),
qatom(atom.H, [-2.2241641, -1.3301577, -6.2601872]),
qatom(atom.H, [-2.2999486, -0.1853810, -4.9016088]),
qatom(atom.H, [-2.3451066, -3.9003373, -4.7724950]),
qatom(atom.H, [-1.0888257, -3.5946447, -5.9694276]),
qatom(atom.H, [-0.6475079, -4.1688992, -4.3496438]),
qatom(atom.H, [2.2433513, -1.6915803, -4.9222355]),
qatom(atom.H, [1.2213244, -3.0105568, -5.4723118]),
qatom(atom.H, [0.7005124, -3.3482403, -2.8669799]),
qatom(atom.H, [2.2224423, -3.8954631, -3.5583247]),
qatom(atom.H, [2.7549903, 0.6036491, -4.7419643]),
qatom(atom.H, [1.9408611, 2.1644605, -4.8603294]),
qatom(atom.H, [1.2592803, 0.7619886, -5.6621959]),
qatom(atom.H, [0.0599044, 4.1357967, -2.5515107]),
qatom(atom.H, [1.5889372, 4.9573625, -2.9247715]),
qatom(atom.H, [0.9452507, 3.7391537, -4.0289615]),
qatom(atom.H, [0.9938906, 5.1301745, -0.3469419]),
qatom(atom.H, [2.6126080, 5.0849980, -1.0343016]),
qatom(atom.H, [3.3660757, 3.1309996, -3.7568796]),
qatom(atom.H, [3.8353750, 3.7078505, -2.1756597]),
qatom(atom.H, [4.9874989, 1.6121714, -3.1096266]),
qatom(atom.H, [3.5274357, 0.7113637, -2.7758397]),
qatom(atom.H, [5.5180500, 0.3440721, 1.1338249]),
qatom(atom.H, [6.6577468, -0.5427504, 0.1202096]),
qatom(atom.H, [5.0639180, -2.5102074, 0.0892666]),
qatom(atom.H, [5.5231033, -3.2173723, 2.4359946]),
qatom(atom.H, [6.9602181, -2.4493939, 1.7295285]),
qatom(atom.H, [5.9476182, -1.5468985, 2.8719477]),
qatom(atom.H, [-0.6797558, 6.1983216, 4.3197538]),
qatom(atom.H, [0.3553762, 5.8699747, 2.9388958]),
qatom(atom.H, [-0.2644805, -2.4201480, 7.2930500]),
qatom(atom.H, [-1.3252863, -1.0414822, 7.2819196]),
qatom(atom.H, [-7.7754639, -0.6467969, 0.6322684]),
qatom(atom.H, [-8.5709867, -2.0877723, 0.0778614]),
qatom(atom.H, [0.3194207, -2.7447965, 2.9936527]),
qatom(atom.H, [1.4868267, -2.8128466, 1.6976327]),
qatom(atom.H, [2.6113360, -1.8174111, -0.3514665]),
qatom(atom.H, [1.2337660, -2.8076687, -0.7893359]),
qatom(atom.H, [4.2294365, 3.7065682, 0.6454668]),
qatom(atom.H, [4.2395605, 4.5778287, 2.1652746]),
qatom(atom.H, [4.5182253, -0.6518564, -1.5027397]),
qatom(atom.H, [3.6040721, -0.9267381, 1.9114674]),
qatom(atom.H, [-3.0545517, 0.6301832, -2.0547739]),
qatom(atom.H, [-2.8683225, 1.6329159, -0.5658026]),
qatom(atom.H, [-1.9506784, 2.0490004, -2.0672184]),
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

acene = [ i.new_basis() for i in geom]
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
# orig frozen ... 73.00
# orig closed ... 195.50
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [269]
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
icmr.frozen = [73]
icmr.closed = [196]
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
lct.TCutDOI_PAO = 1e-2
lct.UseNewDomain = True
lct.FormLVOs = True
lct.UseVM1_CD   = True
lct.UseVM12     = (not lct.UseVM1_CD)

lct.PrintPairDistDBG = True
lct.PrintMapsDBG     = True

lct.LocMet = "PSM"
lct.LocRecursive = True
lct.LocMeasure = True
hint.nroots = 1
hint.nconvroots = 1

# new PMNR scheme threshold (impl = sparse, locrec = True)
lct.PMMaxIt = 3
lct.PMStep = 0.01
lct.GThresh = 5.0e-3
lct.IterLevel = 2
hint.PM_trunc_thresh = 1e-1
hint.PM_AB_thresh = 1e-4
hint.PM_ang_thresh = 1e-6
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
lct.TCutDOI = 1e-3

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

