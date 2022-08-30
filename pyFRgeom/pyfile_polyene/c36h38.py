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
qatom(atom.C, [2.558706633418533, 4.147211672383368, 0.0]),
qatom(atom.C, [2.558706633418533, 5.482182526784317, 0.0]),
qatom(atom.C, [3.8380599501278, 6.220817508575053, 0.0]),
qatom(atom.C, [3.8380599501278, 7.555788362976001, 0.0]),
qatom(atom.C, [5.117413266837066, 8.294423344766736, 0.0]),
qatom(atom.C, [5.117413266837066, 9.629394199167685, 0.0]),
qatom(atom.C, [6.3967665835463325, 10.36802918095842, 0.0]),
qatom(atom.C, [6.3967665835463325, 11.703000035359368, 0.0]),
qatom(atom.C, [7.676119900255599, 12.441635017150103, 0.0]),
qatom(atom.C, [7.676119900255599, 13.776605871551052, 0.0]),
qatom(atom.C, [8.955473216964865, 14.515240853341787, 0.0]),
qatom(atom.C, [8.955473216964865, 15.850211707742735, 0.0]),
qatom(atom.C, [10.234826533674132, 16.58884668953347, 0.0]),
qatom(atom.C, [10.234826533674134, 17.92381754393442, 0.0]),
qatom(atom.C, [11.514179850383401, 18.662452525725154, 0.0]),
qatom(atom.C, [11.514179850383401, 19.997423380126104, 0.0]),
qatom(atom.C, [12.793533167092669, 20.73605836191684, 0.0]),
qatom(atom.C, [12.793533167092669, 22.07102921631779, 0.0]),
qatom(atom.C, [14.072886483801936, 22.809664198108525, 0.0]),
qatom(atom.C, [14.072886483801936, 24.144635052509475, 0.0]),
qatom(atom.C, [15.352239800511203, 24.88327003430021, 0.0]),
qatom(atom.C, [15.352239800511203, 26.21824088870116, 0.0]),
qatom(atom.C, [16.63159311722047, 26.956875870491896, 0.0]),
qatom(atom.C, [16.63159311722047, 28.291846724892846, 0.0]),
qatom(atom.C, [17.910946433929734, 29.03048170668358, 0.0]),
qatom(atom.C, [17.910946433929734, 30.36545256108453, 0.0]),
qatom(atom.C, [19.190299750639, 31.104087542875266, 0.0]),
qatom(atom.C, [19.190299750639, 32.43905839727621, 0.0]),
qatom(atom.C, [20.469653067348265, 33.17769337906695, 0.0]),
qatom(atom.C, [20.46965306734826, 34.5126642334679, 0.0]),
qatom(atom.C, [21.749006384057527, 35.25129921525864, 0.0]),
qatom(atom.C, [21.749006384057523, 36.58627006965959, 0.0]),
qatom(atom.H, [-0.9398288600990078, -0.542610445370341, 0.0]),
qatom(atom.H, [0.9398288600990078, -0.542610445370341, 0.0]),
qatom(atom.H, [-0.9411514043181364, 1.878344871032219, 0.0]),
qatom(atom.H, [2.221330007543493, 1.5297553401681898, 0.0]),
qatom(atom.H, [0.3382019123911302, 3.951950707223903, 0.0]),
qatom(atom.H, [3.5006833242527593, 3.603361176359874, 0.0]),
qatom(atom.H, [1.6175552291003965, 6.025556543415587, 0.0]),
qatom(atom.H, [4.7800366409620265, 5.676967012551558, 0.0]),
qatom(atom.H, [2.8969085458096635, 8.099162379607272, 0.0]),
qatom(atom.H, [6.059389957671293, 7.750572848743242, 0.0]),
qatom(atom.H, [4.176261862518929, 10.172768215798955, 0.0]),
qatom(atom.H, [7.338743274380559, 9.824178684934926, 0.0]),
qatom(atom.H, [5.455615179228197, 12.246374051990639, 0.0]),
qatom(atom.H, [8.618096591089826, 11.89778452112661, 0.0]),
qatom(atom.H, [6.734968495937462, 14.319979888182322, 0.0]),
qatom(atom.H, [9.897449907799091, 13.971390357318294, 0.0]),
qatom(atom.H, [8.01432181264673, 16.393585724374006, 0.0]),
qatom(atom.H, [11.176803224508358, 16.044996193509974, 0.0]),
qatom(atom.H, [9.293675129355998, 18.46719156056569, 0.0]),
qatom(atom.H, [12.456156541217627, 18.11860202970166, 0.0]),
qatom(atom.H, [10.573028446065265, 20.540797396757373, 0.0]),
qatom(atom.H, [13.735509857926894, 20.192207865893344, 0.0]),
qatom(atom.H, [11.852381762774533, 22.61440323294906, 0.0]),
qatom(atom.H, [15.014863174636162, 22.26581370208503, 0.0]),
qatom(atom.H, [13.1317350794838, 24.688009069140744, 0.0]),
qatom(atom.H, [16.29421649134543, 24.339419538276715, 0.0]),
qatom(atom.H, [14.411088396193067, 26.76161490533243, 0.0]),
qatom(atom.H, [17.573569808054696, 26.4130253744684, 0.0]),
qatom(atom.H, [15.690441712902333, 28.835220741524115, 0.0]),
qatom(atom.H, [18.85292312476396, 28.486631210660086, 0.0]),
qatom(atom.H, [16.969795029611596, 30.9088265777158, 0.0]),
qatom(atom.H, [20.132276441473227, 30.56023704685177, 0.0]),
qatom(atom.H, [18.24914834632086, 32.98243241390748, 0.0]),
qatom(atom.H, [21.411629758182492, 32.63384288304346, 0.0]),
qatom(atom.H, [19.528501663030124, 35.05603825009917, 0.0]),
qatom(atom.H, [22.690983074891754, 34.707448719235146, 0.0]),
qatom(atom.H, [22.68883524415653, 37.128880515029934, 0.0]),
qatom(atom.H, [20.809177523958514, 37.12888051502993, 0.0]),
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
qatom(atom.C, [2.558706633418533, 4.147211672383368, 0.0]),
qatom(atom.C, [2.558706633418533, 5.482182526784317, 0.0]),
qatom(atom.C, [3.8380599501278, 6.220817508575053, 0.0]),
qatom(atom.C, [3.8380599501278, 7.555788362976001, 0.0]),
qatom(atom.C, [5.117413266837066, 8.294423344766736, 0.0]),
qatom(atom.C, [5.117413266837066, 9.629394199167685, 0.0]),
qatom(atom.C, [6.3967665835463325, 10.36802918095842, 0.0]),
qatom(atom.C, [6.3967665835463325, 11.703000035359368, 0.0]),
qatom(atom.C, [7.676119900255599, 12.441635017150103, 0.0]),
qatom(atom.C, [7.676119900255599, 13.776605871551052, 0.0]),
qatom(atom.C, [8.955473216964865, 14.515240853341787, 0.0]),
qatom(atom.C, [8.955473216964865, 15.850211707742735, 0.0]),
qatom(atom.C, [10.234826533674132, 16.58884668953347, 0.0]),
qatom(atom.C, [10.234826533674134, 17.92381754393442, 0.0]),
qatom(atom.C, [11.514179850383401, 18.662452525725154, 0.0]),
qatom(atom.C, [11.514179850383401, 19.997423380126104, 0.0]),
qatom(atom.C, [12.793533167092669, 20.73605836191684, 0.0]),
qatom(atom.C, [12.793533167092669, 22.07102921631779, 0.0]),
qatom(atom.C, [14.072886483801936, 22.809664198108525, 0.0]),
qatom(atom.C, [14.072886483801936, 24.144635052509475, 0.0]),
qatom(atom.C, [15.352239800511203, 24.88327003430021, 0.0]),
qatom(atom.C, [15.352239800511203, 26.21824088870116, 0.0]),
qatom(atom.C, [16.63159311722047, 26.956875870491896, 0.0]),
qatom(atom.C, [16.63159311722047, 28.291846724892846, 0.0]),
qatom(atom.C, [17.910946433929734, 29.03048170668358, 0.0]),
qatom(atom.C, [17.910946433929734, 30.36545256108453, 0.0]),
qatom(atom.C, [19.190299750639, 31.104087542875266, 0.0]),
qatom(atom.C, [19.190299750639, 32.43905839727621, 0.0]),
qatom(atom.C, [20.469653067348265, 33.17769337906695, 0.0]),
qatom(atom.C, [20.46965306734826, 34.5126642334679, 0.0]),
qatom(atom.C, [21.749006384057527, 35.25129921525864, 0.0]),
qatom(atom.C, [21.749006384057523, 36.58627006965959, 0.0]),
qatom(atom.H, [-0.9398288600990078, -0.542610445370341, 0.0]),
qatom(atom.H, [0.9398288600990078, -0.542610445370341, 0.0]),
qatom(atom.H, [-0.9411514043181364, 1.878344871032219, 0.0]),
qatom(atom.H, [2.221330007543493, 1.5297553401681898, 0.0]),
qatom(atom.H, [0.3382019123911302, 3.951950707223903, 0.0]),
qatom(atom.H, [3.5006833242527593, 3.603361176359874, 0.0]),
qatom(atom.H, [1.6175552291003965, 6.025556543415587, 0.0]),
qatom(atom.H, [4.7800366409620265, 5.676967012551558, 0.0]),
qatom(atom.H, [2.8969085458096635, 8.099162379607272, 0.0]),
qatom(atom.H, [6.059389957671293, 7.750572848743242, 0.0]),
qatom(atom.H, [4.176261862518929, 10.172768215798955, 0.0]),
qatom(atom.H, [7.338743274380559, 9.824178684934926, 0.0]),
qatom(atom.H, [5.455615179228197, 12.246374051990639, 0.0]),
qatom(atom.H, [8.618096591089826, 11.89778452112661, 0.0]),
qatom(atom.H, [6.734968495937462, 14.319979888182322, 0.0]),
qatom(atom.H, [9.897449907799091, 13.971390357318294, 0.0]),
qatom(atom.H, [8.01432181264673, 16.393585724374006, 0.0]),
qatom(atom.H, [11.176803224508358, 16.044996193509974, 0.0]),
qatom(atom.H, [9.293675129355998, 18.46719156056569, 0.0]),
qatom(atom.H, [12.456156541217627, 18.11860202970166, 0.0]),
qatom(atom.H, [10.573028446065265, 20.540797396757373, 0.0]),
qatom(atom.H, [13.735509857926894, 20.192207865893344, 0.0]),
qatom(atom.H, [11.852381762774533, 22.61440323294906, 0.0]),
qatom(atom.H, [15.014863174636162, 22.26581370208503, 0.0]),
qatom(atom.H, [13.1317350794838, 24.688009069140744, 0.0]),
qatom(atom.H, [16.29421649134543, 24.339419538276715, 0.0]),
qatom(atom.H, [14.411088396193067, 26.76161490533243, 0.0]),
qatom(atom.H, [17.573569808054696, 26.4130253744684, 0.0]),
qatom(atom.H, [15.690441712902333, 28.835220741524115, 0.0]),
qatom(atom.H, [18.85292312476396, 28.486631210660086, 0.0]),
qatom(atom.H, [16.969795029611596, 30.9088265777158, 0.0]),
qatom(atom.H, [20.132276441473227, 30.56023704685177, 0.0]),
qatom(atom.H, [18.24914834632086, 32.98243241390748, 0.0]),
qatom(atom.H, [21.411629758182492, 32.63384288304346, 0.0]),
qatom(atom.H, [19.528501663030124, 35.05603825009917, 0.0]),
qatom(atom.H, [22.690983074891754, 34.707448719235146, 0.0]),
qatom(atom.H, [22.68883524415653, 37.128880515029934, 0.0]),
qatom(atom.H, [20.809177523958514, 37.12888051502993, 0.0]),
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
# orig frozen ... 36.00
# orig closed ... 91.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [127]
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
icmr.frozen = [36]
icmr.closed = [91]
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

