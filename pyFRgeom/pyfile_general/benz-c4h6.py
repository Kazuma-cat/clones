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
qatom(atom.C, [0.0, 0.0, 0.0]),
qatom(atom.C, [0.0, 1.3349708544009489, 0.0]),
qatom(atom.C, [1.2793533167092666, 2.073605836191684, 0.0]),
qatom(atom.C, [1.2793533167092666, 3.408576690592633, 0.0]),
qatom(atom.H, [-0.9398288600990078, -0.542610445370341, 0.0]),
qatom(atom.H, [0.9398288600990078, -0.542610445370341, 0.0]),
qatom(atom.H, [-0.9411514043181364, 1.878344871032219, 0.0]),
qatom(atom.H, [2.221330007543493, 1.5297553401681898, 0.0]),
qatom(atom.H, [0.33952445661025876, 3.9511871359629738, 0.0]),
qatom(atom.C, [2.558706633418533, 4.147211672383368, 0.0]),
qatom(atom.C, [2.558706633418533, 5.538355119803511, 0.0]),
qatom(atom.C, [3.7634721991926385, 6.233926843513583, 0.0]),
qatom(atom.C, [4.9682377649667435, 5.538355119803511, 0.0]),
qatom(atom.C, [4.968237764966743, 4.147211672383368, 0.0]),
qatom(atom.C, [3.7634721991926368, 3.451639948673298, 0.0]),
qatom(atom.H, [1.6106515561023467, 6.085714973898603, 0.0]),
qatom(atom.H, [3.763472199192638, 7.328646551703766, 0.0]),
qatom(atom.H, [5.91629284228293, 6.085714973898603, 0.0]),
qatom(atom.H, [5.916292842282928, 3.5998518182882764, 0.0]),
qatom(atom.H, [3.763472199192636, 2.356920240483115, 0.0]),
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
qatom(atom.C, [0.0, 0.0, 0.0]),
qatom(atom.C, [0.0, 1.3349708544009489, 0.0]),
qatom(atom.C, [1.2793533167092666, 2.073605836191684, 0.0]),
qatom(atom.C, [1.2793533167092666, 3.408576690592633, 0.0]),
qatom(atom.H, [-0.9398288600990078, -0.542610445370341, 0.0]),
qatom(atom.H, [0.9398288600990078, -0.542610445370341, 0.0]),
qatom(atom.H, [-0.9411514043181364, 1.878344871032219, 0.0]),
qatom(atom.H, [2.221330007543493, 1.5297553401681898, 0.0]),
qatom(atom.H, [0.33952445661025876, 3.9511871359629738, 0.0]),
qatom(atom.C, [2.558706633418533, 4.147211672383368, 0.0]),
qatom(atom.C, [2.558706633418533, 5.538355119803511, 0.0]),
qatom(atom.C, [3.7634721991926385, 6.233926843513583, 0.0]),
qatom(atom.C, [4.9682377649667435, 5.538355119803511, 0.0]),
qatom(atom.C, [4.968237764966743, 4.147211672383368, 0.0]),
qatom(atom.C, [3.7634721991926368, 3.451639948673298, 0.0]),
qatom(atom.H, [1.6106515561023467, 6.085714973898603, 0.0]),
qatom(atom.H, [3.763472199192638, 7.328646551703766, 0.0]),
qatom(atom.H, [5.91629284228293, 6.085714973898603, 0.0]),
qatom(atom.H, [5.916292842282928, 3.5998518182882764, 0.0]),
qatom(atom.H, [3.763472199192636, 2.356920240483115, 0.0]),
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
# orig frozen ... 10.00
# orig closed ... 25.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [35]
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
icmr.frozen = [10]
icmr.closed = [25]
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

