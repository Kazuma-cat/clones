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
qatom(atom.C, [1.8911201, -2.9337929, 1.7338849]),
qatom(atom.H, [1.9437169, -2.0232992, 2.3208960]),
qatom(atom.H, [2.5716215, -3.7500123, 1.9548764]),
qatom(atom.C, [0.9496426, -3.0351924, 0.5934139]),
qatom(atom.C, [1.5158964, -2.5772756, -0.7712266]),
qatom(atom.O, [-0.2134717, -2.1733783, 0.8395914]),
qatom(atom.C, [1.0874535, -1.1093198, -0.8297194]),
qatom(atom.C, [-0.3088578, -1.2016760, -0.1800554]),
qatom(atom.C, [-0.7441042, 1.2893547, -0.1860776]),
qatom(atom.C, [-1.3002496, 0.2591567, 1.6862569]),
qatom(atom.C, [-1.3072047, 2.1716118, 0.7418126]),
qatom(atom.H, [-1.4101548, -0.5650528, 2.3748599]),
qatom(atom.C, [-1.4131305, 3.5156867, 0.3312934]),
qatom(atom.C, [-0.4572516, 2.9083459, -1.6868762]),
qatom(atom.H, [-0.1193166, 3.2360676, -2.6667417]),
qatom(atom.N, [-0.7376900, 0.0598960, 0.4356272]),
qatom(atom.N, [-1.6482975, 1.5109146, 1.9106685]),
qatom(atom.N, [-0.2966357, 1.6020834, -1.4174735]),
qatom(atom.N, [-0.9803569, 3.8576395, -0.9022349]),
qatom(atom.N, [-1.9174076, 4.4836273, 1.1282283]),
qatom(atom.H, [-2.3245646, 4.2395034, 2.0184235]),
qatom(atom.H, [-2.0454496, 5.4103424, 0.7494687]),
qatom(atom.O, [0.8662724, -3.3038717, -1.8105581]),
qatom(atom.H, [0.8235189, -2.6827476, -2.5645335]),
qatom(atom.O, [1.0838952, -0.6645425, -2.1690939]),
qatom(atom.H, [0.6238214, 0.2218833, -2.1627752]),
qatom(atom.H, [2.6049565, -2.7011369, -0.8218214]),
qatom(atom.H, [1.7397928, -0.4958225, -0.1899633]),
qatom(atom.H, [0.5773688, -4.0602762, 0.4736626]),
qatom(atom.H, [-1.0549336, -1.4887167, -0.9338134]),
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
qatom(atom.C, [1.8911201, -2.9337929, 1.7338849]),
qatom(atom.H, [1.9437169, -2.0232992, 2.3208960]),
qatom(atom.H, [2.5716215, -3.7500123, 1.9548764]),
qatom(atom.C, [0.9496426, -3.0351924, 0.5934139]),
qatom(atom.C, [1.5158964, -2.5772756, -0.7712266]),
qatom(atom.O, [-0.2134717, -2.1733783, 0.8395914]),
qatom(atom.C, [1.0874535, -1.1093198, -0.8297194]),
qatom(atom.C, [-0.3088578, -1.2016760, -0.1800554]),
qatom(atom.C, [-0.7441042, 1.2893547, -0.1860776]),
qatom(atom.C, [-1.3002496, 0.2591567, 1.6862569]),
qatom(atom.C, [-1.3072047, 2.1716118, 0.7418126]),
qatom(atom.H, [-1.4101548, -0.5650528, 2.3748599]),
qatom(atom.C, [-1.4131305, 3.5156867, 0.3312934]),
qatom(atom.C, [-0.4572516, 2.9083459, -1.6868762]),
qatom(atom.H, [-0.1193166, 3.2360676, -2.6667417]),
qatom(atom.N, [-0.7376900, 0.0598960, 0.4356272]),
qatom(atom.N, [-1.6482975, 1.5109146, 1.9106685]),
qatom(atom.N, [-0.2966357, 1.6020834, -1.4174735]),
qatom(atom.N, [-0.9803569, 3.8576395, -0.9022349]),
qatom(atom.N, [-1.9174076, 4.4836273, 1.1282283]),
qatom(atom.H, [-2.3245646, 4.2395034, 2.0184235]),
qatom(atom.H, [-2.0454496, 5.4103424, 0.7494687]),
qatom(atom.O, [0.8662724, -3.3038717, -1.8105581]),
qatom(atom.H, [0.8235189, -2.6827476, -2.5645335]),
qatom(atom.O, [1.0838952, -0.6645425, -2.1690939]),
qatom(atom.H, [0.6238214, 0.2218833, -2.1627752]),
qatom(atom.H, [2.6049565, -2.7011369, -0.8218214]),
qatom(atom.H, [1.7397928, -0.4958225, -0.1899633]),
qatom(atom.H, [0.5773688, -4.0602762, 0.4736626]),
qatom(atom.H, [-1.0549336, -1.4887167, -0.9338134]),
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
# orig frozen ... 18.00
# orig closed ... 47.50
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [66]
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
icmr.frozen = [18]
icmr.closed = [48]
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

