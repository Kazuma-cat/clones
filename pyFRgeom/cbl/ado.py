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
qatom(atom.C, [78.0923158, -56.7951656, 5.4370953]),
qatom(atom.C, [78.4075756, -58.2648255, 5.7995907]),
qatom(atom.C, [77.0166851, -58.7839286, 6.1585813]),
qatom(atom.C, [76.4304593, -57.5760736, 6.9067200]),
qatom(atom.C, [76.7727923, -57.5400357, 8.3515338]),
qatom(atom.C, [82.6085586, -54.9619487, 5.3771255]),
qatom(atom.C, [81.2381032, -54.9887109, 5.7227741]),
qatom(atom.N, [80.4249348, -54.1325741, 6.4516291]),
qatom(atom.C, [79.2358594, -54.7111307, 6.4286412]),
qatom(atom.N, [79.2259421, -55.9028672, 5.7333274]),
qatom(atom.C, [80.5081660, -56.0900936, 5.2687581]),
qatom(atom.N, [80.9782004, -57.1239008, 4.5412669]),
qatom(atom.C, [82.2871761, -56.9865084, 4.2759396]),
qatom(atom.N, [83.1048049, -55.9901905, 4.6413114]),
qatom(atom.H, [77.8660812, -56.7011055, 4.3682360]),
qatom(atom.H, [79.0482819, -58.2867444, 6.6921166]),
qatom(atom.H, [77.0476212, -59.6802244, 6.7880307]),
qatom(atom.H, [75.3435460, -57.5456049, 6.7437497]),
qatom(atom.H, [77.2824533, -56.6792132, 8.7696559]),
qatom(atom.H, [76.4175022, -58.3282228, 9.0086592]),
qatom(atom.H, [78.3389131, -54.3306900, 6.8943851]),
qatom(atom.H, [82.7409510, -57.7837314, 3.6924885]),
qatom(atom.H, [84.4145667, -54.0043808, 5.4745795]),
qatom(atom.H, [83.1102512, -53.1954089, 6.2961768]),
qatom(atom.N, [83.4395643, -53.9711178, 5.7395785]),
qatom(atom.O, [76.9794498, -56.4032377, 6.2133584]),
qatom(atom.O, [78.9676470, -59.0104368, 4.7329093]),
qatom(atom.H, [79.7885087, -58.5069545, 4.4641360]),
qatom(atom.O, [76.2585830, -59.0180113, 4.9671631]),
qatom(atom.H, [76.8937011, -59.3625282, 4.3099344]),
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
qatom(atom.C, [78.0923158, -56.7951656, 5.4370953]),
qatom(atom.C, [78.4075756, -58.2648255, 5.7995907]),
qatom(atom.C, [77.0166851, -58.7839286, 6.1585813]),
qatom(atom.C, [76.4304593, -57.5760736, 6.9067200]),
qatom(atom.C, [76.7727923, -57.5400357, 8.3515338]),
qatom(atom.C, [82.6085586, -54.9619487, 5.3771255]),
qatom(atom.C, [81.2381032, -54.9887109, 5.7227741]),
qatom(atom.N, [80.4249348, -54.1325741, 6.4516291]),
qatom(atom.C, [79.2358594, -54.7111307, 6.4286412]),
qatom(atom.N, [79.2259421, -55.9028672, 5.7333274]),
qatom(atom.C, [80.5081660, -56.0900936, 5.2687581]),
qatom(atom.N, [80.9782004, -57.1239008, 4.5412669]),
qatom(atom.C, [82.2871761, -56.9865084, 4.2759396]),
qatom(atom.N, [83.1048049, -55.9901905, 4.6413114]),
qatom(atom.H, [77.8660812, -56.7011055, 4.3682360]),
qatom(atom.H, [79.0482819, -58.2867444, 6.6921166]),
qatom(atom.H, [77.0476212, -59.6802244, 6.7880307]),
qatom(atom.H, [75.3435460, -57.5456049, 6.7437497]),
qatom(atom.H, [77.2824533, -56.6792132, 8.7696559]),
qatom(atom.H, [76.4175022, -58.3282228, 9.0086592]),
qatom(atom.H, [78.3389131, -54.3306900, 6.8943851]),
qatom(atom.H, [82.7409510, -57.7837314, 3.6924885]),
qatom(atom.H, [84.4145667, -54.0043808, 5.4745795]),
qatom(atom.H, [83.1102512, -53.1954089, 6.2961768]),
qatom(atom.N, [83.4395643, -53.9711178, 5.7395785]),
qatom(atom.O, [76.9794498, -56.4032377, 6.2133584]),
qatom(atom.O, [78.9676470, -59.0104368, 4.7329093]),
qatom(atom.H, [79.7885087, -58.5069545, 4.4641360]),
qatom(atom.O, [76.2585830, -59.0180113, 4.9671631]),
qatom(atom.H, [76.8937011, -59.3625282, 4.3099344]),
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

