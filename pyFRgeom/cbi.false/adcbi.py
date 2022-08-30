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
qatom(atom.Co, [-0.1325164, -0.2500157, -0.6640851]),
qatom(atom.C, [1.2383563, 1.3050202, 1.2901706]),
qatom(atom.C, [0.8644942, 2.0825335, 2.6078827]),
qatom(atom.C, [-0.2135818, 1.1429449, 3.2609898]),
qatom(atom.C, [-0.7983911, 0.4468599, 2.0562254]),
qatom(atom.C, [-2.0370616, -0.2812550, 2.0355519]),
qatom(atom.C, [-2.1928885, -1.3167204, 1.1413683]),
qatom(atom.C, [-3.2949951, -2.3885872, 1.1413554]),
qatom(atom.C, [-2.5741076, -3.5133478, 0.3227456]),
qatom(atom.C, [-1.6911602, -2.6872788, -0.5614163]),
qatom(atom.C, [-1.3778222, -2.9939214, -1.8776193]),
qatom(atom.C, [-0.5781618, -2.2326588, -2.7095936]),
qatom(atom.C, [-0.4252544, -2.4617825, -4.1985639]),
qatom(atom.C, [0.9253053, -1.7434170, -4.4639191]),
qatom(atom.C, [0.9727941, -0.7296173, -3.3336459]),
qatom(atom.C, [1.7960520, 0.3797112, -3.3191132]),
qatom(atom.C, [1.9010726, 1.2181956, -2.1633575]),
qatom(atom.C, [2.7839312, 2.4614098, -2.0126892]),
qatom(atom.C, [2.7429337, 2.6845951, -0.4638340]),
qatom(atom.C, [1.4067115, 2.0665084, -0.0477403]),
qatom(atom.C, [2.4248705, 0.3484323, 1.4580878]),
qatom(atom.C, [2.0517713, 2.3436667, 3.5399246]),
qatom(atom.C, [0.1724655, 3.4237837, 2.2522806]),
qatom(atom.C, [-0.2222809, 4.2240510, 3.4897283]),
qatom(atom.C, [0.3745881, 0.1353706, 4.2799085]),
qatom(atom.C, [-0.6261936, -0.8548758, 4.8923991]),
qatom(atom.C, [0.1193433, -1.9503371, 5.6384384]),
qatom(atom.C, [-3.1284136, 0.1428513, 2.9986601]),
qatom(atom.C, [-3.7887850, -2.8291305, 2.5272917]),
qatom(atom.C, [-4.4774823, -1.8662756, 0.2797571]),
qatom(atom.C, [-5.5457147, -2.9325015, -0.0315297]),
qatom(atom.C, [-1.7824142, -4.5470672, 1.1616100]),
qatom(atom.C, [-0.7030240, -4.0149862, 2.1095504]),
qatom(atom.C, [0.6414789, -3.7220536, 1.4542062]),
qatom(atom.C, [-1.5548768, -1.6514030, -4.8889433]),
qatom(atom.C, [-0.5120795, -3.9213094, -4.6502197]),
qatom(atom.C, [2.1623958, -2.6744948, -4.4781071]),
qatom(atom.C, [2.4600232, -3.4052346, -3.1573210]),
qatom(atom.C, [3.3454319, -2.6016238, -2.2160116]),
qatom(atom.C, [2.6216721, 0.6759326, -4.5534940]),
qatom(atom.C, [2.0970581, 3.6179546, -2.7778419]),
qatom(atom.C, [2.9579332, 4.1603183, -0.0886302]),
qatom(atom.C, [3.5574755, 4.4387172, 1.2820683]),
qatom(atom.C, [4.2577355, 2.3585626, -2.4693424]),
qatom(atom.C, [4.9756030, 1.0284086, -2.2397445]),
qatom(atom.C, [5.5398656, 0.7547498, -0.8503247]),
qatom(atom.C, [6.5311806, -1.0459108, 0.5169608]),
qatom(atom.C, [5.8931932, -2.2882088, 1.1450174]),
qatom(atom.C, [6.7028455, -2.7961126, 2.3317794]),
qatom(atom.N, [-0.0026118, 0.5100454, 1.0198611]),
qatom(atom.N, [-1.3365752, -1.5366358, 0.0589505]),
qatom(atom.N, [0.1291755, -1.1368293, -2.3121006]),
qatom(atom.N, [1.1555950, 1.0300847, -1.0923081]),
qatom(atom.N, [0.5374622, 5.3222694, 3.7077280]),
qatom(atom.N, [-0.1267492, -2.0597753, 6.9648136]),
qatom(atom.N, [-6.5223113, -2.5151758, -0.8856971]),
qatom(atom.N, [1.5574554, -3.1631506, 2.2721010]),
qatom(atom.N, [2.9464510, -2.5446816, -0.9351569]),
qatom(atom.N, [4.7186391, 3.8015007, 1.5500264]),
qatom(atom.N, [5.7999102, -0.5557628, -0.6403251]),
qatom(atom.O, [-1.1577782, 3.8805919, 4.2194710]),
qatom(atom.O, [0.9143009, -2.7030381, 5.0625394]),
qatom(atom.O, [-5.5312567, -4.0617519, 0.4533099]),
qatom(atom.O, [0.8614963, -3.9936321, 0.2623383]),
qatom(atom.O, [4.3883179, -2.0617830, -2.6346625]),
qatom(atom.O, [3.0258222, 5.2204511, 2.0820908]),
qatom(atom.O, [5.8011080, 1.6403706, -0.0172361]),
qatom(atom.O, [4.5179049, -2.0198869, 1.5303714]),
qatom(atom.C, [-1.7567646, 0.6605027, -1.3253577]),
qatom(atom.C, [-1.6035675, 1.9406155, -2.1248575]),
qatom(atom.C, [-1.6775033, 3.1895109, -1.2516500]),
qatom(atom.O, [-2.7660829, 2.0719283, -3.0291134]),
qatom(atom.C, [-3.1825312, 3.3624763, -1.0571857]),
qatom(atom.C, [-3.7643578, 2.8356309, -2.3956530]),
qatom(atom.C, [-5.9010449, 2.2807031, -1.1565493]),
qatom(atom.C, [-5.1866483, 0.7026691, -2.5291428]),
qatom(atom.C, [-6.6861460, 1.1281005, -1.0510320]),
qatom(atom.C, [-7.7010542, 1.1577503, -0.0688008]),
qatom(atom.C, [-7.0685694, 3.3378332, 0.4085109]),
qatom(atom.N, [-4.9373716, 1.9852845, -2.1025146]),
qatom(atom.N, [-6.2262103, 0.1525105, -1.9271549]),
qatom(atom.N, [-6.0395045, 3.4196444, -0.4540899]),
qatom(atom.N, [-7.8765923, 2.2969900, 0.6356762]),
qatom(atom.N, [-8.5059195, 0.1086290, 0.2060348]),
qatom(atom.O, [-1.1123459, 4.3112333, -1.9149963]),
qatom(atom.O, [-3.5016872, 4.7038702, -0.7683835]),
qatom(atom.H, [-0.9538660, 1.7661100, 3.7740218]),
qatom(atom.H, [-3.3012768, -4.0804391, -0.2594972]),
qatom(atom.H, [-1.8130493, -3.8978166, -2.2884057]),
qatom(atom.H, [0.8892581, -1.2392840, -5.4346900]),
qatom(atom.H, [3.5540123, 2.0859110, -0.0459693]),
qatom(atom.H, [0.6135623, 2.8124650, -0.1319738]),
qatom(atom.H, [3.3301848, 0.9071883, 1.7114517]),
qatom(atom.H, [2.5985113, -0.1879121, 0.5226834]),
qatom(atom.H, [2.2263987, -0.3901739, 2.2351051]),
qatom(atom.H, [2.5795809, 1.4240673, 3.7987969]),
qatom(atom.H, [2.7639979, 3.0341288, 3.0901600]),
qatom(atom.H, [1.6985461, 2.8010738, 4.4690981]),
qatom(atom.H, [-0.7478538, 3.2251469, 1.6925836]),
qatom(atom.H, [0.8368704, 4.0273696, 1.6313139]),
qatom(atom.H, [1.1655113, -0.4548424, 3.8113858]),
qatom(atom.H, [0.8349936, 0.7099894, 5.0890373]),
qatom(atom.H, [-1.1839390, -1.3580145, 4.0956622]),
qatom(atom.H, [-1.3456937, -0.3391335, 5.5362935]),
qatom(atom.H, [-4.1062220, 0.0820949, 2.5149880]),
qatom(atom.H, [-3.1785431, -0.4586871, 3.9106620]),
qatom(atom.H, [-2.9745901, 1.1830593, 3.2965734]),
qatom(atom.H, [-4.5121511, -2.1174398, 2.9307574]),
qatom(atom.H, [-2.9687368, -2.9201203, 3.2443848]),
qatom(atom.H, [-4.2950061, -3.7903065, 2.4369551]),
qatom(atom.H, [-4.9669065, -1.0256201, 0.7854087]),
qatom(atom.H, [-4.0985023, -1.4704888, -0.6703217]),
qatom(atom.H, [-1.3164081, -5.2530641, 0.4669493]),
qatom(atom.H, [-2.5194991, -5.1068888, 1.7447599]),
qatom(atom.H, [-1.0266460, -3.1110891, 2.6355015]),
qatom(atom.H, [-0.5183390, -4.7592956, 2.8941586]),
qatom(atom.H, [-2.5363404, -2.0416254, -4.6019238]),
qatom(atom.H, [-1.4532520, -1.7316539, -5.9762618]),
qatom(atom.H, [-1.5053952, -0.5930383, -4.6124421]),
qatom(atom.H, [-1.5227461, -4.3093397, -4.4880299]),
qatom(atom.H, [-0.3059513, -3.9940498, -5.7226873]),
qatom(atom.H, [0.1888887, -4.5690356, -4.1189278]),
qatom(atom.H, [3.0502762, -2.0960797, -4.7493887]),
qatom(atom.H, [2.0095180, -3.4081810, -5.2753835]),
qatom(atom.H, [1.5487417, -3.7191413, -2.6401197]),
qatom(atom.H, [3.0270761, -4.3153016, -3.3874338]),
qatom(atom.H, [3.5959649, 0.1764519, -4.5255859]),
qatom(atom.H, [2.7985547, 1.7447216, -4.6671171]),
qatom(atom.H, [2.1059257, 0.3388318, -5.4546352]),
qatom(atom.H, [1.1113010, 3.8576651, -2.3717918]),
qatom(atom.H, [2.7181608, 4.5181177, -2.7357973]),
qatom(atom.H, [1.9706904, 3.3587800, -3.8323398]),
qatom(atom.H, [2.0288056, 4.7290680, -0.1655130]),
qatom(atom.H, [3.6598078, 4.5966411, -0.8108386]),
qatom(atom.H, [4.3211643, 2.5960910, -3.5344814]),
qatom(atom.H, [4.8084041, 3.1563891, -1.9538654]),
qatom(atom.H, [5.8489917, 0.9959186, -2.9051285]),
qatom(atom.H, [4.3587170, 0.1744904, -2.5313137]),
qatom(atom.H, [6.5738945, -0.2272139, 1.2436151]),
qatom(atom.H, [7.5647270, -1.2899287, 0.2361690]),
qatom(atom.H, [5.7992222, -3.0773710, 0.3906600]),
qatom(atom.H, [6.2153635, -3.6676409, 2.7754448]),
qatom(atom.H, [7.7112198, -3.0840278, 2.0170305]),
qatom(atom.H, [6.7955705, -2.0184599, 3.0992701]),
qatom(atom.H, [0.3582006, 5.8797509, 4.5328249]),
qatom(atom.H, [1.3654530, 5.5089422, 3.1427910]),
qatom(atom.H, [0.3507601, -2.7759483, 7.4973975]),
qatom(atom.H, [-0.7681880, -1.4449471, 7.4436848]),
qatom(atom.H, [-6.4289463, -1.6402002, -1.4251582]),
qatom(atom.H, [-7.1601931, -3.2308911, -1.2140986]),
qatom(atom.H, [1.3503777, -3.0068667, 3.2647974]),
qatom(atom.H, [2.5146182, -3.0426060, 1.9550284]),
qatom(atom.H, [3.5580425, -2.1279298, -0.2346326]),
qatom(atom.H, [2.1562984, -3.1084445, -0.5850876]),
qatom(atom.H, [5.1617100, 3.1483030, 0.8980554]),
qatom(atom.H, [5.1865703, 4.0141316, 2.4214081]),
qatom(atom.H, [5.4893531, -1.2126308, -1.3731496]),
qatom(atom.H, [4.5168657, -1.2243784, 2.0884056]),
qatom(atom.H, [-2.2223017, -0.1033527, -1.9525679]),
qatom(atom.H, [-2.3546012, 0.8099422, -0.4210978]),
qatom(atom.H, [-0.7349614, 1.9366494, -2.7838068]),
qatom(atom.H, [-1.1937574, 3.0175984, -0.2828897]),
qatom(atom.H, [-3.5165465, 2.7009985, -0.2478607]),
qatom(atom.H, [-4.0739731, 3.6536884, -3.0533672]),
qatom(atom.H, [-4.5633153, 0.2305145, -3.2732619]),
qatom(atom.H, [-7.2604833, 4.2250268, 1.0062481]),
qatom(atom.H, [-8.2822595, -0.8125909, -0.1464174]),
qatom(atom.H, [-9.1422736, 0.1943229, 0.9868880]),
qatom(atom.H, [-1.6355106, 5.0863310, -1.6339158]),
qatom(atom.H, [-4.4662694, 4.6859766, -0.5559616]),
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

acene = [ i.new_basis() for i in geom]
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
# orig frozen ... 90.00
# orig closed ... 239.50
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [330]
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
icmr.frozen = [90]
icmr.closed = [240]
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
lct.TCutDOI_PAO = 1e-2
lct.UseNewDomain = True
lct.FormLVOs = True
lct.UseVM1_CD   = True
lct.UseVM12     = (not lct.UseVM1_CD)

lct.PrintPairDistDBG = True
lct.PrintMapsDBG     = True

lct.LocMet = "PSM"
lct.LocRecursive = True
lct.LocMeasure = True
hint.nroots = 1
hint.nconvroots = 1

# new PMNR scheme threshold (impl = sparse, locrec = True)
lct.PMMaxIt = 3
lct.PMStep = 0.01
lct.GThresh = 5.0e-3
lct.IterLevel = 2
hint.PM_trunc_thresh = 1e-1
hint.PM_AB_thresh = 1e-4
hint.PM_ang_thresh = 1e-6
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
lct.TCutDOI = 1e-3

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

