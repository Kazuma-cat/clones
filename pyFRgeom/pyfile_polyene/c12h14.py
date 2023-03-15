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
qatom(atom.C, [0.080278, 6.759410, 0.000000]),
qatom(atom.C, [0.652876, 5.553117, 0.000000]),
qatom(atom.C, [-0.080278, 4.300466, 0.000000]),
qatom(atom.C, [0.500686, 3.087545, 0.000000]),
qatom(atom.C, [-0.223307, 1.838157, 0.000000]),
qatom(atom.C, [0.361143, 0.624379, 0.000000]),
qatom(atom.C, [-0.361143, -0.624379, 0.000000]),
qatom(atom.C, [0.223307, -1.838157, 0.000000]),
qatom(atom.C, [-0.500686, -3.087545, 0.000000]),
qatom(atom.C, [0.080278, -4.300466, 0.000000]),
qatom(atom.C, [-0.652876, -5.553117, 0.000000]),
qatom(atom.C, [-0.080278, -6.759410, 0.000000]),
qatom(atom.H, [0.669048, 7.670460, 0.000000]),
qatom(atom.H, [-1.000288, 6.874626, 0.000000]),
qatom(atom.H, [1.739327, 5.476859, 0.000000]),
qatom(atom.H, [-1.167732, 4.368660, 0.000000]),
qatom(atom.H, [1.588670, 3.024310, 0.000000]),
qatom(atom.H, [-1.311185, 1.899816, 0.000000]),
qatom(atom.H, [1.449131, 0.563391, 0.000000]),
qatom(atom.H, [-1.449131, -0.563391, 0.000000]),
qatom(atom.H, [1.311185, -1.899816, 0.000000]),
qatom(atom.H, [-1.588670, -3.024310, 0.000000]),
qatom(atom.H, [1.167732, -4.368660, 0.000000]),
qatom(atom.H, [-1.739327, -5.476859, 0.000000]),
qatom(atom.H, [1.000288, -6.874626, 0.000000]),
qatom(atom.H, [-0.669048, -7.670460, 0.000000]),
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
qatom(atom.C, [0.080278, 6.759410, 0.000000]),
qatom(atom.C, [0.652876, 5.553117, 0.000000]),
qatom(atom.C, [-0.080278, 4.300466, 0.000000]),
qatom(atom.C, [0.500686, 3.087545, 0.000000]),
qatom(atom.C, [-0.223307, 1.838157, 0.000000]),
qatom(atom.C, [0.361143, 0.624379, 0.000000]),
qatom(atom.C, [-0.361143, -0.624379, 0.000000]),
qatom(atom.C, [0.223307, -1.838157, 0.000000]),
qatom(atom.C, [-0.500686, -3.087545, 0.000000]),
qatom(atom.C, [0.080278, -4.300466, 0.000000]),
qatom(atom.C, [-0.652876, -5.553117, 0.000000]),
qatom(atom.C, [-0.080278, -6.759410, 0.000000]),
qatom(atom.H, [0.669048, 7.670460, 0.000000]),
qatom(atom.H, [-1.000288, 6.874626, 0.000000]),
qatom(atom.H, [1.739327, 5.476859, 0.000000]),
qatom(atom.H, [-1.167732, 4.368660, 0.000000]),
qatom(atom.H, [1.588670, 3.024310, 0.000000]),
qatom(atom.H, [-1.311185, 1.899816, 0.000000]),
qatom(atom.H, [1.449131, 0.563391, 0.000000]),
qatom(atom.H, [-1.449131, -0.563391, 0.000000]),
qatom(atom.H, [1.311185, -1.899816, 0.000000]),
qatom(atom.H, [-1.588670, -3.024310, 0.000000]),
qatom(atom.H, [1.167732, -4.368660, 0.000000]),
qatom(atom.H, [-1.739327, -5.476859, 0.000000]),
qatom(atom.H, [1.000288, -6.874626, 0.000000]),
qatom(atom.H, [-0.669048, -7.670460, 0.000000]),
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
# orig frozen ... 12.00
# orig closed ... 31.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [43]
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
icmr.frozen = [12]
icmr.closed = [31]
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

