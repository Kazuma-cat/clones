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
qatom(atom.C, [0, 0, 0]),
qatom(atom.C, [0.0, 1.391143447420143, 0.0]),
qatom(atom.C, [-1.2047655657741054, 2.086715171130214, 0.0]),
qatom(atom.C, [-2.4095311315482104, 1.3911434474201414, 0.0]),
qatom(atom.C, [-2.409531131548209, -1.5543122344752192e-15, 0.0]),
qatom(atom.C, [-1.204765565774103, -0.6955717237100716, 0.0]),
qatom(atom.H, [0.9480550773161863, -0.5473598540950914, 0.0]),
qatom(atom.H, [0.9480550773161859, 1.9385033015152353, 0.0]),
qatom(atom.H, [-1.2047655657741065, 3.1814348793203973, 0.0]),
qatom(atom.H, [-3.3575862088643973, 1.9385033015152318, 0.0]),
qatom(atom.H, [-3.3575862088643946, -0.5473598540950945, 0.0]),
qatom(atom.C, [-1.2047655657741012, -2.211821723710072, 0.0]),
qatom(atom.H, [-1.7185965588616896, -2.575155242094386, 0.8899811598910946]),
qatom(atom.H, [-1.7185965588616896, -2.575155242094386, -0.8899811598910946]),
qatom(atom.C, [0.23678964235603317, -2.7214878712153623, 0.0]),
qatom(atom.H, [0.7506206354436212, -2.358154352831048, 0.8899811598910946]),
qatom(atom.H, [0.7506206354436212, -2.358154352831048, -0.8899811598910946]),
qatom(atom.C, [0.2367896423560351, -4.250487871215363, 0.0]),
qatom(atom.H, [-0.2770413507315533, -4.613821389599677, 0.8899811598910946]),
qatom(atom.H, [-0.2770413507315533, -4.613821389599677, -0.8899811598910946]),
qatom(atom.C, [1.6783448504861695, -4.7601540187206535, 0.0]),
qatom(atom.H, [2.1921758435737577, -4.3968205003363385, 0.8899811598910946]),
qatom(atom.H, [2.1921758435737577, -4.3968205003363385, -0.8899811598910946]),
qatom(atom.C, [1.678344850486171, -6.289154018720653, 0.0]),
qatom(atom.H, [1.1645138573985827, -6.652487537104967, 0.8899811598910946]),
qatom(atom.H, [1.1645138573985827, -6.652487537104967, -0.8899811598910946]),
qatom(atom.C, [3.1199000586163055, -6.798820166225944, 0.0]),
qatom(atom.H, [3.6337310517038937, -6.435486647841629, 0.8899811598910946]),
qatom(atom.H, [3.6337310517038937, -6.435486647841629, -0.8899811598910946]),
qatom(atom.C, [3.119900058616307, -8.327820166225944, 0.0]),
qatom(atom.H, [2.606069065528718, -8.691153684610258, 0.8899811598910946]),
qatom(atom.H, [2.606069065528718, -8.691153684610258, -0.8899811598910946]),
qatom(atom.C, [4.561455266746441, -8.837486313731235, 0.0]),
qatom(atom.H, [5.07528625983403, -8.474152795346921, 0.8899811598910946]),
qatom(atom.H, [5.07528625983403, -8.474152795346921, -0.8899811598910946]),
qatom(atom.C, [4.561455266746443, -10.366486313731235, 0.0]),
qatom(atom.H, [4.047624273658855, -10.729819832115549, 0.8899811598910946]),
qatom(atom.H, [4.047624273658855, -10.729819832115549, -0.8899811598910946]),
qatom(atom.C, [6.003010474876578, -10.876152461236526, 0.0]),
qatom(atom.H, [6.516841467964166, -10.512818942852212, 0.8899811598910946]),
qatom(atom.H, [6.516841467964166, -10.512818942852212, -0.8899811598910946]),
qatom(atom.H, [6.003010474876579, -11.966152461236526, 0.0]),
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
qatom(atom.C, [0, 0, 0]),
qatom(atom.C, [0.0, 1.391143447420143, 0.0]),
qatom(atom.C, [-1.2047655657741054, 2.086715171130214, 0.0]),
qatom(atom.C, [-2.4095311315482104, 1.3911434474201414, 0.0]),
qatom(atom.C, [-2.409531131548209, -1.5543122344752192e-15, 0.0]),
qatom(atom.C, [-1.204765565774103, -0.6955717237100716, 0.0]),
qatom(atom.H, [0.9480550773161863, -0.5473598540950914, 0.0]),
qatom(atom.H, [0.9480550773161859, 1.9385033015152353, 0.0]),
qatom(atom.H, [-1.2047655657741065, 3.1814348793203973, 0.0]),
qatom(atom.H, [-3.3575862088643973, 1.9385033015152318, 0.0]),
qatom(atom.H, [-3.3575862088643946, -0.5473598540950945, 0.0]),
qatom(atom.C, [-1.2047655657741012, -2.211821723710072, 0.0]),
qatom(atom.H, [-1.7185965588616896, -2.575155242094386, 0.8899811598910946]),
qatom(atom.H, [-1.7185965588616896, -2.575155242094386, -0.8899811598910946]),
qatom(atom.C, [0.23678964235603317, -2.7214878712153623, 0.0]),
qatom(atom.H, [0.7506206354436212, -2.358154352831048, 0.8899811598910946]),
qatom(atom.H, [0.7506206354436212, -2.358154352831048, -0.8899811598910946]),
qatom(atom.C, [0.2367896423560351, -4.250487871215363, 0.0]),
qatom(atom.H, [-0.2770413507315533, -4.613821389599677, 0.8899811598910946]),
qatom(atom.H, [-0.2770413507315533, -4.613821389599677, -0.8899811598910946]),
qatom(atom.C, [1.6783448504861695, -4.7601540187206535, 0.0]),
qatom(atom.H, [2.1921758435737577, -4.3968205003363385, 0.8899811598910946]),
qatom(atom.H, [2.1921758435737577, -4.3968205003363385, -0.8899811598910946]),
qatom(atom.C, [1.678344850486171, -6.289154018720653, 0.0]),
qatom(atom.H, [1.1645138573985827, -6.652487537104967, 0.8899811598910946]),
qatom(atom.H, [1.1645138573985827, -6.652487537104967, -0.8899811598910946]),
qatom(atom.C, [3.1199000586163055, -6.798820166225944, 0.0]),
qatom(atom.H, [3.6337310517038937, -6.435486647841629, 0.8899811598910946]),
qatom(atom.H, [3.6337310517038937, -6.435486647841629, -0.8899811598910946]),
qatom(atom.C, [3.119900058616307, -8.327820166225944, 0.0]),
qatom(atom.H, [2.606069065528718, -8.691153684610258, 0.8899811598910946]),
qatom(atom.H, [2.606069065528718, -8.691153684610258, -0.8899811598910946]),
qatom(atom.C, [4.561455266746441, -8.837486313731235, 0.0]),
qatom(atom.H, [5.07528625983403, -8.474152795346921, 0.8899811598910946]),
qatom(atom.H, [5.07528625983403, -8.474152795346921, -0.8899811598910946]),
qatom(atom.C, [4.561455266746443, -10.366486313731235, 0.0]),
qatom(atom.H, [4.047624273658855, -10.729819832115549, 0.8899811598910946]),
qatom(atom.H, [4.047624273658855, -10.729819832115549, -0.8899811598910946]),
qatom(atom.C, [6.003010474876578, -10.876152461236526, 0.0]),
qatom(atom.H, [6.516841467964166, -10.512818942852212, 0.8899811598910946]),
qatom(atom.H, [6.516841467964166, -10.512818942852212, -0.8899811598910946]),
qatom(atom.H, [6.003010474876579, -11.966152461236526, 0.0]),
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
# orig frozen ... 16.00
# orig closed ... 45.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [58]
casscf.occ = [6]
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
icmr.frozen = [16]
icmr.closed = [42]
icmr.occ = [6]
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

