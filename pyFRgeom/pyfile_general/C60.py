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
qatom(atom.C, [-2.319825, -8.558323, -6.206653]),
qatom(atom.C, [0.733975, -5.834231, -7.092603]),
qatom(atom.C, [0.224390, -2.467734, -4.652410]),
qatom(atom.C, [-3.145390, -3.104899, -2.254089]),
qatom(atom.C, [-4.714007, -6.867668, -3.217577]),
qatom(atom.C, [-3.378812, -8.523208, -5.312185]),
qatom(atom.C, [0.029153, -7.021260, -7.223139]),
qatom(atom.C, [0.844636, -3.235616, -5.625291]),
qatom(atom.C, [-2.054986, -2.390940, -2.726090]),
qatom(atom.C, [-4.662055, -5.660958, -2.536708]),
qatom(atom.C, [0.158840, -8.049793, -6.252106]),
qatom(atom.C, [1.653311, -4.345505, -5.263772]),
qatom(atom.C, [-0.736705, -2.737913, -2.327358]),
qatom(atom.C, [-3.711056, -5.454630, -1.502439]),
qatom(atom.C, [-3.160633, -8.735421, -3.924807]),
qatom(atom.C, [-0.997345, -8.806981, -5.752007]),
qatom(atom.C, [1.598736, -5.624510, -5.985688]),
qatom(atom.C, [0.385783, -2.776134, -3.275816]),
qatom(atom.C, [-2.964662, -4.196218, -1.363211]),
qatom(atom.C, [-3.817528, -7.920372, -2.893374]),
qatom(atom.C, [-0.869175, -9.439078, -4.488607]),
qatom(atom.C, [2.043801, -6.783509, -5.299391]),
qatom(atom.C, [1.508543, -3.571326, -2.930786]),
qatom(atom.C, [-1.738560, -4.237261, -0.651127]),
qatom(atom.C, [-3.204987, -7.861916, -1.615113]),
qatom(atom.C, [-1.961359, -9.402562, -3.565913]),
qatom(atom.C, [1.317384, -8.007834, -5.434525]),
qatom(atom.C, [2.147950, -4.363863, -3.934186]),
qatom(atom.C, [-0.613817, -3.500426, -1.137467]),
qatom(atom.C, [-3.151043, -6.617142, -0.913454]),
qatom(atom.C, [1.560351, -9.047241, -4.462921]),
qatom(atom.C, [3.026776, -5.422587, -3.498935]),
qatom(atom.C, [0.690966, -3.845423, -0.625441]),
qatom(atom.C, [-2.222011, -6.500992, 0.185343]),
qatom(atom.C, [-1.686753, -9.713175, -2.183262]),
qatom(atom.C, [0.435607, -9.784076, -3.976581]),
qatom(atom.C, [2.972832, -6.667359, -4.200594]),
qatom(atom.C, [1.783149, -3.881940, -1.548135]),
qatom(atom.C, [-1.495594, -5.276668, 0.320477]),
qatom(atom.C, [-2.326160, -8.920639, -1.179862]),
qatom(atom.C, [0.558495, -10.546589, -2.786691]),
qatom(atom.C, [3.532846, -7.829872, -3.611608]),
qatom(atom.C, [2.982423, -4.549080, -1.189241]),
qatom(atom.C, [-0.337050, -5.234708, 1.138058]),
qatom(atom.C, [-1.831521, -8.938997, 0.149724]),
qatom(atom.C, [-0.563992, -10.508368, -1.838232]),
qatom(atom.C, [2.786452, -9.088283, -3.750837]),
qatom(atom.C, [3.639317, -5.364130, -2.220673]),
qatom(atom.C, [0.819136, -4.477520, 0.637959]),
qatom(atom.C, [-1.776945, -7.659991, 0.871639]),
qatom(atom.C, [2.967181, -10.179604, -2.859959]),
qatom(atom.C, [4.535795, -6.416833, -1.896470]),
qatom(atom.C, [2.141617, -4.726176, 1.092605]),
qatom(atom.C, [-0.912184, -7.450271, 1.978554]),
qatom(atom.C, [-0.402599, -10.816768, -0.461638]),
qatom(atom.C, [1.876777, -10.893563, -2.387959]),
qatom(atom.C, [4.483845, -7.623543, -2.577340]),
qatom(atom.C, [3.200602, -4.761292, 0.198136]),
qatom(atom.C, [-0.207363, -6.263242, 2.109092]),
qatom(atom.C, [-1.022845, -10.048885, 0.511243]),
qatom(atom.H, [-2.492766, -8.219012, -7.230278]),
qatom(atom.H, [0.480518, -5.002855, -7.754133]),
qatom(atom.H, [-0.524380, -1.736933, -4.966101]),
qatom(atom.H, [-4.120313, -2.927499, -2.713549]),
qatom(atom.H, [-5.331080, -6.929909, -4.116715]),
qatom(atom.H, [-4.345570, -8.157563, -5.664704]),
qatom(atom.H, [-0.753443, -7.079926, -7.983122]),
qatom(atom.H, [0.560124, -3.080313, -6.668710]),
qatom(atom.H, [-2.212036, -1.678338, -3.539008]),
qatom(atom.H, [-5.240367, -4.819118, -2.923407]),
qatom(atom.H, [3.942104, -10.357000, -2.400498]),
qatom(atom.H, [5.152873, -6.354595, -0.997335]),
qatom(atom.H, [2.314557, -5.065490, 2.116230]),
qatom(atom.H, [-0.658729, -8.281648, 2.640083]),
qatom(atom.H, [0.346171, -11.547567, -0.147946]),
qatom(atom.H, [2.033823, -11.606166, -1.575041]),
qatom(atom.H, [5.062159, -8.465381, -2.190638]),
qatom(atom.H, [4.167363, -5.126932, 0.550656]),
qatom(atom.H, [0.575237, -6.204576, 2.869072]),
qatom(atom.H, [-0.738334, -10.204190, 1.554661]),
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
qatom(atom.C, [-2.319825, -8.558323, -6.206653]),
qatom(atom.C, [0.733975, -5.834231, -7.092603]),
qatom(atom.C, [0.224390, -2.467734, -4.652410]),
qatom(atom.C, [-3.145390, -3.104899, -2.254089]),
qatom(atom.C, [-4.714007, -6.867668, -3.217577]),
qatom(atom.C, [-3.378812, -8.523208, -5.312185]),
qatom(atom.C, [0.029153, -7.021260, -7.223139]),
qatom(atom.C, [0.844636, -3.235616, -5.625291]),
qatom(atom.C, [-2.054986, -2.390940, -2.726090]),
qatom(atom.C, [-4.662055, -5.660958, -2.536708]),
qatom(atom.C, [0.158840, -8.049793, -6.252106]),
qatom(atom.C, [1.653311, -4.345505, -5.263772]),
qatom(atom.C, [-0.736705, -2.737913, -2.327358]),
qatom(atom.C, [-3.711056, -5.454630, -1.502439]),
qatom(atom.C, [-3.160633, -8.735421, -3.924807]),
qatom(atom.C, [-0.997345, -8.806981, -5.752007]),
qatom(atom.C, [1.598736, -5.624510, -5.985688]),
qatom(atom.C, [0.385783, -2.776134, -3.275816]),
qatom(atom.C, [-2.964662, -4.196218, -1.363211]),
qatom(atom.C, [-3.817528, -7.920372, -2.893374]),
qatom(atom.C, [-0.869175, -9.439078, -4.488607]),
qatom(atom.C, [2.043801, -6.783509, -5.299391]),
qatom(atom.C, [1.508543, -3.571326, -2.930786]),
qatom(atom.C, [-1.738560, -4.237261, -0.651127]),
qatom(atom.C, [-3.204987, -7.861916, -1.615113]),
qatom(atom.C, [-1.961359, -9.402562, -3.565913]),
qatom(atom.C, [1.317384, -8.007834, -5.434525]),
qatom(atom.C, [2.147950, -4.363863, -3.934186]),
qatom(atom.C, [-0.613817, -3.500426, -1.137467]),
qatom(atom.C, [-3.151043, -6.617142, -0.913454]),
qatom(atom.C, [1.560351, -9.047241, -4.462921]),
qatom(atom.C, [3.026776, -5.422587, -3.498935]),
qatom(atom.C, [0.690966, -3.845423, -0.625441]),
qatom(atom.C, [-2.222011, -6.500992, 0.185343]),
qatom(atom.C, [-1.686753, -9.713175, -2.183262]),
qatom(atom.C, [0.435607, -9.784076, -3.976581]),
qatom(atom.C, [2.972832, -6.667359, -4.200594]),
qatom(atom.C, [1.783149, -3.881940, -1.548135]),
qatom(atom.C, [-1.495594, -5.276668, 0.320477]),
qatom(atom.C, [-2.326160, -8.920639, -1.179862]),
qatom(atom.C, [0.558495, -10.546589, -2.786691]),
qatom(atom.C, [3.532846, -7.829872, -3.611608]),
qatom(atom.C, [2.982423, -4.549080, -1.189241]),
qatom(atom.C, [-0.337050, -5.234708, 1.138058]),
qatom(atom.C, [-1.831521, -8.938997, 0.149724]),
qatom(atom.C, [-0.563992, -10.508368, -1.838232]),
qatom(atom.C, [2.786452, -9.088283, -3.750837]),
qatom(atom.C, [3.639317, -5.364130, -2.220673]),
qatom(atom.C, [0.819136, -4.477520, 0.637959]),
qatom(atom.C, [-1.776945, -7.659991, 0.871639]),
qatom(atom.C, [2.967181, -10.179604, -2.859959]),
qatom(atom.C, [4.535795, -6.416833, -1.896470]),
qatom(atom.C, [2.141617, -4.726176, 1.092605]),
qatom(atom.C, [-0.912184, -7.450271, 1.978554]),
qatom(atom.C, [-0.402599, -10.816768, -0.461638]),
qatom(atom.C, [1.876777, -10.893563, -2.387959]),
qatom(atom.C, [4.483845, -7.623543, -2.577340]),
qatom(atom.C, [3.200602, -4.761292, 0.198136]),
qatom(atom.C, [-0.207363, -6.263242, 2.109092]),
qatom(atom.C, [-1.022845, -10.048885, 0.511243]),
qatom(atom.H, [-2.492766, -8.219012, -7.230278]),
qatom(atom.H, [0.480518, -5.002855, -7.754133]),
qatom(atom.H, [-0.524380, -1.736933, -4.966101]),
qatom(atom.H, [-4.120313, -2.927499, -2.713549]),
qatom(atom.H, [-5.331080, -6.929909, -4.116715]),
qatom(atom.H, [-4.345570, -8.157563, -5.664704]),
qatom(atom.H, [-0.753443, -7.079926, -7.983122]),
qatom(atom.H, [0.560124, -3.080313, -6.668710]),
qatom(atom.H, [-2.212036, -1.678338, -3.539008]),
qatom(atom.H, [-5.240367, -4.819118, -2.923407]),
qatom(atom.H, [3.942104, -10.357000, -2.400498]),
qatom(atom.H, [5.152873, -6.354595, -0.997335]),
qatom(atom.H, [2.314557, -5.065490, 2.116230]),
qatom(atom.H, [-0.658729, -8.281648, 2.640083]),
qatom(atom.H, [0.346171, -11.547567, -0.147946]),
qatom(atom.H, [2.033823, -11.606166, -1.575041]),
qatom(atom.H, [5.062159, -8.465381, -2.190638]),
qatom(atom.H, [4.167363, -5.126932, 0.550656]),
qatom(atom.H, [0.575237, -6.204576, 2.869072]),
qatom(atom.H, [-0.738334, -10.204190, 1.554661]),
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
# orig frozen ... 60.00
# orig closed ... 130.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [190]
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
icmr.frozen = [60]
icmr.closed = [130]
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

