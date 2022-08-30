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
qatom(atom.Co, [1.0691581, -0.4450992, 0.4986371]),
qatom(atom.C, [0.3262177, 1.9514574, -0.1115200]),
qatom(atom.C, [-0.0461521, 3.5010834, -0.0858507]),
qatom(atom.C, [1.4363490, 3.5695511, -0.6078316]),
qatom(atom.C, [1.9831024, 2.2115126, -0.2336511]),
qatom(atom.C, [3.3754081, 1.8768099, -0.2384306]),
qatom(atom.C, [3.7836060, 0.5614048, -0.1646195]),
qatom(atom.C, [5.2353463, 0.0658457, -0.2839559]),
qatom(atom.C, [5.0491543, -1.4775602, -0.4370946]),
qatom(atom.C, [3.6206734, -1.6812710, -0.0375193]),
qatom(atom.C, [3.1154748, -2.9498532, 0.2061703]),
qatom(atom.C, [1.8228698, -3.2429517, 0.5887021]),
qatom(atom.C, [1.3561349, -4.6326584, 0.9690693]),
qatom(atom.C, [-0.1816472, -4.4499140, 0.8684399]),
qatom(atom.C, [-0.3386134, -2.9605269, 1.1201914]),
qatom(atom.C, [-1.4945026, -2.3416391, 1.5634537]),
qatom(atom.C, [-1.6509273, -0.9257970, 1.4579487]),
qatom(atom.C, [-2.9290305, -0.1305314, 1.7549895]),
qatom(atom.C, [-2.6279089, 1.1865900, 0.9734136]),
qatom(atom.C, [-1.1088799, 1.3006962, 1.0501534]),
qatom(atom.C, [-0.8813632, 1.4700209, -1.4630421]),
qatom(atom.C, [-1.0496652, 4.3115677, -0.9149578]),
qatom(atom.C, [-0.0610793, 4.0329558, 1.3757343]),
qatom(atom.C, [0.1563766, 5.5414073, 1.4682774]),
qatom(atom.C, [1.6444455, 3.8787333, -2.1149000]),
qatom(atom.C, [1.8153975, 5.3830222, -2.3906384]),
qatom(atom.C, [3.2293088, 5.8326169, -2.0257772]),
qatom(atom.C, [4.3473354, 3.0324744, -0.3492095]),
qatom(atom.C, [6.0241838, 0.6976172, -1.4450400]),
qatom(atom.C, [5.9460806, 0.3382628, 1.0810874]),
qatom(atom.C, [7.4378059, 0.0144265, 1.0292497]),
qatom(atom.C, [5.3402197, -2.1315235, -1.8180711]),
qatom(atom.C, [6.7009317, -2.8345123, -1.8272647]),
qatom(atom.C, [6.6915191, -3.9807581, -0.8148544]),
qatom(atom.C, [1.7404739, -4.8635276, 2.4521163]),
qatom(atom.C, [1.9589690, -5.7452335, 0.1047226]),
qatom(atom.C, [-0.7349244, -4.8090710, -0.5362854]),
qatom(atom.C, [-2.2438815, -4.6379193, -0.6729944]),
qatom(atom.C, [-2.7381211, -4.9633359, -2.0843685]),
qatom(atom.C, [-2.5894793, -3.1853987, 2.1882201]),
qatom(atom.C, [-3.0405036, 0.1124007, 3.2750938]),
qatom(atom.C, [-3.4923634, 2.3974491, 1.3515236]),
qatom(atom.C, [-4.8555306, 2.2497413, 0.6689592]),
qatom(atom.C, [-4.2319004, -0.7677179, 1.2289901]),
qatom(atom.C, [-4.1967482, -1.1737934, -0.2538266]),
qatom(atom.C, [-5.5889373, -1.5740340, -0.7156021]),
qatom(atom.C, [-7.8217107, -0.6623739, -1.2510989]),
qatom(atom.C, [-8.5402954, 0.6759628, -1.1264463]),
qatom(atom.C, [-10.0097439, 0.5513809, -1.5050015]),
qatom(atom.H, [1.9603025, 4.3483624, -0.0473133]),
qatom(atom.H, [5.6931446, -1.9827701, 0.2888624]),
qatom(atom.H, [3.8133704, -3.7734963, 0.0857822]),
qatom(atom.H, [-0.6942404, -5.0570945, 1.6196295]),
qatom(atom.H, [-2.8581345, 0.9872782, -0.0748338]),
qatom(atom.H, [-0.7709266, 1.7360838, 1.9981366]),
qatom(atom.H, [-0.1979897, 1.7371729, -2.2712735]),
qatom(atom.H, [-1.8624994, 1.9011631, -1.6764847]),
qatom(atom.H, [-0.9774893, 0.3795850, -1.4515806]),
qatom(atom.H, [-2.0727227, 4.1556476, -0.5591465]),
qatom(atom.H, [-1.0306230, 4.0402128, -1.9707751]),
qatom(atom.H, [-0.8332424, 5.3805817, -0.8420425]),
qatom(atom.H, [0.7339403, 3.5469602, 1.9544384]),
qatom(atom.H, [-1.0135482, 3.7844289, 1.8533664]),
qatom(atom.H, [-0.7226512, 7.2325836, 2.2179665]),
qatom(atom.H, [-1.6308464, 5.7794298, 2.5084902]),
qatom(atom.H, [0.8126041, 3.4834681, -2.7032309]),
qatom(atom.H, [2.5432829, 3.3674348, -2.4733904]),
qatom(atom.H, [1.0608678, 5.9684794, -1.8579135]),
qatom(atom.H, [1.6996865, 5.5682422, -3.4628291]),
qatom(atom.H, [4.2507980, 6.9693994, -0.6742327]),
qatom(atom.H, [2.5439937, 6.8412056, -0.3455755]),
qatom(atom.H, [5.3037030, 2.8026094, 0.1180622]),
qatom(atom.H, [3.9445645, 3.9095388, 0.1641216]),
qatom(atom.H, [4.5456177, 3.3358499, -1.3821285]),
qatom(atom.H, [5.4141280, 0.7684686, -2.3486795]),
qatom(atom.H, [6.9002437, 0.0827106, -1.6668557]),
qatom(atom.H, [6.3794472, 1.6998239, -1.2047419]),
qatom(atom.H, [5.7919429, 1.3768809, 1.3861467]),
qatom(atom.H, [5.4912361, -0.2977874, 1.8487809]),
qatom(atom.H, [9.2685504, 0.8818430, 1.3380566]),
qatom(atom.H, [7.9268848, 1.9514298, 1.6148084]),
qatom(atom.H, [4.5759677, -2.8893774, -2.0115873]),
qatom(atom.H, [5.2766305, -1.3957760, -2.6233251]),
qatom(atom.H, [6.8821939, -3.2751287, -2.8147625]),
qatom(atom.H, [7.5162620, -2.1374471, -1.6129983]),
qatom(atom.H, [7.8013728, -4.7909145, 0.6871611]),
qatom(atom.H, [8.3972630, -3.2760585, 0.0911952]),
qatom(atom.H, [2.8273440, -4.8463599, 2.5737524]),
qatom(atom.H, [1.3695451, -5.8406305, 2.7786331]),
qatom(atom.H, [1.3043071, -4.0918519, 3.0961875]),
qatom(atom.H, [1.7974270, -5.5718779, -0.9615381]),
qatom(atom.H, [1.5123842, -6.7085658, 0.3717400]),
qatom(atom.H, [3.0371373, -5.8202533, 0.2740132]),
qatom(atom.H, [-0.4765992, -5.8470765, -0.7582071]),
qatom(atom.H, [-0.2289543, -4.1974565, -1.2922212]),
qatom(atom.H, [-2.5354835, -3.6125989, -0.4308957]),
qatom(atom.H, [-2.7732094, -5.2909855, 0.0327065]),
qatom(atom.H, [-4.4040097, -4.7975014, -3.2459660]),
qatom(atom.H, [-4.6078097, -4.0782538, -1.6719008]),
qatom(atom.H, [-2.1906224, -4.1495179, 2.5040082]),
qatom(atom.H, [-3.4307238, -3.3860530, 1.5192246]),
qatom(atom.H, [-2.9866718, -2.6986189, 3.0821903]),
qatom(atom.H, [-3.9686816, 0.6431380, 3.5116529]),
qatom(atom.H, [-2.1966392, 0.7005209, 3.6509769]),
qatom(atom.H, [-3.0586983, -0.8324054, 3.8227088]),
qatom(atom.H, [-3.5815933, 2.5305030, 2.4341403]),
qatom(atom.H, [-3.0447554, 3.3091545, 0.9427903]),
qatom(atom.H, [-6.8652471, 2.1051790, 1.0171837]),
qatom(atom.H, [-5.8998598, 2.4860960, 2.4301480]),
qatom(atom.H, [-5.0346835, -0.0393602, 1.3809636]),
qatom(atom.H, [-4.5080527, -1.6309580, 1.8372406]),
qatom(atom.H, [-3.8461134, -0.3414611, -0.8706703]),
qatom(atom.H, [-3.5234144, -2.0180510, -0.4085149]),
qatom(atom.H, [-6.0005427, 0.4197365, -0.9153373]),
qatom(atom.H, [-8.2573980, -1.3932215, -0.5620506]),
qatom(atom.H, [-7.9630939, -1.0420383, -2.2714643]),
qatom(atom.H, [-8.0470598, 1.4144895, -1.7751641]),
qatom(atom.H, [-10.5114766, -0.1851643, -0.8687822]),
qatom(atom.H, [-10.1121417, 0.2372381, -2.5481342]),
qatom(atom.H, [-10.5194027, 1.5162490, -1.3999488]),
qatom(atom.H, [-9.2025735, 1.6515211, 0.4573156]),
qatom(atom.N, [1.0324291, 1.3598697, 0.0585424]),
qatom(atom.N, [2.9269723, -0.5222522, 0.0437243]),
qatom(atom.N, [0.8385034, -2.3169424, 0.7613407]),
qatom(atom.N, [-0.6860141, -0.1272558, 1.0455795]),
qatom(atom.N, [-0.8291873, 6.2331373, 2.0968996]),
qatom(atom.N, [3.3256460, 6.6890130, -0.9733844]),
qatom(atom.N, [8.2694286, 1.0439755, 1.3366111]),
qatom(atom.N, [7.8025003, -4.0850726, -0.0387901]),
qatom(atom.N, [-4.0141896, -4.5674954, -2.3415368]),
qatom(atom.N, [-5.9646333, 2.3784057, 1.4279315]),
qatom(atom.N, [-6.4030756, -0.5197130, -0.9556961]),
qatom(atom.O, [1.1471674, 6.1129542, 1.0090951]),
qatom(atom.O, [4.2063954, 5.4297247, -2.6546591]),
qatom(atom.O, [7.8664024, -1.0974408, 0.7195978]),
qatom(atom.O, [5.7448258, -4.7666772, -0.7354195]),
qatom(atom.O, [-2.0307860, -5.5380913, -2.9078648]),
qatom(atom.O, [-4.9132454, 1.9981283, -0.5419462]),
qatom(atom.O, [-5.9501492, -2.7547893, -0.8046666]),
qatom(atom.O, [-8.4049056, 1.1379447, 0.2532657]),
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
# orig frozen ... 72.00
# orig closed ... 192.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [264]
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
icmr.frozen = [72]
icmr.closed = [192]
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

