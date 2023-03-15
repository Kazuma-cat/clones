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
qatom(atom.H, [-3.71855584367113, 0.25227718446552, -1.54436441155366]),
qatom(atom.H, [-1.42906375461913, -3.52595004639265, -1.54507659967858]),
qatom(atom.H, [2.81397439735214, -2.38292923548007, -1.54815717064960]),
qatom(atom.H, [3.20924144008009, 2.02150712841796, -1.54219471551161]),
qatom(atom.H, [-0.88114912834593, 3.63343490232366, -1.54797875697755]),
qatom(atom.H, [-2.85671012716644, 2.34510983158902, -1.54516738681277]),
qatom(atom.H, [-3.17525225178509, -2.04474320902959, -1.54797643459861]),
qatom(atom.H, [0.92877571526124, -3.64865206775280, -1.54290957684771]),
qatom(atom.H, [3.70143990716213, -0.19796870390769, -1.54770727420229]),
qatom(atom.H, [1.40076086012485, 3.53930940495171, -1.54408123819544]),
qatom(atom.C, [-3.21984785247396, -1.54050510699759, -0.58462786489321]),
qatom(atom.C, [0.43030362092392, -3.53992258289616, -0.58176585465616]),
qatom(atom.C, [3.45644946514833, -0.63933684712729, -0.58419434014377]),
qatom(atom.C, [1.73224696798389, 3.15324753463633, -0.58235155186731]),
qatom(atom.C, [-2.39942119647749, 2.56338162818823, -0.58263529011859]),
qatom(atom.C, [-3.53057146429439, -0.22071454358049, -0.58298916730922]),
qatom(atom.C, [-0.92363219727948, -3.47060954311700, -0.58282881452684]),
qatom(atom.C, [2.94579735970839, -1.89600637053093, -0.58426131929943]),
qatom(atom.C, [2.77013348312452, 2.28172048193117, -0.58138278738508]),
qatom(atom.C, [-1.26399559970827, 3.30498148444026, -0.58409150267108]),
qatom(atom.C, [-3.45645225116627, 0.63933873592248, 0.58418387532520]),
qatom(atom.C, [-1.73224607161784, -3.15324448267956, 0.58234549099686]),
qatom(atom.C, [2.39942138537672, -2.56338252625865, 0.58262460033173]),
qatom(atom.C, [3.21984869126147, 1.54050571592321, 0.58462227212697]),
qatom(atom.C, [-0.43030562170778, 3.53992185971122, 0.58175838069912]),
qatom(atom.C, [-2.94579944300294, 1.89600744653809, 0.58424960428645]),
qatom(atom.C, [-2.77013196126808, -2.28171734690749, 0.58137682250621]),
qatom(atom.C, [1.26399649736564, -3.30498390319907, 0.58408268845393]),
qatom(atom.C, [3.53057091265208, 0.22071428303890, 0.58298156780149]),
qatom(atom.C, [0.92363043348759, 3.47060948483343, 0.58282297002882]),
qatom(atom.H, [-3.20923848311405, -2.02150278158557, 1.54218759066052]),
qatom(atom.H, [0.88115173066139, -3.63343697167657, 1.54796960071444]),
qatom(atom.H, [3.71855401060557, -0.25227972586125, 1.54435637527462]),
qatom(atom.H, [1.42906145323295, 3.52595053419479, 1.54507301587631]),
qatom(atom.H, [-2.81397871161911, 2.38293248369948, 1.54814491737697]),
qatom(atom.H, [-3.70144405366692, 0.19797291586015, 1.54769635382071]),
qatom(atom.H, [-1.40075970445106, -3.53930573294643, 1.54407562402296]),
qatom(atom.H, [2.85671268295984, -2.34511132136066, 1.54515736831912]),
qatom(atom.H, [3.17525343403010, 2.04474240706836, 1.54797245357364]),
qatom(atom.H, [-0.92877873106756, 3.64864760155353, 1.54290048570248]),
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
qatom(atom.H, [-3.71855584367113, 0.25227718446552, -1.54436441155366]),
qatom(atom.H, [-1.42906375461913, -3.52595004639265, -1.54507659967858]),
qatom(atom.H, [2.81397439735214, -2.38292923548007, -1.54815717064960]),
qatom(atom.H, [3.20924144008009, 2.02150712841796, -1.54219471551161]),
qatom(atom.H, [-0.88114912834593, 3.63343490232366, -1.54797875697755]),
qatom(atom.H, [-2.85671012716644, 2.34510983158902, -1.54516738681277]),
qatom(atom.H, [-3.17525225178509, -2.04474320902959, -1.54797643459861]),
qatom(atom.H, [0.92877571526124, -3.64865206775280, -1.54290957684771]),
qatom(atom.H, [3.70143990716213, -0.19796870390769, -1.54770727420229]),
qatom(atom.H, [1.40076086012485, 3.53930940495171, -1.54408123819544]),
qatom(atom.C, [-3.21984785247396, -1.54050510699759, -0.58462786489321]),
qatom(atom.C, [0.43030362092392, -3.53992258289616, -0.58176585465616]),
qatom(atom.C, [3.45644946514833, -0.63933684712729, -0.58419434014377]),
qatom(atom.C, [1.73224696798389, 3.15324753463633, -0.58235155186731]),
qatom(atom.C, [-2.39942119647749, 2.56338162818823, -0.58263529011859]),
qatom(atom.C, [-3.53057146429439, -0.22071454358049, -0.58298916730922]),
qatom(atom.C, [-0.92363219727948, -3.47060954311700, -0.58282881452684]),
qatom(atom.C, [2.94579735970839, -1.89600637053093, -0.58426131929943]),
qatom(atom.C, [2.77013348312452, 2.28172048193117, -0.58138278738508]),
qatom(atom.C, [-1.26399559970827, 3.30498148444026, -0.58409150267108]),
qatom(atom.C, [-3.45645225116627, 0.63933873592248, 0.58418387532520]),
qatom(atom.C, [-1.73224607161784, -3.15324448267956, 0.58234549099686]),
qatom(atom.C, [2.39942138537672, -2.56338252625865, 0.58262460033173]),
qatom(atom.C, [3.21984869126147, 1.54050571592321, 0.58462227212697]),
qatom(atom.C, [-0.43030562170778, 3.53992185971122, 0.58175838069912]),
qatom(atom.C, [-2.94579944300294, 1.89600744653809, 0.58424960428645]),
qatom(atom.C, [-2.77013196126808, -2.28171734690749, 0.58137682250621]),
qatom(atom.C, [1.26399649736564, -3.30498390319907, 0.58408268845393]),
qatom(atom.C, [3.53057091265208, 0.22071428303890, 0.58298156780149]),
qatom(atom.C, [0.92363043348759, 3.47060948483343, 0.58282297002882]),
qatom(atom.H, [-3.20923848311405, -2.02150278158557, 1.54218759066052]),
qatom(atom.H, [0.88115173066139, -3.63343697167657, 1.54796960071444]),
qatom(atom.H, [3.71855401060557, -0.25227972586125, 1.54435637527462]),
qatom(atom.H, [1.42906145323295, 3.52595053419479, 1.54507301587631]),
qatom(atom.H, [-2.81397871161911, 2.38293248369948, 1.54814491737697]),
qatom(atom.H, [-3.70144405366692, 0.19797291586015, 1.54769635382071]),
qatom(atom.H, [-1.40075970445106, -3.53930573294643, 1.54407562402296]),
qatom(atom.H, [2.85671268295984, -2.34511132136066, 1.54515736831912]),
qatom(atom.H, [3.17525343403010, 2.04474240706836, 1.54797245357364]),
qatom(atom.H, [-0.92877873106756, 3.64864760155353, 1.54290048570248]),
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
# orig frozen ... 20.00
# orig closed ... 50.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [70]
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
icmr.frozen = [20]
icmr.closed = [50]
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

