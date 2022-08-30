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
qatom(atom.Co, [-0.92777, 0.08050, -0.85615]),
qatom(atom.C, [0.42650, 1.65233, 1.10279]),
qatom(atom.C, [0.02817, 2.42247, 2.41660]),
qatom(atom.C, [-1.00224, 1.44435, 3.08014]),
qatom(atom.C, [-1.58041, 0.73990, 1.87805]),
qatom(atom.C, [-2.83091, 0.04065, 1.84899]),
qatom(atom.C, [-3.04344, -0.93257, 0.89940]),
qatom(atom.C, [-4.21994, -1.91038, 0.82246]),
qatom(atom.C, [-3.57227, -3.05405, -0.01943]),
qatom(atom.C, [-2.62487, -2.25914, -0.86228]),
qatom(atom.C, [-2.29243, -2.56414, -2.17111]),
qatom(atom.C, [-1.43712, -1.82731, -2.96915]),
qatom(atom.C, [-1.24643, -2.05761, -4.45377]),
qatom(atom.C, [0.11336, -1.34674, -4.68531]),
qatom(atom.C, [0.14461, -0.34176, -3.54886]),
qatom(atom.C, [0.95861, 0.77230, -3.52439]),
qatom(atom.C, [1.04994, 1.60083, -2.36148]),
qatom(atom.C, [1.84680, 2.90138, -2.22122]),
qatom(atom.C, [1.80995, 3.12533, -0.67260]),
qatom(atom.C, [0.52460, 2.41566, -0.24147]),
qatom(atom.C, [1.66795, 0.76767, 1.26057]),
qatom(atom.C, [1.20536, 2.74439, 3.34150]),
qatom(atom.C, [-0.72917, 3.72629, 2.04950]),
qatom(atom.C, [-1.17341, 4.51288, 3.27879]),
qatom(atom.C, [-0.37823, 0.44027, 4.07960]),
qatom(atom.C, [-1.37446, -0.54988, 4.70437]),
qatom(atom.C, [-0.62650, -1.65644, 5.42832]),
qatom(atom.C, [-3.89617, 0.43758, 2.85268]),
qatom(atom.C, [-4.83610, -2.40237, 2.13653]),
qatom(atom.C, [-5.31402, -1.20720, -0.04851]),
qatom(atom.C, [-6.55026, -2.07895, -0.25913]),
qatom(atom.C, [-2.84293, -4.15136, 0.79825]),
qatom(atom.C, [-1.75136, -3.70912, 1.78172]),
qatom(atom.C, [-0.38667, -3.43269, 1.15776]),
qatom(atom.C, [-2.35285, -1.24422, -5.17609]),
qatom(atom.C, [-1.32786, -3.51846, -4.90399]),
qatom(atom.C, [1.35232, -2.27525, -4.67257]),
qatom(atom.C, [1.62113, -3.00273, -3.34618]),
qatom(atom.C, [2.44522, -2.18755, -2.35912]),
qatom(atom.C, [1.77499, 1.09254, -4.75871]),
qatom(atom.C, [1.06084, 4.00062, -2.97415]),
qatom(atom.C, [1.95256, 4.60935, -0.29734]),
qatom(atom.C, [2.56972, 4.91897, 1.06020]),
qatom(atom.C, [3.31934, 2.88796, -2.69218]),
qatom(atom.C, [4.09832, 1.58999, -2.46491]),
qatom(atom.C, [4.64677, 1.33747, -1.06548]),
qatom(atom.C, [5.59195, -0.43257, 0.36406]),
qatom(atom.C, [5.07647, -1.77025, 0.89719]),
qatom(atom.C, [5.92898, -2.27745, 2.05431]),
qatom(atom.N, [-0.77440, 0.79507, 0.84648]),
qatom(atom.N, [-2.20941, -1.15140, -0.19795]),
qatom(atom.N, [-0.71452, -0.75564, -2.54040]),
qatom(atom.N, [0.35601, 1.35342, -1.27143]),
qatom(atom.N, [-0.46514, 5.64437, 3.50076]),
qatom(atom.N, [-0.75510, -1.70226, 6.77490]),
qatom(atom.N, [-7.71382, -1.57424, 0.23950]),
qatom(atom.N, [0.52011, -2.88382, 1.99585]),
qatom(atom.N, [2.02341, -2.21465, -1.08461]),
qatom(atom.N, [3.76622, 4.34135, 1.30290]),
qatom(atom.N, [4.85642, 0.02926, -0.80385]),
qatom(atom.O, [-2.10125, 4.13291, 4.00072]),
qatom(atom.O, [0.07627, -2.46998, 4.81590]),
qatom(atom.O, [-6.49963, -3.16806, -0.82445]),
qatom(atom.O, [-0.13668, -3.71102, -0.02545]),
qatom(atom.O, [3.46620, -1.57580, -2.73065]),
qatom(atom.O, [2.01757, 5.67676, 1.86937]),
qatom(atom.O, [4.94406, 2.24486, -0.26733]),
qatom(atom.O, [3.68115, -1.66940, 1.28988]),
qatom(atom.C, [-2.37719, 1.24744, -1.46192]),
qatom(atom.H, [-1.75263, 2.04002, 3.60931]),
qatom(atom.H, [-4.33617, -3.54483, -0.62649]),
qatom(atom.H, [-2.76217, -3.43861, -2.60631]),
qatom(atom.H, [0.10100, -0.83914, -5.65462]),
qatom(atom.H, [2.65857, 2.57314, -0.26528]),
qatom(atom.H, [-0.34059, 3.08364, -0.32752]),
qatom(atom.H, [2.54485, 1.37485, 1.50201]),
qatom(atom.H, [1.86049, 0.23460, 0.32774]),
qatom(atom.H, [1.51601, 0.02788, 2.04782]),
qatom(atom.H, [1.77363, 1.85031, 3.60518]),
qatom(atom.H, [1.88663, 3.46156, 2.88503]),
qatom(atom.H, [0.83494, 3.19238, 4.26872]),
qatom(atom.H, [-1.62990, 3.47957, 1.47611]),
qatom(atom.H, [-0.08647, 4.35891, 1.43497]),
qatom(atom.H, [0.40138, -0.14724, 3.58820]),
qatom(atom.H, [0.09903, 1.01066, 4.88198]),
qatom(atom.H, [-1.94764, -1.04172, 3.91272]),
qatom(atom.H, [-2.07792, -0.03042, 5.36303]),
qatom(atom.H, [-4.87538, 0.47997, 2.36938]),
qatom(atom.H, [-3.98291, -0.24465, 3.70352]),
qatom(atom.H, [-3.68740, 1.43491, 3.24581]),
qatom(atom.H, [-5.49099, -1.65392, 2.58598]),
qatom(atom.H, [-4.07713, -2.67729, 2.87241]),
qatom(atom.H, [-5.44516, -3.28783, 1.93102]),
qatom(atom.H, [-5.58140, -0.25341, 0.41803]),
qatom(atom.H, [-4.89370, -0.98780, -1.03589]),
qatom(atom.H, [-2.39958, -4.85333, 0.08501]),
qatom(atom.H, [-3.60870, -4.70227, 1.35348]),
qatom(atom.H, [-2.04861, -2.82862, 2.36061]),
qatom(atom.H, [-1.59798, -4.50834, 2.51843]),
qatom(atom.H, [-3.34437, -1.62312, -4.91127]),
qatom(atom.H, [-2.22416, -1.33016, -6.26019]),
qatom(atom.H, [-2.29995, -0.18538, -4.90161]),
qatom(atom.H, [-2.34511, -3.90034, -4.77250]),
qatom(atom.H, [-1.08883, -3.59464, -5.96943]),
qatom(atom.H, [-0.64751, -4.16890, -4.34964]),
qatom(atom.H, [2.24335, -1.69158, -4.92224]),
qatom(atom.H, [1.22132, -3.01056, -5.47231]),
qatom(atom.H, [0.70051, -3.34824, -2.86698]),
qatom(atom.H, [2.22244, -3.89546, -3.55832]),
qatom(atom.H, [2.75499, 0.60365, -4.74196]),
qatom(atom.H, [1.94086, 2.16446, -4.86033]),
qatom(atom.H, [1.25928, 0.76199, -5.66220]),
qatom(atom.H, [0.05990, 4.13580, -2.55151]),
qatom(atom.H, [1.58894, 4.95736, -2.92477]),
qatom(atom.H, [0.94525, 3.73915, -4.02896]),
qatom(atom.H, [0.99389, 5.13017, -0.34694]),
qatom(atom.H, [2.61261, 5.08500, -1.03430]),
qatom(atom.H, [3.36608, 3.13100, -3.75688]),
qatom(atom.H, [3.83537, 3.70785, -2.17566]),
qatom(atom.H, [4.98750, 1.61217, -3.10963]),
qatom(atom.H, [3.52744, 0.71136, -2.77584]),
qatom(atom.H, [5.51805, 0.34407, 1.13382]),
qatom(atom.H, [6.65775, -0.54275, 0.12021]),
qatom(atom.H, [5.06392, -2.51021, 0.08927]),
qatom(atom.H, [5.52310, -3.21737, 2.43599]),
qatom(atom.H, [6.96022, -2.44939, 1.72953]),
qatom(atom.H, [5.94762, -1.54690, 2.87195]),
qatom(atom.H, [-0.67976, 6.19832, 4.31975]),
qatom(atom.H, [0.35538, 5.86997, 2.93890]),
qatom(atom.H, [-0.26448, -2.42015, 7.29305]),
qatom(atom.H, [-1.32529, -1.04148, 7.28192]),
qatom(atom.H, [-7.77546, -0.64680, 0.63227]),
qatom(atom.H, [-8.57099, -2.08777, 0.07786]),
qatom(atom.H, [0.31942, -2.74480, 2.99365]),
qatom(atom.H, [1.48683, -2.81285, 1.69763]),
qatom(atom.H, [2.61134, -1.81741, -0.35147]),
qatom(atom.H, [1.23377, -2.80767, -0.78934]),
qatom(atom.H, [4.22944, 3.70657, 0.64547]),
qatom(atom.H, [4.23956, 4.57783, 2.16527]),
qatom(atom.H, [4.51823, -0.65186, -1.50274]),
qatom(atom.H, [3.60407, -0.92674, 1.91147]),
qatom(atom.H, [-3.05455, 0.63018, -2.05477]),
qatom(atom.H, [-2.86832, 1.63292, -0.56580]),
qatom(atom.H, [-1.95068, 2.04900, -2.06722]),
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

