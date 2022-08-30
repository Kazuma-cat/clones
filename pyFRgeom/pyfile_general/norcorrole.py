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
qatom(atom.C, [3.694132, -0.247473, 7.587338]),
qatom(atom.N, [4.822146, 0.409965, 7.248317]),
qatom(atom.Ni, [6.301486, 0.000000, 8.177068]),
qatom(atom.C, [2.660390, 0.247006, 6.755403]),
qatom(atom.H, [1.751377, -0.031284, 6.760800]),
qatom(atom.C, [3.220301, 1.215886, 5.930174]),
qatom(atom.H, [2.762219, 1.721571, 5.269303]),
qatom(atom.C, [4.611528, 1.315342, 6.254149]),
qatom(atom.N, [7.353758, 1.146780, 7.293454]),
qatom(atom.C, [5.705040, 2.110057, 5.751259]),
qatom(atom.C, [7.062630, 2.012935, 6.272793]),
qatom(atom.C, [8.308319, 2.663836, 5.963863]),
qatom(atom.H, [8.445245, 3.316604, 5.287292]),
qatom(atom.C, [9.269186, 2.172625, 6.824091]),
qatom(atom.H, [10.182041, 2.434573, 6.854019]),
qatom(atom.C, [5.452564, 3.047185, 4.620534]),
qatom(atom.H, [5.257773, 2.534496, 3.808878]),
qatom(atom.H, [6.246714, 3.603299, 4.472856]),
qatom(atom.H, [4.687017, 3.620575, 4.835918]),
qatom(atom.C, [8.641833, 1.196742, 7.664857]),
qatom(atom.C, [8.908840, 0.247473, 8.766799]),
qatom(atom.N, [7.780826, -0.409965, 9.105820]),
qatom(atom.C, [9.942582, -0.247006, 9.598734]),
qatom(atom.H, [10.851595, 0.031284, 9.593337]),
qatom(atom.C, [9.382671, -1.215886, 10.423963]),
qatom(atom.H, [9.840753, -1.721571, 11.084834]),
qatom(atom.C, [7.991445, -1.315342, 10.099988]),
qatom(atom.N, [5.249215, -1.146780, 9.060682]),
qatom(atom.C, [6.897932, -2.110057, 10.602878]),
qatom(atom.C, [5.540342, -2.012935, 10.081344]),
qatom(atom.C, [4.294653, -2.663836, 10.390274]),
qatom(atom.H, [4.157727, -3.316604, 11.066844]),
qatom(atom.C, [3.333787, -2.172625, 9.530046]),
qatom(atom.H, [2.420931, -2.434573, 9.500118]),
qatom(atom.C, [7.150408, -3.047185, 11.733603]),
qatom(atom.H, [7.345200, -2.534496, 12.545258]),
qatom(atom.H, [6.356258, -3.603299, 11.881280]),
qatom(atom.H, [7.915955, -3.620575, 11.518219]),
qatom(atom.C, [3.961140, -1.196742, 8.689280]),
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
qatom(atom.C, [3.694132, -0.247473, 7.587338]),
qatom(atom.N, [4.822146, 0.409965, 7.248317]),
qatom(atom.Ni, [6.301486, 0.000000, 8.177068]),
qatom(atom.C, [2.660390, 0.247006, 6.755403]),
qatom(atom.H, [1.751377, -0.031284, 6.760800]),
qatom(atom.C, [3.220301, 1.215886, 5.930174]),
qatom(atom.H, [2.762219, 1.721571, 5.269303]),
qatom(atom.C, [4.611528, 1.315342, 6.254149]),
qatom(atom.N, [7.353758, 1.146780, 7.293454]),
qatom(atom.C, [5.705040, 2.110057, 5.751259]),
qatom(atom.C, [7.062630, 2.012935, 6.272793]),
qatom(atom.C, [8.308319, 2.663836, 5.963863]),
qatom(atom.H, [8.445245, 3.316604, 5.287292]),
qatom(atom.C, [9.269186, 2.172625, 6.824091]),
qatom(atom.H, [10.182041, 2.434573, 6.854019]),
qatom(atom.C, [5.452564, 3.047185, 4.620534]),
qatom(atom.H, [5.257773, 2.534496, 3.808878]),
qatom(atom.H, [6.246714, 3.603299, 4.472856]),
qatom(atom.H, [4.687017, 3.620575, 4.835918]),
qatom(atom.C, [8.641833, 1.196742, 7.664857]),
qatom(atom.C, [8.908840, 0.247473, 8.766799]),
qatom(atom.N, [7.780826, -0.409965, 9.105820]),
qatom(atom.C, [9.942582, -0.247006, 9.598734]),
qatom(atom.H, [10.851595, 0.031284, 9.593337]),
qatom(atom.C, [9.382671, -1.215886, 10.423963]),
qatom(atom.H, [9.840753, -1.721571, 11.084834]),
qatom(atom.C, [7.991445, -1.315342, 10.099988]),
qatom(atom.N, [5.249215, -1.146780, 9.060682]),
qatom(atom.C, [6.897932, -2.110057, 10.602878]),
qatom(atom.C, [5.540342, -2.012935, 10.081344]),
qatom(atom.C, [4.294653, -2.663836, 10.390274]),
qatom(atom.H, [4.157727, -3.316604, 11.066844]),
qatom(atom.C, [3.333787, -2.172625, 9.530046]),
qatom(atom.H, [2.420931, -2.434573, 9.500118]),
qatom(atom.C, [7.150408, -3.047185, 11.733603]),
qatom(atom.H, [7.345200, -2.534496, 12.545258]),
qatom(atom.H, [6.356258, -3.603299, 11.881280]),
qatom(atom.H, [7.915955, -3.620575, 11.518219]),
qatom(atom.C, [3.961140, -1.196742, 8.689280]),
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
# orig frozen ... 29.00
# orig closed ... 66.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [95]
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
icmr.frozen = [29]
icmr.closed = [66]
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

