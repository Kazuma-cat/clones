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
qatom(atom.C, [-2.025837, -8.392724, -6.134865]),
qatom(atom.C, [0.947823, -5.675850, -7.054611]),
qatom(atom.C, [0.430575, -2.343166, -4.661571]),
qatom(atom.C, [-2.863751, -2.992274, -2.257719]),
qatom(atom.C, [-4.377025, -6.729772, -3.171603]),
qatom(atom.C, [-3.062695, -8.362914, -5.241192]),
qatom(atom.C, [0.264730, -6.856913, -7.170217]),
qatom(atom.C, [1.041371, -3.101405, -5.623396]),
qatom(atom.C, [-1.799709, -2.278014, -2.738556]),
qatom(atom.C, [-4.332917, -5.533468, -2.507126]),
qatom(atom.C, [0.443334, -7.893790, -6.190559]),
qatom(atom.C, [1.894094, -4.195623, -5.247749]),
qatom(atom.C, [-0.463451, -2.603880, -2.320630]),
qatom(atom.C, [-3.375831, -5.325726, -1.455207]),
qatom(atom.C, [-2.818094, -8.591399, -3.843087]),
qatom(atom.C, [-0.687022, -8.652450, -5.679888]),
qatom(atom.C, [1.847531, -5.466080, -5.953357]),
qatom(atom.C, [0.637834, -2.636185, -3.269993]),
qatom(atom.C, [-2.650861, -4.071340, -1.332074]),
qatom(atom.C, [-3.466387, -7.785322, -2.821512]),
qatom(atom.C, [-0.543182, -9.340799, -4.448985]),
qatom(atom.C, [2.369212, -6.618935, -5.314408]),
qatom(atom.C, [1.811464, -3.353245, -2.926513]),
qatom(atom.C, [-1.449984, -4.050862, -0.579033]),
qatom(atom.C, [-2.900744, -7.749052, -1.521852]),
qatom(atom.C, [-1.644484, -9.308491, -3.499611]),
qatom(atom.C, [1.644230, -7.873336, -5.437547]),
qatom(atom.C, [2.459766, -4.159334, -3.948100]),
qatom(atom.C, [-0.319610, -3.292192, -1.089708]),
qatom(atom.C, [-2.854179, -6.478579, -0.816231]),
qatom(atom.C, [1.857113, -8.952387, -4.511914]),
qatom(atom.C, [3.370383, -5.214874, -3.598015]),
qatom(atom.C, [1.019188, -3.551915, -0.634740]),
qatom(atom.C, [-1.954479, -6.268807, 0.285004]),
qatom(atom.C, [-1.437223, -9.601500, -2.108050]),
qatom(atom.C, [0.793060, -9.666657, -4.031068]),
qatom(atom.C, [3.326279, -6.411193, -4.262499]),
qatom(atom.C, [2.056056, -3.581726, -1.528427]),
qatom(atom.C, [-1.271381, -5.087727, 0.400607]),
qatom(atom.C, [-2.048026, -8.843253, -1.146214]),
qatom(atom.H, [-2.203251, -8.078036, -7.165203]),
qatom(atom.H, [0.697376, -4.848711, -7.721968]),
qatom(atom.H, [-0.321052, -1.609868, -4.961101]),
qatom(atom.H, [-3.852453, -2.827963, -2.691015]),
qatom(atom.H, [-5.008755, -6.821363, -4.057508]),
qatom(atom.H, [-4.044881, -8.025053, -5.577169]),
qatom(atom.H, [-0.516729, -6.946551, -7.927752]),
qatom(atom.H, [0.762813, -2.956434, -6.669483]),
qatom(atom.H, [-1.962189, -1.558980, -3.544215]),
qatom(atom.H, [-4.930238, -4.697228, -2.875676]),
qatom(atom.H, [2.845780, -9.116721, -4.078546]),
qatom(atom.H, [4.002094, -5.123362, -2.712086]),
qatom(atom.H, [1.196649, -3.866653, 0.395574]),
qatom(atom.H, [-1.703969, -7.095931, 0.952356]),
qatom(atom.H, [-0.685574, -10.334754, -1.808468]),
qatom(atom.H, [0.955583, -10.385650, -3.225381]),
qatom(atom.H, [3.923582, -7.247414, -3.893878]),
qatom(atom.H, [3.038207, -3.919636, -1.192398]),
qatom(atom.H, [-0.489906, -4.998172, 1.158137]),
qatom(atom.H, [-1.769402, -8.988235, -0.100145]),
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
qatom(atom.C, [-2.025837, -8.392724, -6.134865]),
qatom(atom.C, [0.947823, -5.675850, -7.054611]),
qatom(atom.C, [0.430575, -2.343166, -4.661571]),
qatom(atom.C, [-2.863751, -2.992274, -2.257719]),
qatom(atom.C, [-4.377025, -6.729772, -3.171603]),
qatom(atom.C, [-3.062695, -8.362914, -5.241192]),
qatom(atom.C, [0.264730, -6.856913, -7.170217]),
qatom(atom.C, [1.041371, -3.101405, -5.623396]),
qatom(atom.C, [-1.799709, -2.278014, -2.738556]),
qatom(atom.C, [-4.332917, -5.533468, -2.507126]),
qatom(atom.C, [0.443334, -7.893790, -6.190559]),
qatom(atom.C, [1.894094, -4.195623, -5.247749]),
qatom(atom.C, [-0.463451, -2.603880, -2.320630]),
qatom(atom.C, [-3.375831, -5.325726, -1.455207]),
qatom(atom.C, [-2.818094, -8.591399, -3.843087]),
qatom(atom.C, [-0.687022, -8.652450, -5.679888]),
qatom(atom.C, [1.847531, -5.466080, -5.953357]),
qatom(atom.C, [0.637834, -2.636185, -3.269993]),
qatom(atom.C, [-2.650861, -4.071340, -1.332074]),
qatom(atom.C, [-3.466387, -7.785322, -2.821512]),
qatom(atom.C, [-0.543182, -9.340799, -4.448985]),
qatom(atom.C, [2.369212, -6.618935, -5.314408]),
qatom(atom.C, [1.811464, -3.353245, -2.926513]),
qatom(atom.C, [-1.449984, -4.050862, -0.579033]),
qatom(atom.C, [-2.900744, -7.749052, -1.521852]),
qatom(atom.C, [-1.644484, -9.308491, -3.499611]),
qatom(atom.C, [1.644230, -7.873336, -5.437547]),
qatom(atom.C, [2.459766, -4.159334, -3.948100]),
qatom(atom.C, [-0.319610, -3.292192, -1.089708]),
qatom(atom.C, [-2.854179, -6.478579, -0.816231]),
qatom(atom.C, [1.857113, -8.952387, -4.511914]),
qatom(atom.C, [3.370383, -5.214874, -3.598015]),
qatom(atom.C, [1.019188, -3.551915, -0.634740]),
qatom(atom.C, [-1.954479, -6.268807, 0.285004]),
qatom(atom.C, [-1.437223, -9.601500, -2.108050]),
qatom(atom.C, [0.793060, -9.666657, -4.031068]),
qatom(atom.C, [3.326279, -6.411193, -4.262499]),
qatom(atom.C, [2.056056, -3.581726, -1.528427]),
qatom(atom.C, [-1.271381, -5.087727, 0.400607]),
qatom(atom.C, [-2.048026, -8.843253, -1.146214]),
qatom(atom.H, [-2.203251, -8.078036, -7.165203]),
qatom(atom.H, [0.697376, -4.848711, -7.721968]),
qatom(atom.H, [-0.321052, -1.609868, -4.961101]),
qatom(atom.H, [-3.852453, -2.827963, -2.691015]),
qatom(atom.H, [-5.008755, -6.821363, -4.057508]),
qatom(atom.H, [-4.044881, -8.025053, -5.577169]),
qatom(atom.H, [-0.516729, -6.946551, -7.927752]),
qatom(atom.H, [0.762813, -2.956434, -6.669483]),
qatom(atom.H, [-1.962189, -1.558980, -3.544215]),
qatom(atom.H, [-4.930238, -4.697228, -2.875676]),
qatom(atom.H, [2.845780, -9.116721, -4.078546]),
qatom(atom.H, [4.002094, -5.123362, -2.712086]),
qatom(atom.H, [1.196649, -3.866653, 0.395574]),
qatom(atom.H, [-1.703969, -7.095931, 0.952356]),
qatom(atom.H, [-0.685574, -10.334754, -1.808468]),
qatom(atom.H, [0.955583, -10.385650, -3.225381]),
qatom(atom.H, [3.923582, -7.247414, -3.893878]),
qatom(atom.H, [3.038207, -3.919636, -1.192398]),
qatom(atom.H, [-0.489906, -4.998172, 1.158137]),
qatom(atom.H, [-1.769402, -8.988235, -0.100145]),
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
# orig frozen ... 40.00
# orig closed ... 90.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [130]
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
icmr.frozen = [40]
icmr.closed = [90]
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

