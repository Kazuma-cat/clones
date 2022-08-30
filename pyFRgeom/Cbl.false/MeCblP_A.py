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
qatom(atom.Co, [1.0384053, -0.4167239, 0.4974171]),
qatom(atom.C, [-0.3726942, 1.9567218, -0.2091555]),
qatom(atom.C, [-0.0938783, 3.5059703, -0.1794849]),
qatom(atom.C, [1.3918382, 3.5746882, -0.6887237]),
qatom(atom.C, [1.9338629, 2.2207221, -0.2985117]),
qatom(atom.C, [3.3260563, 1.8920782, -0.2806774]),
qatom(atom.C, [3.7301219, 0.5749468, -0.2390275]),
qatom(atom.C, [5.1792623, 0.0783705, -0.3691646]),
qatom(atom.C, [4.9853906, -1.4595729, -0.5540136]),
qatom(atom.C, [3.5615868, -1.6621785, -0.1391395]),
qatom(atom.C, [3.0637229, -2.9275784, 0.1299077]),
qatom(atom.C, [1.7752975, -3.2174912, 0.5245269]),
qatom(atom.C, [1.3172911, -4.6036837, 0.9261322]),
qatom(atom.C, [-0.2205544, -4.4287476, 0.8299525]),
qatom(atom.C, [-0.3798444, -2.9373436, 1.0663129]),
qatom(atom.C, [-1.5344632, -2.3198073, 1.5116444]),
qatom(atom.C, [-1.7007580, -0.9090936, 1.3727611]),
qatom(atom.C, [-2.9813420, -0.1143460, 1.6561054]),
qatom(atom.C, [-2.6806353, 1.1943798, 0.8606983]),
qatom(atom.C, [-1.1620039, 1.3065508, 0.9428518]),
qatom(atom.C, [-0.9141054, 1.4775560, -1.5667328]),
qatom(atom.C, [-1.0882288, 4.3196294, -1.0159826]),
qatom(atom.C, [-0.1184595, 4.0340747, 1.2836254]),
qatom(atom.C, [0.1025414, 5.5413708, 1.3801570]),
qatom(atom.C, [1.6155298, 3.8791393, -2.1942657]),
qatom(atom.C, [1.7960451, 5.3821623, -2.4703253]),
qatom(atom.C, [3.2062088, 5.8262319, -2.0853493]),
qatom(atom.C, [4.2964659, 3.0504967, -0.3531420]),
qatom(atom.C, [5.9701990, 0.7330735, -1.5155969]),
qatom(atom.C, [5.8878823, 0.3153340, 1.0029695]),
qatom(atom.C, [7.3795415, -0.0092109, 0.9464725]),
qatom(atom.C, [5.2559093, -2.0852314, -1.9514356]),
qatom(atom.C, [6.6161402, -2.7876717, -1.9928836]),
qatom(atom.C, [6.6253183, -3.9478760, -0.9964634]),
qatom(atom.C, [1.7082945, -4.8068208, 2.4115745]),
qatom(atom.C, [1.9210568, -5.7272981, 0.0773052]),
qatom(atom.C, [-0.7797594, -4.8096114, -0.5662176]),
qatom(atom.C, [-2.2907151, -4.6508643, -0.6951344]),
qatom(atom.C, [-2.7920297, -5.0101947, -2.0960350]),
qatom(atom.C, [-2.6203805, -3.1593511, 2.1557426]),
qatom(atom.C, [-3.0918328, 0.1498675, 3.1730689]),
qatom(atom.C, [-3.5424671, 2.4097871, 1.2293545]),
qatom(atom.C, [-4.9142594, 2.2485863, 0.5678175]),
qatom(atom.C, [-4.2815948, -0.7641350, 1.1400819]),
qatom(atom.C, [-4.2461255, -1.1841031, -0.3388027]),
qatom(atom.C, [-5.6370007, -1.5970393, -0.7933859]),
qatom(atom.C, [-7.8734584, -0.6952466, -1.3367606]),
qatom(atom.C, [-8.6023806, 0.6302959, -1.1419813]),
qatom(atom.C, [-10.0794202, 0.5062681, -1.4883711]),
qatom(atom.H, [1.9103434, 4.3555390, -0.1256218]),
qatom(atom.H, [5.6351444, -1.9831528, 0.1530562]),
qatom(atom.H, [3.7627777, -3.7509677, 0.0139818]),
qatom(atom.H, [-0.7274194, -5.0271087, 1.5921248]),
qatom(atom.H, [-2.9098298, 0.9864560, -0.1861316]),
qatom(atom.H, [-0.8262346, 1.7342120, 1.8955045]),
qatom(atom.H, [-0.2215109, 1.7432599, -2.3676098]),
qatom(atom.H, [-1.8909637, 1.9137630, -1.7894800]),
qatom(atom.H, [-1.0131308, 0.3880841, -1.5563922]),
qatom(atom.H, [-2.1149211, 4.1667900, -0.6696091]),
qatom(atom.H, [-1.0600701, 4.0492314, -2.0718376]),
qatom(atom.H, [-0.8693826, 5.3880092, -0.9398062]),
qatom(atom.H, [0.6705187, 3.5431407, 1.8663069]),
qatom(atom.H, [-1.0752496, 3.7867652, 1.7531892]),
qatom(atom.H, [-0.7880675, 7.2371527, 2.1056552]),
qatom(atom.H, [-1.7061988, 5.7872267, 2.3802179]),
qatom(atom.H, [0.7878964, 3.4866779, -2.7903852]),
qatom(atom.H, [2.5159363, 3.3632309, -2.5425113]),
qatom(atom.H, [1.0360097, 5.9714663, -1.9496033]),
qatom(atom.H, [1.6965742, 5.5663934, -3.5443409]),
qatom(atom.H, [4.2139037, 6.9616014, -0.7231961]),
qatom(atom.H, [2.5026614, 6.8425458, -0.4178547]),
qatom(atom.H, [5.2550808, 2.8045618, 0.1005505]),
qatom(atom.H, [3.8932142, 3.9079660, 0.1926093]),
qatom(atom.H, [4.4889444, 3.3899709, -1.3762416]),
qatom(atom.H, [5.3605387, 0.8241741, -2.4176784]),
qatom(atom.H, [6.8454391, 0.1218557, -1.7499432]),
qatom(atom.H, [6.3265058, 1.7297203, -1.2539401]),
qatom(atom.H, [5.7347301, 1.3457154, 1.3351504]),
qatom(atom.H, [5.4295481, -0.3382476, 1.7539810]),
qatom(atom.H, [9.2080592, 0.8349939, 1.3250313]),
qatom(atom.H, [7.8652030, 1.8909833, 1.6447846]),
qatom(atom.H, [4.4884476, -2.8392382, -2.1481710]),
qatom(atom.H, [5.1813312, -1.3335842, -2.7410987]),
qatom(atom.H, [6.7822688, -3.2137627, -2.9894860]),
qatom(atom.H, [7.4347532, -2.0934243, -1.7820128]),
qatom(atom.H, [7.7766360, -4.7971273, 0.4516427]),
qatom(atom.H, [8.3735560, -3.2831430, -0.1429877]),
qatom(atom.H, [2.7956503, -4.7847617, 2.5285621]),
qatom(atom.H, [1.3408911, -5.7785277, 2.7576430]),
qatom(atom.H, [1.2731564, -4.0241063, 3.0430307]),
qatom(atom.H, [1.7558803, -5.5705202, -0.9909859]),
qatom(atom.H, [1.4783067, -6.6878966, 0.3600572]),
qatom(atom.H, [3.0000193, -5.7968407, 0.2440569]),
qatom(atom.H, [-0.5165892, -5.848865, -0.7762615]),
qatom(atom.H, [-0.2826108, -4.204758, -1.3333628]),
qatom(atom.H, [-2.5882284, -3.622966, -0.4716082]),
qatom(atom.H, [-2.8101593, -5.293459, 0.0274237]),
qatom(atom.H, [-4.4622183, -4.871729, -3.2543671]),
qatom(atom.H, [-4.6592491, -4.113073, -1.6978903]),
qatom(atom.H, [-2.2124997, -4.112415, 2.4930041]),
qatom(atom.H, [-3.4587871, -3.381959, 1.4900983]),
qatom(atom.H, [-3.0233326, -2.655841, 3.0374844]),
qatom(atom.H, [-4.0204028, 0.6830026, 3.4023609]),
qatom(atom.H, [-2.2484005, 0.7444166, 3.5397711]),
qatom(atom.H, [-3.1086275, -0.786490, 3.7348183]),
qatom(atom.H, [-3.6173874, 2.5608135, 2.3107114]),
qatom(atom.H, [-3.1015399, 3.3146760, 0.7990988]),
qatom(atom.H, [-6.9180576, 2.0981215, 0.9516320]),
qatom(atom.H, [-5.9313289, 2.5053039, 2.3412923]),
qatom(atom.H, [-5.0898638, -0.041030, 1.2871856]),
qatom(atom.H, [-4.5493895, -1.624164, 1.7567622]),
qatom(atom.H, [-3.9014528, -0.355434, -0.9638360]),
qatom(atom.H, [-3.5675738, -2.025488, -0.4866068]),
qatom(atom.H, [-6.0536115, 0.3918685, -1.0198711]),
qatom(atom.H, [-8.2877431, -1.460810, -0.6730404]),
qatom(atom.H, [-8.0277958, -1.031132, -2.3709169]),
qatom(atom.H, [-8.1327038, 1.3978898, -1.7736949]),
qatom(atom.H, [-10.5595973, -0.2563935, -0.8657844]),
qatom(atom.H, [-10.2053488, 0.2244491, -2.5380613]),
qatom(atom.H, [-10.5934115, 1.4627837, -1.3392558]),
qatom(atom.H, [-9.2723658, 1.4439507, 0.5306429]),
qatom(atom.N, [0.9849571, 1.3619260, -0.0220667]),
qatom(atom.N, [2.8645255, -0.5057934, -0.0586327]),
qatom(atom.N, [0.7892933, -2.2893199, 0.6870489]),
qatom(atom.N, [-0.7398378, -0.1194507, 0.9359158]),
qatom(atom.N, [-0.8956226, 6.2379927, 1.9831113]),
qatom(atom.N, [3.2914901, 6.6867225, -1.0357026]),
qatom(atom.N, [8.2094298, 1.0000090, 1.3193486]),
qatom(atom.N, [7.7628035, -4.0812644, -0.2643051]),
qatom(atom.N, [-4.0689114, -4.6205048, -2.3571040]),
qatom(atom.N, [-6.0122278, 2.3835809, 1.3418692]),
qatom(atom.N, [-6.4525941, -0.5493548, -1.0555304]),
qatom(atom.O, [1.1061124, 6.1084071, 0.9432939]),
qatom(atom.O, [4.1908837, 5.4148821, -2.6973038]),
qatom(atom.O, [7.8094066, -1.1030870, 0.5800950]),
qatom(atom.O, [5.6705990, -4.7212308, -0.8931361]),
qatom(atom.O, [-2.0887195, -5.6066352, -2.9075268]),
qatom(atom.O, [-4.9878754, 1.9813220, -0.6387401]),
qatom(atom.O, [-5.9948760, -2.7804924, -0.8582659]),
qatom(atom.O, [-8.4330805, 1.0482531, 0.2480600]),
qatom(atom.C, [1.6424662, -0.1294351, 2.3338095]),
qatom(atom.H, [0.7766927, -0.1864615, 2.9957766]),
qatom(atom.H, [2.3582492, -0.9227636, 2.5569459]),
qatom(atom.H, [2.1145890, 0.8552788, 2.3653842]),
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
# orig frozen ... 73.00
# orig closed ... 195.50
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [269]
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
icmr.frozen = [73]
icmr.closed = [196]
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

