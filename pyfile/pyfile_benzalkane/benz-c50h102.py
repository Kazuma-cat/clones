from sci import *

import os

qatom.basis = baslib("def2-svp")

geom = [ 
     qatom(atom.C, [0, 0, 0]), 
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
     qatom(atom.C, [13.408776439469262, -22.75337657487908, 0.0]), 
     qatom(atom.H, [12.894945446381673, -23.116710093263393, 0.8899811598910946]), 
     qatom(atom.H, [12.894945446381673, -23.116710093263393, -0.8899811598910946]), 
     qatom(atom.C, [14.870130639993597, -23.270042715253968, 0.0]), 
     qatom(atom.H, [15.383961633081185, -22.906709196869656, 0.8899811598910946]), 
     qatom(atom.H, [15.383961633081185, -22.906709196869656, -0.8899811598910946]), 
     qatom(atom.C, [14.870130639993597, -24.82004271525397, 0.0]), 
     qatom(atom.H, [14.356299646906008, -25.18337623363828, 0.8899811598910946]), 
     qatom(atom.H, [14.356299646906008, -25.18337623363828, -0.8899811598910946]), 
     qatom(atom.C, [16.33148484051793, -25.336708855628856, 0.0]), 
     qatom(atom.H, [16.845315833605518, -24.973375337244544, 0.8899811598910946]), 
     qatom(atom.H, [16.845315833605518, -24.973375337244544, -0.8899811598910946]), 
     qatom(atom.C, [16.33148484051793, -26.886708855628857, 0.0]), 
     qatom(atom.H, [15.817653847430341, -27.25004237401317, 0.8899811598910946]), 
     qatom(atom.H, [15.817653847430341, -27.25004237401317, -0.8899811598910946]), 
     qatom(atom.C, [17.792839041042264, -27.403374996003745, 0.0]), 
     qatom(atom.H, [18.30667003412985, -27.040041477619432, 0.8899811598910946]), 
     qatom(atom.H, [18.30667003412985, -27.040041477619432, -0.8899811598910946]), 
     qatom(atom.C, [17.792839041042264, -28.953374996003745, 0.0]), 
     qatom(atom.H, [17.279008047954676, -29.316708514388058, 0.8899811598910946]), 
     qatom(atom.H, [17.279008047954676, -29.316708514388058, -0.8899811598910946]), 
     qatom(atom.C, [19.254193241566597, -29.470041136378633, 0.0]), 
     qatom(atom.H, [19.768024234654185, -29.10670761799432, 0.8899811598910946]), 
     qatom(atom.H, [19.768024234654185, -29.10670761799432, -0.8899811598910946]), 
     qatom(atom.C, [19.254193241566597, -31.020041136378634, 0.0]), 
     qatom(atom.H, [18.74036224847901, -31.383374654762946, 0.8899811598910946]), 
     qatom(atom.H, [18.74036224847901, -31.383374654762946, -0.8899811598910946]), 
     qatom(atom.C, [20.71554744209093, -31.53670727675352, 0.0]), 
     qatom(atom.H, [21.229378435178518, -31.17337375836921, 0.8899811598910946]), 
     qatom(atom.H, [21.229378435178518, -31.17337375836921, -0.8899811598910946]), 
     qatom(atom.C, [20.71554744209093, -33.08670727675352, 0.0]), 
     qatom(atom.H, [20.201716449003342, -33.45004079513784, 0.8899811598910946]), 
     qatom(atom.H, [20.201716449003342, -33.45004079513784, -0.8899811598910946]), 
     qatom(atom.C, [22.176901642615263, -33.60337341712841, 0.0]), 
     qatom(atom.H, [22.69073263570285, -33.240039898744094, 0.8899811598910946]), 
     qatom(atom.H, [22.69073263570285, -33.240039898744094, -0.8899811598910946]), 
     qatom(atom.C, [22.176901642615263, -35.15337341712841, 0.0]), 
     qatom(atom.H, [21.663070649527675, -35.51670693551272, 0.8899811598910946]), 
     qatom(atom.H, [21.663070649527675, -35.51670693551272, -0.8899811598910946]), 
     qatom(atom.C, [23.638255843139596, -35.670039557503294, 0.0]), 
     qatom(atom.H, [24.152086836227184, -35.30670603911898, 0.8899811598910946]), 
     qatom(atom.H, [24.152086836227184, -35.30670603911898, -0.8899811598910946]), 
     qatom(atom.C, [23.638255843139596, -37.22003955750329, 0.0]), 
     qatom(atom.H, [23.12442485005201, -37.58337307588761, 0.8899811598910946]), 
     qatom(atom.H, [23.12442485005201, -37.58337307588761, -0.8899811598910946]), 
     qatom(atom.C, [25.09961004366393, -37.73670569787818, 0.0]), 
     qatom(atom.H, [25.613441036751517, -37.37337217949386, 0.8899811598910946]), 
     qatom(atom.H, [25.613441036751517, -37.37337217949386, -0.8899811598910946]), 
     qatom(atom.C, [25.09961004366393, -39.286705697878176, 0.0]), 
     qatom(atom.H, [24.585779050576342, -39.65003921626249, 0.8899811598910946]), 
     qatom(atom.H, [24.585779050576342, -39.65003921626249, -0.8899811598910946]), 
     qatom(atom.C, [26.560964244188263, -39.803371838253064, 0.0]), 
     qatom(atom.H, [27.07479523727585, -39.44003831986875, 0.8899811598910946]), 
     qatom(atom.H, [27.07479523727585, -39.44003831986875, -0.8899811598910946]), 
     qatom(atom.C, [26.560964244188263, -41.35337183825306, 0.0]), 
     qatom(atom.H, [26.047133251100675, -41.71670535663738, 0.8899811598910946]), 
     qatom(atom.H, [26.047133251100675, -41.71670535663738, -0.8899811598910946]), 
     qatom(atom.C, [28.022318444712596, -41.87003797862795, 0.0]), 
     qatom(atom.H, [28.536149437800184, -41.50670446024363, 0.8899811598910946]), 
     qatom(atom.H, [28.536149437800184, -41.50670446024363, -0.8899811598910946]), 
     qatom(atom.C, [28.022318444712596, -43.420037978627946, 0.0]), 
     qatom(atom.H, [27.508487451625008, -43.78337149701226, 0.8899811598910946]), 
     qatom(atom.H, [27.508487451625008, -43.78337149701226, -0.8899811598910946]), 
     qatom(atom.C, [29.48367264523693, -43.93670411900283, 0.0]), 
     qatom(atom.H, [29.997503638324517, -43.57337060061852, 0.8899811598910946]), 
     qatom(atom.H, [29.997503638324517, -43.57337060061852, -0.8899811598910946]), 
     qatom(atom.C, [29.48367264523693, -45.48670411900283, 0.0]), 
     qatom(atom.H, [28.96984165214934, -45.850037637387146, 0.8899811598910946]), 
     qatom(atom.H, [28.96984165214934, -45.850037637387146, -0.8899811598910946]), 
     qatom(atom.C, [30.945026845761262, -46.00337025937772, 0.0]), 
     qatom(atom.H, [31.45885783884885, -45.6400367409934, 0.8899811598910946]), 
     qatom(atom.H, [31.45885783884885, -45.6400367409934, -0.8899811598910946]), 
     qatom(atom.C, [30.945026845761262, -47.553370259377715, 0.0]), 
     qatom(atom.H, [30.431195852673675, -47.91670377776203, 0.8899811598910946]), 
     qatom(atom.H, [30.431195852673675, -47.91670377776203, -0.8899811598910946]), 
     qatom(atom.C, [32.406381046285595, -48.0700363997526, 0.0]), 
     qatom(atom.H, [32.92021203937318, -47.70670288136829, 0.8899811598910946]), 
     qatom(atom.H, [32.92021203937318, -47.70670288136829, -0.8899811598910946]), 
     qatom(atom.C, [32.406381046285595, -49.6200363997526, 0.0]), 
     qatom(atom.H, [31.892550053198008, -49.983369918136916, 0.8899811598910946]), 
     qatom(atom.H, [31.892550053198008, -49.983369918136916, -0.8899811598910946]), 
     qatom(atom.C, [33.86773524680993, -50.13670254012749, 0.0]), 
     qatom(atom.H, [34.381566239897516, -49.77336902174317, 0.8899811598910946]), 
     qatom(atom.H, [34.381566239897516, -49.77336902174317, -0.8899811598910946]), 
     qatom(atom.C, [33.86773524680993, -51.686702540127484, 0.0]), 
     qatom(atom.H, [33.35390425372234, -52.0500360585118, 0.8899811598910946]), 
     qatom(atom.H, [33.35390425372234, -52.0500360585118, -0.8899811598910946]), 
     qatom(atom.C, [35.32908944733426, -52.20336868050237, 0.0]), 
     qatom(atom.H, [35.84292044042185, -51.840035162118056, 0.8899811598910946]), 
     qatom(atom.H, [35.84292044042185, -51.840035162118056, -0.8899811598910946]), 
     qatom(atom.H, [35.32908944733426, -53.293368680502375, 0.0]), 
] 

qatom.unit = unit.angstrom

qmolecule = molecule( geom, charge=0, mult=1, sym=sym.C1 )
print qmolecule

qatom.basis = baslib("def2-svp/jkfit")
#qatom.basis = baslib("aug-cc-pv5z-ri/jkfit")
#qatom.basis = myribasis
acene = [ i.new_basis() for i in geom]
qmolecule_RI_JK = molecule(acene, charge=0, mult=1, sym=sym.C1) # hojokitei in icmr module
casscf.no4c_RI_JK = True
hint.use_RI_JK = True
hint.itrf_RI_JK_memory = 2000

#qatom.basis = baslib("cc-pvdz-ri/mp2fit")
benzene = [ i.new_basis() for i in geom]
qmolecule_RI_C = molecule(benzene, charge=0, mult=1, sym=sym.C1) # hojokitei in lct module

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
casscf.frozen = [0]
casscf.closed = [218.0]
casscf.occ = [6]
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
icmr.frozen = [56]
icmr.closed = [162.0]
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
