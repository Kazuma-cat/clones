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
qatom(atom.C, [0.0, 1.391143447420143, 0.0]),
qatom(atom.C, [-1.2047655657741054, 2.086715171130214, 0.0]),
qatom(atom.C, [-2.4095311315482104, 1.3911434474201414, 0.0]),
qatom(atom.C, [-2.409531131548209, -1.5543122344752192e-15, 0.0]),
qatom(atom.C, [-1.204765565774103, -0.6955717237100716, 0.0]),
qatom(atom.H, [1.2047655657741054, -0.6955717237100711, 0.0]),
qatom(atom.H, [1.204765565774105, 2.086715171130215, 0.0]),
qatom(atom.H, [-1.2047655657741068, 3.477858618550357, 0.0]),
qatom(atom.H, [-3.6142966973223167, 2.086715171130211, 0.0]),
qatom(atom.H, [-3.614296697322313, -0.6955717237100747, 0.0]),
qatom(atom.C, [-1.2047655657741014, -2.0867151711302148, 0.0]),
qatom(atom.H, [-1.7185965588616898, -2.450048689514529, 0.8899811598910946]),
qatom(atom.H, [-1.7185965588616898, -2.450048689514529, -0.8899811598910946]),
qatom(atom.C, [0.2565886347502335, -2.6033813115051005, 0.0]),
qatom(atom.H, [0.7704196278378216, -2.240047793120786, 0.8899811598910946]),
qatom(atom.H, [0.7704196278378216, -2.240047793120786, -0.8899811598910946]),
qatom(atom.C, [0.25658863475023524, -4.1533813115051, 0.0]),
qatom(atom.H, [-0.25724235833735315, -4.516714829889414, 0.8899811598910946]),
qatom(atom.H, [-0.25724235833735315, -4.516714829889414, -0.8899811598910946]),
qatom(atom.C, [1.7179428352745707, -4.670047451879986, 0.0]),
qatom(atom.H, [2.231773828362159, -4.306713933495671, 0.8899811598910946]),
qatom(atom.H, [2.231773828362159, -4.306713933495671, -0.8899811598910946]),
qatom(atom.C, [1.7179428352745725, -6.220047451879986, 0.0]),
qatom(atom.H, [1.204111842186984, -6.5833809702643, 0.8899811598910946]),
qatom(atom.H, [1.204111842186984, -6.5833809702643, -0.8899811598910946]),
qatom(atom.C, [3.179297035798908, -6.736713592254872, 0.0]),
qatom(atom.H, [3.6931280288864956, -6.373380073870557, 0.8899811598910946]),
qatom(atom.H, [3.6931280288864956, -6.373380073870557, -0.8899811598910946]),
qatom(atom.C, [3.1792970357989097, -8.286713592254872, 0.0]),
qatom(atom.H, [2.665466042711321, -8.650047110639186, 0.8899811598910946]),
qatom(atom.H, [2.665466042711321, -8.650047110639186, -0.8899811598910946]),
qatom(atom.C, [4.6406512363232455, -8.803379732629757, 0.0]),
qatom(atom.H, [5.154482229410833, -8.440046214245443, 0.8899811598910946]),
qatom(atom.H, [5.154482229410833, -8.440046214245443, -0.8899811598910946]),
qatom(atom.C, [4.640651236323247, -10.353379732629758, 0.0]),
qatom(atom.H, [4.126820243235659, -10.716713251014072, 0.8899811598910946]),
qatom(atom.H, [4.126820243235659, -10.716713251014072, -0.8899811598910946]),
qatom(atom.C, [6.102005436847582, -10.870045873004644, 0.0]),
qatom(atom.H, [6.61583642993517, -10.50671235462033, 0.8899811598910946]),
qatom(atom.H, [6.61583642993517, -10.50671235462033, -0.8899811598910946]),
qatom(atom.C, [6.102005436847584, -12.420045873004645, 0.0]),
qatom(atom.H, [5.588174443759995, -12.783379391388959, 0.8899811598910946]),
qatom(atom.H, [5.588174443759995, -12.783379391388959, -0.8899811598910946]),
qatom(atom.C, [7.563359637371919, -12.93671201337953, 0.0]),
qatom(atom.H, [8.077190630459507, -12.573378494995216, 0.8899811598910946]),
qatom(atom.H, [8.077190630459507, -12.573378494995216, -0.8899811598910946]),
qatom(atom.C, [7.563359637371921, -14.486712013379531, 0.0]),
qatom(atom.H, [7.049528644284332, -14.850045531763845, 0.8899811598910946]),
qatom(atom.H, [7.049528644284332, -14.850045531763845, -0.8899811598910946]),
qatom(atom.C, [9.024713837896256, -15.003378153754417, 0.0]),
qatom(atom.H, [9.538544830983843, -14.640044635370103, 0.8899811598910946]),
qatom(atom.H, [9.538544830983843, -14.640044635370103, -0.8899811598910946]),
qatom(atom.C, [9.024713837896257, -16.553378153754416, 0.0]),
qatom(atom.H, [8.51088284480867, -16.91671167213873, 0.8899811598910946]),
qatom(atom.H, [8.51088284480867, -16.91671167213873, -0.8899811598910946]),
qatom(atom.C, [10.486068038420592, -17.070044294129303, 0.0]),
qatom(atom.H, [10.99989903150818, -16.70671077574499, 0.8899811598910946]),
qatom(atom.H, [10.99989903150818, -16.70671077574499, -0.8899811598910946]),
qatom(atom.C, [10.486068038420592, -18.620044294129304, 0.0]),
qatom(atom.H, [9.972237045333003, -18.983377812513616, 0.8899811598910946]),
qatom(atom.H, [9.972237045333003, -18.983377812513616, -0.8899811598910946]),
qatom(atom.C, [11.947422238944927, -19.13671043450419, 0.0]),
qatom(atom.H, [12.461253232032515, -18.77337691611988, 0.8899811598910946]),
qatom(atom.H, [12.461253232032515, -18.77337691611988, -0.8899811598910946]),
qatom(atom.C, [11.947422238944927, -20.686710434504192, 0.0]),
qatom(atom.H, [11.433591245857338, -21.050043952888505, 0.8899811598910946]),
qatom(atom.H, [11.433591245857338, -21.050043952888505, -0.8899811598910946]),
qatom(atom.C, [13.408776439469262, -21.20337657487908, 0.0]),
qatom(atom.H, [13.92260743255685, -20.840043056494768, 0.8899811598910946]),
qatom(atom.H, [13.92260743255685, -20.840043056494768, -0.8899811598910946]),
qatom(atom.H, [13.408776439469262, -22.29337657487908, 0.0]),
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
qatom(atom.C, [0.0, 1.391143447420143, 0.0]),
qatom(atom.C, [-1.2047655657741054, 2.086715171130214, 0.0]),
qatom(atom.C, [-2.4095311315482104, 1.3911434474201414, 0.0]),
qatom(atom.C, [-2.409531131548209, -1.5543122344752192e-15, 0.0]),
qatom(atom.C, [-1.204765565774103, -0.6955717237100716, 0.0]),
qatom(atom.H, [1.2047655657741054, -0.6955717237100711, 0.0]),
qatom(atom.H, [1.204765565774105, 2.086715171130215, 0.0]),
qatom(atom.H, [-1.2047655657741068, 3.477858618550357, 0.0]),
qatom(atom.H, [-3.6142966973223167, 2.086715171130211, 0.0]),
qatom(atom.H, [-3.614296697322313, -0.6955717237100747, 0.0]),
qatom(atom.C, [-1.2047655657741014, -2.0867151711302148, 0.0]),
qatom(atom.H, [-1.7185965588616898, -2.450048689514529, 0.8899811598910946]),
qatom(atom.H, [-1.7185965588616898, -2.450048689514529, -0.8899811598910946]),
qatom(atom.C, [0.2565886347502335, -2.6033813115051005, 0.0]),
qatom(atom.H, [0.7704196278378216, -2.240047793120786, 0.8899811598910946]),
qatom(atom.H, [0.7704196278378216, -2.240047793120786, -0.8899811598910946]),
qatom(atom.C, [0.25658863475023524, -4.1533813115051, 0.0]),
qatom(atom.H, [-0.25724235833735315, -4.516714829889414, 0.8899811598910946]),
qatom(atom.H, [-0.25724235833735315, -4.516714829889414, -0.8899811598910946]),
qatom(atom.C, [1.7179428352745707, -4.670047451879986, 0.0]),
qatom(atom.H, [2.231773828362159, -4.306713933495671, 0.8899811598910946]),
qatom(atom.H, [2.231773828362159, -4.306713933495671, -0.8899811598910946]),
qatom(atom.C, [1.7179428352745725, -6.220047451879986, 0.0]),
qatom(atom.H, [1.204111842186984, -6.5833809702643, 0.8899811598910946]),
qatom(atom.H, [1.204111842186984, -6.5833809702643, -0.8899811598910946]),
qatom(atom.C, [3.179297035798908, -6.736713592254872, 0.0]),
qatom(atom.H, [3.6931280288864956, -6.373380073870557, 0.8899811598910946]),
qatom(atom.H, [3.6931280288864956, -6.373380073870557, -0.8899811598910946]),
qatom(atom.C, [3.1792970357989097, -8.286713592254872, 0.0]),
qatom(atom.H, [2.665466042711321, -8.650047110639186, 0.8899811598910946]),
qatom(atom.H, [2.665466042711321, -8.650047110639186, -0.8899811598910946]),
qatom(atom.C, [4.6406512363232455, -8.803379732629757, 0.0]),
qatom(atom.H, [5.154482229410833, -8.440046214245443, 0.8899811598910946]),
qatom(atom.H, [5.154482229410833, -8.440046214245443, -0.8899811598910946]),
qatom(atom.C, [4.640651236323247, -10.353379732629758, 0.0]),
qatom(atom.H, [4.126820243235659, -10.716713251014072, 0.8899811598910946]),
qatom(atom.H, [4.126820243235659, -10.716713251014072, -0.8899811598910946]),
qatom(atom.C, [6.102005436847582, -10.870045873004644, 0.0]),
qatom(atom.H, [6.61583642993517, -10.50671235462033, 0.8899811598910946]),
qatom(atom.H, [6.61583642993517, -10.50671235462033, -0.8899811598910946]),
qatom(atom.C, [6.102005436847584, -12.420045873004645, 0.0]),
qatom(atom.H, [5.588174443759995, -12.783379391388959, 0.8899811598910946]),
qatom(atom.H, [5.588174443759995, -12.783379391388959, -0.8899811598910946]),
qatom(atom.C, [7.563359637371919, -12.93671201337953, 0.0]),
qatom(atom.H, [8.077190630459507, -12.573378494995216, 0.8899811598910946]),
qatom(atom.H, [8.077190630459507, -12.573378494995216, -0.8899811598910946]),
qatom(atom.C, [7.563359637371921, -14.486712013379531, 0.0]),
qatom(atom.H, [7.049528644284332, -14.850045531763845, 0.8899811598910946]),
qatom(atom.H, [7.049528644284332, -14.850045531763845, -0.8899811598910946]),
qatom(atom.C, [9.024713837896256, -15.003378153754417, 0.0]),
qatom(atom.H, [9.538544830983843, -14.640044635370103, 0.8899811598910946]),
qatom(atom.H, [9.538544830983843, -14.640044635370103, -0.8899811598910946]),
qatom(atom.C, [9.024713837896257, -16.553378153754416, 0.0]),
qatom(atom.H, [8.51088284480867, -16.91671167213873, 0.8899811598910946]),
qatom(atom.H, [8.51088284480867, -16.91671167213873, -0.8899811598910946]),
qatom(atom.C, [10.486068038420592, -17.070044294129303, 0.0]),
qatom(atom.H, [10.99989903150818, -16.70671077574499, 0.8899811598910946]),
qatom(atom.H, [10.99989903150818, -16.70671077574499, -0.8899811598910946]),
qatom(atom.C, [10.486068038420592, -18.620044294129304, 0.0]),
qatom(atom.H, [9.972237045333003, -18.983377812513616, 0.8899811598910946]),
qatom(atom.H, [9.972237045333003, -18.983377812513616, -0.8899811598910946]),
qatom(atom.C, [11.947422238944927, -19.13671043450419, 0.0]),
qatom(atom.H, [12.461253232032515, -18.77337691611988, 0.8899811598910946]),
qatom(atom.H, [12.461253232032515, -18.77337691611988, -0.8899811598910946]),
qatom(atom.C, [11.947422238944927, -20.686710434504192, 0.0]),
qatom(atom.H, [11.433591245857338, -21.050043952888505, 0.8899811598910946]),
qatom(atom.H, [11.433591245857338, -21.050043952888505, -0.8899811598910946]),
qatom(atom.C, [13.408776439469262, -21.20337657487908, 0.0]),
qatom(atom.H, [13.92260743255685, -20.840043056494768, 0.8899811598910946]),
qatom(atom.H, [13.92260743255685, -20.840043056494768, -0.8899811598910946]),
qatom(atom.H, [13.408776439469262, -22.29337657487908, 0.0]),
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
# orig frozen ... 26.00
# orig closed ... 75.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [98]
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
icmr.frozen = [26]
icmr.closed = [72]
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

