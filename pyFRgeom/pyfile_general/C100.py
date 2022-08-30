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
qatom(atom.C, [-2.001776, -5.886744, 0.337808]),
qatom(atom.C, [-2.157942, -4.717276, -3.661495]),
qatom(atom.C, [-6.170548, -4.349872, -4.737165]),
qatom(atom.C, [-8.501074, -5.292918, -1.407988]),
qatom(atom.C, [-5.918080, -6.242831, 1.727077]),
qatom(atom.C, [-2.976977, -6.147498, 1.272692]),
qatom(atom.C, [-1.532490, -5.068168, -2.487004]),
qatom(atom.C, [-4.811492, -4.306540, -4.948363]),
qatom(atom.C, [-8.282867, -4.914106, -2.712793]),
qatom(atom.C, [-7.144278, -6.054012, 1.132497]),
qatom(atom.C, [-1.449496, -4.137689, -1.400610]),
qatom(atom.C, [-4.031496, -3.214970, -4.445873]),
qatom(atom.C, [-7.859074, -3.580807, -3.022867]),
qatom(atom.C, [-7.645848, -4.731678, 0.903477]),
qatom(atom.C, [-3.685579, -5.074624, 1.903925]),
qatom(atom.C, [-1.679442, -4.537673, -0.020764]),
qatom(atom.C, [-2.735194, -3.415163, -3.818113]),
qatom(atom.C, [-6.828333, -3.304934, -4.011249]),
qatom(atom.C, [-8.307387, -4.360243, -0.337470]),
qatom(atom.C, [-5.121948, -5.120965, 2.126443]),
qatom(atom.C, [-2.032678, -3.530448, 0.915329]),
qatom(atom.C, [-2.245349, -2.395985, -2.959454]),
qatom(atom.C, [-6.153128, -2.057991, -3.941434]),
qatom(atom.C, [-8.356979, -2.983195, -0.679654]),
qatom(atom.C, [-5.807228, -3.893214, 2.321933]),
qatom(atom.C, [-3.053408, -3.803678, 1.894367]),
qatom(atom.C, [-1.591404, -2.763588, -1.729387]),
qatom(atom.C, [-4.730634, -2.012270, -4.162870]),
qatom(atom.C, [-8.128475, -2.586552, -2.045838]),
qatom(atom.C, [-7.091293, -3.695399, 1.700198]),
qatom(atom.C, [-1.477615, -1.768003, -0.698997]),
qatom(atom.C, [-4.009549, -0.859855, -3.696685]),
qatom(atom.C, [-7.774151, -1.217920, -2.303710]),
qatom(atom.C, [-7.573632, -2.349236, 1.557427]),
qatom(atom.C, [-3.682650, -2.688211, 2.545934]),
qatom(atom.C, [-1.702676, -2.158047, 0.645527]),
qatom(atom.C, [-2.745687, -1.054629, -3.085388]),
qatom(atom.C, [-6.769787, -0.948970, -3.267266]),
qatom(atom.C, [-8.217124, -1.987321, 0.347080]),
qatom(atom.C, [-5.082560, -2.733447, 2.763681]),
qatom(atom.C, [-1.997330, -1.148359, 1.618617]),
qatom(atom.C, [-2.205756, -0.010755, -2.265536]),
qatom(atom.C, [-6.121669, 0.328649, -3.253073]),
qatom(atom.C, [-8.334124, -0.598135, 0.014743]),
qatom(atom.C, [-5.781830, -1.510847, 3.025838]),
qatom(atom.C, [-3.015900, -1.421130, 2.595635]),
qatom(atom.C, [-1.553249, -0.377639, -1.038017]),
qatom(atom.C, [-4.702133, 0.374432, -3.474068]),
qatom(atom.C, [-8.105649, -0.202525, -1.348673]),
qatom(atom.C, [-7.063429, -1.313376, 2.406061]),
qatom(atom.C, [-1.426911, 0.598135, -0.014743]),
qatom(atom.C, [-3.979206, 1.510847, -3.025838]),
qatom(atom.C, [-7.763706, 1.148359, -1.618618]),
qatom(atom.C, [-7.555280, 0.010756, 2.265536]),
qatom(atom.C, [-3.639367, -0.328649, 3.253073]),
qatom(atom.C, [-1.655387, 0.202524, 1.348673]),
qatom(atom.C, [-2.697607, 1.313376, -2.406061]),
qatom(atom.C, [-6.745136, 1.421130, -2.595636]),
qatom(atom.C, [-8.207787, 0.377639, 1.038016]),
qatom(atom.C, [-5.058903, -0.374432, 3.474068]),
qatom(atom.C, [-1.986885, 1.217920, 2.303710]),
qatom(atom.C, [-2.187404, 2.349236, -1.557426]),
qatom(atom.C, [-6.078386, 2.688211, -2.545934]),
qatom(atom.C, [-8.283421, 1.768003, 0.698996]),
qatom(atom.C, [-5.751487, 0.859856, 3.696685]),
qatom(atom.C, [-2.991249, 0.948970, 3.267266]),
qatom(atom.C, [-1.543911, 1.987321, -0.347080]),
qatom(atom.C, [-4.678476, 2.733447, -2.763681]),
qatom(atom.C, [-8.058361, 2.158047, -0.645527]),
qatom(atom.C, [-7.015349, 1.054630, 3.085387]),
qatom(atom.C, [-1.404056, 2.983195, 0.679654]),
qatom(atom.C, [-3.953808, 3.893214, -2.321932]),
qatom(atom.C, [-7.728358, 3.530448, -0.915330]),
qatom(atom.C, [-7.515686, 2.395986, 2.959454]),
qatom(atom.C, [-3.607907, 2.057991, 3.941434]),
qatom(atom.C, [-1.632560, 2.586552, 2.045838]),
qatom(atom.C, [-2.669743, 3.695399, -1.700198]),
qatom(atom.C, [-6.707628, 3.803678, -1.894367]),
qatom(atom.C, [-8.169632, 2.763588, 1.729387]),
qatom(atom.C, [-5.030401, 2.012270, 4.162870]),
qatom(atom.C, [-1.901961, 3.580806, 3.022867]),
qatom(atom.C, [-2.115188, 4.731678, -0.903477]),
qatom(atom.C, [-6.075457, 5.074624, -1.903925]),
qatom(atom.C, [-8.311540, 4.137689, 1.400609]),
qatom(atom.C, [-5.729539, 3.214970, 4.445873]),
qatom(atom.C, [-2.932702, 3.304934, 4.011249]),
qatom(atom.C, [-1.453649, 4.360243, 0.337470]),
qatom(atom.C, [-4.639088, 5.120965, -2.126442]),
qatom(atom.C, [-8.081594, 4.537673, 0.020763]),
qatom(atom.C, [-7.025841, 3.415163, 3.818112]),
qatom(atom.C, [-1.259961, 5.292918, 1.407988]),
qatom(atom.C, [-3.842956, 6.242831, -1.727077]),
qatom(atom.C, [-7.759260, 5.886744, -0.337808]),
qatom(atom.C, [-7.603093, 4.717276, 3.661494]),
qatom(atom.C, [-3.590487, 4.349872, 4.737165]),
qatom(atom.C, [-1.478168, 4.914105, 2.712794]),
qatom(atom.C, [-2.616758, 6.054012, -1.132497]),
qatom(atom.C, [-6.784059, 6.147498, -1.272693]),
qatom(atom.C, [-8.228546, 5.068169, 2.487003]),
qatom(atom.C, [-4.949543, 4.306540, 4.948363]),
qatom(atom.H, [-1.585347, -6.718764, -0.233894]),
qatom(atom.H, [-2.343185, -5.490833, -4.410012]),
qatom(atom.H, [-6.714531, -5.260572, -4.996855]),
qatom(atom.H, [-8.676684, -6.347909, -1.187257]),
qatom(atom.H, [-5.494278, -7.249176, 1.750350]),
qatom(atom.H, [-3.307931, -7.178442, 1.415181]),
qatom(atom.H, [-1.236102, -6.108510, -2.338069]),
qatom(atom.H, [-4.315749, -5.185012, -5.366726]),
qatom(atom.H, [-8.291147, -5.680252, -3.491490]),
qatom(atom.H, [-7.657904, -6.916122, 0.701913]),
qatom(atom.H, [-1.084352, 6.347909, 1.187257]),
qatom(atom.H, [-4.266758, 7.249176, -1.750350]),
qatom(atom.H, [-8.175689, 6.718764, 0.233893]),
qatom(atom.H, [-7.417850, 5.490834, 4.410011]),
qatom(atom.H, [-3.046504, 5.260572, 4.996855]),
qatom(atom.H, [-1.469888, 5.680252, 3.491490]),
qatom(atom.H, [-2.103132, 6.916122, -0.701912]),
qatom(atom.H, [-6.453105, 7.178442, -1.415182]),
qatom(atom.H, [-8.524933, 6.108510, 2.338068]),
qatom(atom.H, [-5.445286, 5.185012, 5.366726]),
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
qatom(atom.C, [-2.001776, -5.886744, 0.337808]),
qatom(atom.C, [-2.157942, -4.717276, -3.661495]),
qatom(atom.C, [-6.170548, -4.349872, -4.737165]),
qatom(atom.C, [-8.501074, -5.292918, -1.407988]),
qatom(atom.C, [-5.918080, -6.242831, 1.727077]),
qatom(atom.C, [-2.976977, -6.147498, 1.272692]),
qatom(atom.C, [-1.532490, -5.068168, -2.487004]),
qatom(atom.C, [-4.811492, -4.306540, -4.948363]),
qatom(atom.C, [-8.282867, -4.914106, -2.712793]),
qatom(atom.C, [-7.144278, -6.054012, 1.132497]),
qatom(atom.C, [-1.449496, -4.137689, -1.400610]),
qatom(atom.C, [-4.031496, -3.214970, -4.445873]),
qatom(atom.C, [-7.859074, -3.580807, -3.022867]),
qatom(atom.C, [-7.645848, -4.731678, 0.903477]),
qatom(atom.C, [-3.685579, -5.074624, 1.903925]),
qatom(atom.C, [-1.679442, -4.537673, -0.020764]),
qatom(atom.C, [-2.735194, -3.415163, -3.818113]),
qatom(atom.C, [-6.828333, -3.304934, -4.011249]),
qatom(atom.C, [-8.307387, -4.360243, -0.337470]),
qatom(atom.C, [-5.121948, -5.120965, 2.126443]),
qatom(atom.C, [-2.032678, -3.530448, 0.915329]),
qatom(atom.C, [-2.245349, -2.395985, -2.959454]),
qatom(atom.C, [-6.153128, -2.057991, -3.941434]),
qatom(atom.C, [-8.356979, -2.983195, -0.679654]),
qatom(atom.C, [-5.807228, -3.893214, 2.321933]),
qatom(atom.C, [-3.053408, -3.803678, 1.894367]),
qatom(atom.C, [-1.591404, -2.763588, -1.729387]),
qatom(atom.C, [-4.730634, -2.012270, -4.162870]),
qatom(atom.C, [-8.128475, -2.586552, -2.045838]),
qatom(atom.C, [-7.091293, -3.695399, 1.700198]),
qatom(atom.C, [-1.477615, -1.768003, -0.698997]),
qatom(atom.C, [-4.009549, -0.859855, -3.696685]),
qatom(atom.C, [-7.774151, -1.217920, -2.303710]),
qatom(atom.C, [-7.573632, -2.349236, 1.557427]),
qatom(atom.C, [-3.682650, -2.688211, 2.545934]),
qatom(atom.C, [-1.702676, -2.158047, 0.645527]),
qatom(atom.C, [-2.745687, -1.054629, -3.085388]),
qatom(atom.C, [-6.769787, -0.948970, -3.267266]),
qatom(atom.C, [-8.217124, -1.987321, 0.347080]),
qatom(atom.C, [-5.082560, -2.733447, 2.763681]),
qatom(atom.C, [-1.997330, -1.148359, 1.618617]),
qatom(atom.C, [-2.205756, -0.010755, -2.265536]),
qatom(atom.C, [-6.121669, 0.328649, -3.253073]),
qatom(atom.C, [-8.334124, -0.598135, 0.014743]),
qatom(atom.C, [-5.781830, -1.510847, 3.025838]),
qatom(atom.C, [-3.015900, -1.421130, 2.595635]),
qatom(atom.C, [-1.553249, -0.377639, -1.038017]),
qatom(atom.C, [-4.702133, 0.374432, -3.474068]),
qatom(atom.C, [-8.105649, -0.202525, -1.348673]),
qatom(atom.C, [-7.063429, -1.313376, 2.406061]),
qatom(atom.C, [-1.426911, 0.598135, -0.014743]),
qatom(atom.C, [-3.979206, 1.510847, -3.025838]),
qatom(atom.C, [-7.763706, 1.148359, -1.618618]),
qatom(atom.C, [-7.555280, 0.010756, 2.265536]),
qatom(atom.C, [-3.639367, -0.328649, 3.253073]),
qatom(atom.C, [-1.655387, 0.202524, 1.348673]),
qatom(atom.C, [-2.697607, 1.313376, -2.406061]),
qatom(atom.C, [-6.745136, 1.421130, -2.595636]),
qatom(atom.C, [-8.207787, 0.377639, 1.038016]),
qatom(atom.C, [-5.058903, -0.374432, 3.474068]),
qatom(atom.C, [-1.986885, 1.217920, 2.303710]),
qatom(atom.C, [-2.187404, 2.349236, -1.557426]),
qatom(atom.C, [-6.078386, 2.688211, -2.545934]),
qatom(atom.C, [-8.283421, 1.768003, 0.698996]),
qatom(atom.C, [-5.751487, 0.859856, 3.696685]),
qatom(atom.C, [-2.991249, 0.948970, 3.267266]),
qatom(atom.C, [-1.543911, 1.987321, -0.347080]),
qatom(atom.C, [-4.678476, 2.733447, -2.763681]),
qatom(atom.C, [-8.058361, 2.158047, -0.645527]),
qatom(atom.C, [-7.015349, 1.054630, 3.085387]),
qatom(atom.C, [-1.404056, 2.983195, 0.679654]),
qatom(atom.C, [-3.953808, 3.893214, -2.321932]),
qatom(atom.C, [-7.728358, 3.530448, -0.915330]),
qatom(atom.C, [-7.515686, 2.395986, 2.959454]),
qatom(atom.C, [-3.607907, 2.057991, 3.941434]),
qatom(atom.C, [-1.632560, 2.586552, 2.045838]),
qatom(atom.C, [-2.669743, 3.695399, -1.700198]),
qatom(atom.C, [-6.707628, 3.803678, -1.894367]),
qatom(atom.C, [-8.169632, 2.763588, 1.729387]),
qatom(atom.C, [-5.030401, 2.012270, 4.162870]),
qatom(atom.C, [-1.901961, 3.580806, 3.022867]),
qatom(atom.C, [-2.115188, 4.731678, -0.903477]),
qatom(atom.C, [-6.075457, 5.074624, -1.903925]),
qatom(atom.C, [-8.311540, 4.137689, 1.400609]),
qatom(atom.C, [-5.729539, 3.214970, 4.445873]),
qatom(atom.C, [-2.932702, 3.304934, 4.011249]),
qatom(atom.C, [-1.453649, 4.360243, 0.337470]),
qatom(atom.C, [-4.639088, 5.120965, -2.126442]),
qatom(atom.C, [-8.081594, 4.537673, 0.020763]),
qatom(atom.C, [-7.025841, 3.415163, 3.818112]),
qatom(atom.C, [-1.259961, 5.292918, 1.407988]),
qatom(atom.C, [-3.842956, 6.242831, -1.727077]),
qatom(atom.C, [-7.759260, 5.886744, -0.337808]),
qatom(atom.C, [-7.603093, 4.717276, 3.661494]),
qatom(atom.C, [-3.590487, 4.349872, 4.737165]),
qatom(atom.C, [-1.478168, 4.914105, 2.712794]),
qatom(atom.C, [-2.616758, 6.054012, -1.132497]),
qatom(atom.C, [-6.784059, 6.147498, -1.272693]),
qatom(atom.C, [-8.228546, 5.068169, 2.487003]),
qatom(atom.C, [-4.949543, 4.306540, 4.948363]),
qatom(atom.H, [-1.585347, -6.718764, -0.233894]),
qatom(atom.H, [-2.343185, -5.490833, -4.410012]),
qatom(atom.H, [-6.714531, -5.260572, -4.996855]),
qatom(atom.H, [-8.676684, -6.347909, -1.187257]),
qatom(atom.H, [-5.494278, -7.249176, 1.750350]),
qatom(atom.H, [-3.307931, -7.178442, 1.415181]),
qatom(atom.H, [-1.236102, -6.108510, -2.338069]),
qatom(atom.H, [-4.315749, -5.185012, -5.366726]),
qatom(atom.H, [-8.291147, -5.680252, -3.491490]),
qatom(atom.H, [-7.657904, -6.916122, 0.701913]),
qatom(atom.H, [-1.084352, 6.347909, 1.187257]),
qatom(atom.H, [-4.266758, 7.249176, -1.750350]),
qatom(atom.H, [-8.175689, 6.718764, 0.233893]),
qatom(atom.H, [-7.417850, 5.490834, 4.410011]),
qatom(atom.H, [-3.046504, 5.260572, 4.996855]),
qatom(atom.H, [-1.469888, 5.680252, 3.491490]),
qatom(atom.H, [-2.103132, 6.916122, -0.701912]),
qatom(atom.H, [-6.453105, 7.178442, -1.415182]),
qatom(atom.H, [-8.524933, 6.108510, 2.338068]),
qatom(atom.H, [-5.445286, 5.185012, 5.366726]),
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
# orig frozen ... 100.00
# orig closed ... 210.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [310]
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
icmr.frozen = [100]
icmr.closed = [210]
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

