from sci import *

import os

qatom.basis = baslib("def2-svp")

geom = [ 
     qatom(atom.C, [0, 0, 0]), 
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
     qatom(atom.C, [23.02835970076679, 37.32490505145033, 0.0]), 
     qatom(atom.C, [23.028359700766785, 38.65987590585128, 0.0]), 
     qatom(atom.C, [24.30771301747605, 39.39851088764202, 0.0]), 
     qatom(atom.C, [24.307713017476047, 40.73348174204297, 0.0]), 
     qatom(atom.C, [25.587066334185312, 41.47211672383371, 0.0]), 
     qatom(atom.C, [25.58706633418531, 42.80708757823466, 0.0]), 
     qatom(atom.C, [26.866419650894574, 43.545722560025396, 0.0]), 
     qatom(atom.C, [26.86641965089457, 44.88069341442635, 0.0]), 
     qatom(atom.C, [28.145772967603836, 45.619328396217085, 0.0]), 
     qatom(atom.C, [28.145772967603833, 46.954299250618035, 0.0]), 
     qatom(atom.C, [29.425126284313098, 47.692934232408774, 0.0]), 
     qatom(atom.C, [29.425126284313095, 49.027905086809724, 0.0]), 
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
     qatom(atom.H, [20.807854979739385, 37.12964408629086, 0.0]), 
     qatom(atom.H, [23.970336391601016, 36.781054555426834, 0.0]), 
     qatom(atom.H, [22.087208296448647, 39.20324992248255, 0.0]), 
     qatom(atom.H, [25.249689708310278, 38.85466039161852, 0.0]), 
     qatom(atom.H, [23.36656161315791, 41.27685575867424, 0.0]), 
     qatom(atom.H, [26.52904302501954, 40.92826622781021, 0.0]), 
     qatom(atom.H, [24.64591492986717, 43.350461594865926, 0.0]), 
     qatom(atom.H, [27.808396341728802, 43.0018720640019, 0.0]), 
     qatom(atom.H, [25.925268246576433, 45.424067431057615, 0.0]), 
     qatom(atom.H, [29.087749658438064, 45.07547790019359, 0.0]), 
     qatom(atom.H, [27.204621563285695, 47.497673267249304, 0.0]), 
     qatom(atom.H, [30.367102975147326, 47.14908373638528, 0.0]), 
     qatom(atom.H, [28.485297424214085, 49.57051553218006, 0.0]), 
     qatom(atom.C, [30.70447960102236, 49.76654006860046, 0.0]), 
     qatom(atom.C, [30.704479601022356, 51.157683516020604, 0.0]), 
     qatom(atom.C, [31.90924516679646, 51.85325523973068, 0.0]), 
     qatom(atom.C, [33.11401073257057, 51.15768351602061, 0.0]), 
     qatom(atom.C, [33.11401073257058, 49.76654006860047, 0.0]), 
     qatom(atom.C, [31.909245166796474, 49.070968344890396, 0.0]), 
     qatom(atom.H, [29.75642452370617, 51.705043370115696, 0.0]), 
     qatom(atom.H, [31.909245166796456, 52.94797494792086, 0.0]), 
     qatom(atom.H, [34.062065809886754, 51.70504337011571, 0.0]), 
     qatom(atom.H, [34.06206580988677, 49.219180214505386, 0.0]), 
     qatom(atom.H, [31.909245166796477, 47.97624863670021, 0.0]), 
] 

qatom.unit = unit.angstrom

qmolecule = molecule( geom, charge=0, mult=1, sym=sym.C1 )
print qmolecule

qatom.basis = baslib("def2-svp/jkfit")
qatom.basis = baslib("aug-cc-pv5z-ri/jkfit")
#qatom.basis = myribasis
acene = [ i.new_basis() for i in geom]
qmolecule_RI_JK = molecule(acene, charge=0, mult=1, sym=sym.C1)
casscf.no4c_RI_JK = True
hint.use_RI_JK = True
hint.itrf_RI_JK_memory = 2000

qatom.basis = baslib("cc-pvdz-ri/mp2fit")
benzene = [ i.new_basis() for i in geom]
qmolecule_RI_C = molecule(benzene, charge=0, mult=1, sym=sym.C1)

qmolecule_RI_C = qmolecule_RI_JK

#qrel.sr1e = "dk2"
#prop.dipmom = True
#prop.soc = True
#qrel.so1e = "dk1"

scf.maxloop = 300
scf.tol_density = 1e-4

## Generate int
#scf.maxloop = 0
#scf.guess = "moread"

# loc3
#casscf.orbconfig = "orblist"
#casscf.frozen = []
#  Localizd occ
#casscf.occ = [i-1 for i in [107,108,124,125,131,135,149,154,155,156,157,158,160,163,166,167,168,169]] #
#casscf.closed = list(sorted(set(range(169))-set(casscf.occ)))
#  Localizd vir
#casscf.occ = []
#casscf.closed = list(sorted(set(range(169))-set(casscf.occ)))
#casscf.occ = [i-1 for i in [170,171,172,174,175,177,181,182,183,184,185,186,193,197]]

# localiz occ + virtual
#casscf.occ = [i-1 for i in [107,108,124,125,131,135,149,154,155,156,157,158,160,163,166]] + [i-1 for i in [170,171,172,174,175,177,181,182,183,184,185]]
#casscf.closed = list(sorted(set(range(169))-set(casscf.occ)))
#casscf.roots = {1.0:1}

### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [ 0  ]
casscf.closed = [85-2]
casscf.occ    = [   4]
#casscf.roots = {1.0:7}
casscf.roots = {1.0:1}

##-#
#occ_active = [84,85] # avigadro ordering
#vir_active = [86,89] # avigadro ordering
#occ_active = map((lambda x : x-1), occ_active) # C/C++ ordering
#vir_active = map((lambda x : x-1), vir_active) # C/C++ ordering
#
#active = occ_active+vir_active
#docc   = filter(lambda x: not x in occ_active, range(0,85))
#
#casscf.scfinp = key.scfread
#casscf.orbconfig = "orblist"
#casscf.frozen = []
#casscf.closed = docc
#casscf.occ    = active
##-#

casscf.maxMacroloop = 100
casscf.tolMacroloop = 1e-5

#hint.atom_ordering = [i-1 for i in [1,4,6,8,10,12,14,16]]   # <====

prop.dipmom = True

casscf.citype = "fullci"
#casscf.localize_type = "orz"
casscf.CI_restartGrad = casscf.tolMacroloop
casscf.CI_onedotGrad = casscf.tolMacroloop

#qcdmrg.schedule_type = "orz"
#qcdmrg.numschedule          = 4
#qcdmrg.numdot               = [     2,     2,     2,     1 ]
#qcdmrg.nrgstate             = [   256,   256,   256,   256 ] # M
#qcdmrg.thresh_david         = [ 5.e-3, 5.e-4, 1.e-5, 1.e-5 ]
#qcdmrg.thresh_sweep         = [ 5.e-4, 5.e-5, 1.e-6, 1.e-6 ]
#qcdmrg.dennoise             = [ 1.e-3, 1.e-5,   0.0,   0.0 ]

##casscf.citype = "dmrg"
##casscf.localize_type = "orz"
###casscf.debugkeys=["localizeocc"]
casscf.debugkeys=["canonical"]
##
##dmrg.init_alpha = []
##dmrg.init_beta  = []
##for i in range(11):
##    dmrg.init_alpha.append(2*i)
##    dmrg.init_beta  = dmrg.init_alpha
##dmrg.guess_option = "hf"
##dmrg.orb_ordering_option = "nosort"
##dmrg.m_state   = 256
##dmrg.tol_sweep = 1.e-6
##dmrg.tol_david = dmrg.tol_sweep * 10.0
##dmrg.debugkeys=["PrintRDMs","spinadaptation"]
###dmrg.debugkeys=["spinadaptation","noPrintRDMs"]
##prop.dipmom = True
##dmrg.silentlog = True
## ICMR

icmr.orbconfig = "symlist"
icmr.frozen = [54]
icmr.closed = [133.0]
icmr.occ = [4]
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
icmr.pt.toliter = 1e-10
#icmr.pt.ccvv_of = False #True # try later
#icmr.pt.ccvv_of = True
#icmr.pt.sinvshift = 0.00
icmr.pt.tolOrthExternal = 1e-8
icmr.pt.tolOrthInternal = 1e-8
#icmr.debugkeys = ["casfock","oporthog","oporthog_no_normd"] #,"caspt2d"]
#icmr.debugkeys = ["casfock","oporthog"] #,"caspt2d"]

#icmr.skip_casci = eval(os.getenv("ICMR_SKIPCASCI"))
icmr.method = "caspt2"
#icmr.debugkeys = ["no3TRDM"]

#scf.show_mulliken = 2

#qrel.sr1e = "dk2"
#prop.dipmom = True
#prop.soc = True
#qrel.so1e = "dk1"

# LCT
lct.test        = False
lct.DoPNO       = True
lct.UseOrthPNOs = True
lct.DoLoc       = True
lct.DoCEPT2     = True
lct.NewTrafo    = True
lct.Make4EXT    = False

lct.TCutPNOrho0 = 1e-8
lct.TCutPNOrho1 = 5e-8
lct.TCutPNOrho2 = 5e-8
lct.TCutPairs   = 1e-5

lct.TCutPNOrho0 = 1e-8
lct.TCutPNOrho1 = 5e-8
lct.TCutPNOrho2 = 5e-8
lct.TCutPairs   = 5e-6

lct.TCutPre     = 1e-7
#lct.TCutPre     = 0.0

#lct.TCutPNOrho0 = 0.0
#lct.TCutPNOrho1 = 0.0
#lct.TCutPNOrho2 = 0.0
#lct.TCutPairs   = 0.0

lct.MaxIter = 50

lct.DoCEPT2     = False
lct.NNewTrafo   = True
lct.NewTrafo    = (not lct.NNewTrafo)
lct.TrafoMode   = "Disk"
lct.NewAlgoPNO  = True
lct.OVLMode     = lct.TrafoMode
#lct.OVLMode     = "InCore"

# Use of Local PAO/PNO
#lct.UsePAOs    ppp = False
lct.UseVM1_CD   = True
lct.UseVM12     = (not lct.UseVM1_CD)

lct.PrintPairDistDBG = True
lct.PrintMapsDBG     = True

#lct.UseCholeskyOrb  = True
#lct.LocMet          = "FBNR"
#hint.loc_thresh     = 1e-14
#hint.maximize_niter = 20

#lct.LocMet = "PSM"
lct.LocPower = 2
lct.LocRecursive = True
lct.LocMeasure = True
hint.nroots = 2
hint.nconvroots = 1

lct.UsePAOs = False
lct.FormLVOs = True
lct.RIMP2 = False 
lct.LocMet = "PMNR"
#hint.PSMVersion = 2
hint.isOnTheFly = True
hint.ChargeType = "Loewdin"
hint.ImplTypePM = "incore"
hint.PMNRdebug = "no-debug"


hint.jacobi_thresh     = 1e-5 # Convergence threshold for Jacobi rotations
hint.loc_thresh        = 1e-5 # Convergence thrshold for grad norm
hint.cg_thresh         = 1e-5 # Convergence threshold for preconditioned conjugate gradient(=PCG) iterations
hint.res_tol           = 1e-5
hint.kscal = 1e-3
hint.print_dvd  = True
hint.stepThresh = 0.6
hint.maximize_niter = 2000
hint.nmicroiter     = 20000
#hint.cg_thresh      = 1e-6
#hint.loc_thresh     = 1e-5

#lct.TCutMKN=0.0

# # No Domain
lct.DomScheme = 'Scheme1'
lct.TCutDOI = 1e-3
# lct.UsePAOs     = False
# lct.UseVM1_CD_Asym = True
# lct.UseVM1_CD   = False
# lct.UseVM12     = False
