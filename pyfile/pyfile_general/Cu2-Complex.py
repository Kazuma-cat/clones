from sci import *

import os

qatom.basis = baslib("sto-3g")
qatom.basis = baslib("def2-tzvp")
class mybasis:
    C = baslib("def2-asvp").C
    O = baslib("def2-asvp").O
    N = baslib("def2-asvp").N
    S = baslib("def2-asvp").S
    H = baslib("def2-sv(p)").H
class myribasis:
    C = baslib("def2-asvp/jkfit").C
    O = baslib("def2-asvp/jkfit").O
    N = baslib("def2-asvp/jkfit").N
    S = baslib("def2-asvp/jkfit").S
    H = baslib("def2-svp/jkfit").H
#qatom.basis = mybasis

geom = convert_g09("""
Cu   -1.4673600000000000   1.6370100000000001  -1.5762300000000000
O    -1.7093300000000000   0.0850100000000000  -0.3825000000000000
O     0.5890700000000000   1.3402099999999999  -0.9351500000000000
C    -0.6487400000000000  -0.3650600000000000   0.1716100000000000
N    -1.2004699999999999   3.2680199999999999  -2.7240099999999998
N    -3.0385599999999999   2.6879300000000002  -0.6980900000000000
N    -1.3597200000000000   0.4650700000000000  -3.4308299999999998
C    -2.2121700000000000   4.2706799999999996  -2.3604200000000000
C    -3.2813400000000001   3.7631000000000001  -1.6361500000000000
C    -1.5107299999999999   2.8054500000000000  -4.1201999999999996
C    -0.9250699999999999   1.4827399999999999  -4.3979799999999996
C     0.1742700000000000   3.8406099999999999  -2.7007400000000006
C     0.6372200000000000   4.4057000000000004  -1.4019999999999999
C    -2.7656000000000001   3.2580200000000001   0.5802900000000000
C    -2.0346199999999999   2.7454399999999999   1.5678000000000001
C    -4.2421699999999998   1.8803000000000001  -0.6922700000000001
C    -5.5327200000000003   2.5454100000000000  -0.3214100000000000
C    -0.3447800000000000  -0.5875899999999999  -3.3755600000000006
C    -0.0865300000000000  -1.3877200000000001  -4.6350400000000000
C    -2.6728000000000001  -0.0625100000000000  -3.8540500000000000
C    -3.1981400000000000  -1.1726900000000000  -3.0163400000000000
H    -1.2759100000000001   3.4305500000000002  -4.7993800000000002
H    -2.5103100000000000   2.6854300000000002  -4.2278200000000004
H     0.0618000000000000   1.5452500000000000  -4.3209000000000000
H    -1.0710599999999999   1.1551800000000001  -5.3055000000000003
H     0.2552400000000000   4.5482300000000002  -3.3682900000000000
H     0.8131000000000000   3.1605099999999999  -2.9596200000000001
H     1.5341400000000001   4.7707600000000019  -1.4165399999999999
H     0.0605500000000000   5.1383200000000002  -1.0994900000000001
H     0.6184100000000000   3.7481000000000000  -0.6908200000000000
H    -3.6135799999999998   3.6280800000000002   0.8987900000000000
H    -2.2684799999999998   4.1406599999999996   0.3199600000000000
H    -1.9533900000000000   3.2680199999999999   2.3604200000000000
H    -2.5336400000000001   1.9078100000000000   1.8877600000000001
H    -1.1876100000000001   2.4203899999999998   1.3103800000000001
H    -4.1086700000000000   1.1251800000000001  -0.0669000000000000
H    -4.3678699999999999   1.4502299999999999  -1.5619799999999999
H    -6.3024199999999997   1.9503100000000000  -0.3112300000000000
H    -5.4887699999999997   2.9354700000000000   0.5672000000000000
H    -5.7480200000000004   3.2630200000000000  -0.9264300000000001
H    -0.5540300000000002  -1.2226999999999999  -2.6396600000000001
H     0.5080800000000000  -0.1950300000000000  -3.1123300000000009
H     0.5664600000000000  -2.0853299999999999  -4.5419600000000004
H    -0.9287700000000003  -1.8703000000000001  -4.8939100000000000
H     0.1343200000000000  -0.8451400000000000  -5.3665799999999999
H    -2.6776499999999999  -0.3375500000000000  -4.7732000000000001
H    -3.3486400000000001   0.6801100000000000  -3.8133300000000001
H    -4.0647300000000000  -1.4802400000000000  -3.2781199999999999
H    -2.5930499999999999  -1.9128099999999999  -3.0454300000000001
H    -3.2650299999999999  -0.8951400000000003  -2.0855500000000000
H    -2.5184400000000000   4.7732599999999996  -3.1472300000000000
H    -1.8332900000000001   4.9432900000000002  -1.7655900000000000
H    -3.9343300000000001   3.4130500000000001  -2.4026000000000001
H    -3.8290999999999999   4.4907199999999996  -1.2900199999999999
C     0.6487400000000000   0.3650600000000000  -0.1716100000000000
O    -0.5890700000000000  -1.3402099999999999   0.9351500000000000
O     1.7093300000000000  -0.0850100000000000   0.3825000000000000
Cu    1.4673600000000000  -1.6370100000000001   1.5762300000000000
N     1.2004699999999999  -3.2680199999999999   2.7240099999999998
N     3.0385599999999999  -2.6879300000000002   0.6980900000000000
N     1.3597200000000000  -0.4650700000000000   3.4308299999999998
C     2.2121700000000000  -4.2706799999999996   2.3604200000000000
C     1.5107299999999999  -2.8054500000000000   4.1201999999999996
C    -0.1742700000000000  -3.8406099999999999   2.7007400000000006
C     3.2813400000000001  -3.7631000000000001   1.6361500000000000
C     2.7656000000000001  -3.2580200000000001  -0.5802900000000000
C     4.2421699999999998  -1.8803000000000001   0.6922700000000001
C     0.9250699999999999  -1.4827399999999999   4.3979799999999996
C     0.3447800000000000   0.5875899999999999   3.3755600000000006
C     2.6728000000000001   0.0625100000000000   3.8540500000000000
H     2.5184400000000000  -4.7732599999999996   3.1472300000000000
H     1.8332900000000001  -4.9432900000000002   1.7655900000000000
H     1.2759100000000001  -3.4305500000000002   4.7993800000000002
H     2.5103100000000000  -2.6854300000000002   4.2278200000000004
C    -0.6372200000000000  -4.4057000000000004   1.4019999999999999
H    -0.2552400000000000  -4.5482300000000002   3.3682900000000000
H    -0.8131000000000000  -3.1605099999999999   2.9596200000000001
H     3.9343300000000001  -3.4130500000000001   2.4026000000000001
H     3.8290999999999999  -4.4907199999999996   1.2900199999999999
C     2.0346199999999999  -2.7454399999999999  -1.5678000000000001
H     3.6135799999999998  -3.6280800000000002  -0.8987900000000000
H     2.2684799999999998  -4.1406599999999996  -0.3199600000000000
C     5.5327200000000003  -2.5454100000000000   0.3214100000000000
H     4.1086700000000000  -1.1251800000000001   0.0669000000000000
H     4.3678699999999999  -1.4502299999999999   1.5619799999999999
H    -0.0618000000000000  -1.5452500000000000   4.3209000000000000
H     1.0710599999999999  -1.1551800000000001   5.3055000000000003
C     0.0865300000000000   1.3877200000000001   4.6350400000000000
H     0.5540300000000002   1.2226999999999999   2.6396600000000001
H    -0.5080800000000000   0.1950300000000000   3.1123300000000009
C     3.1981400000000000   1.1726900000000000   3.0163400000000000
H     2.6776499999999999   0.3375500000000000   4.7732000000000001
H     3.3486400000000001  -0.6801100000000000   3.8133300000000001
H    -1.5341400000000001  -4.7707600000000019   1.4165399999999999
H    -0.0605500000000000  -5.1383200000000002   1.0994900000000001
H    -0.6184100000000000  -3.7481000000000000   0.6908200000000000
H     1.9533900000000000  -3.2680199999999999  -2.3604200000000000
H     2.5336400000000001  -1.9078100000000000  -1.8877600000000001
H     1.1876100000000001  -2.4203899999999998  -1.3103800000000001
H     6.3024199999999997  -1.9503100000000000   0.3112300000000000
H     5.4887699999999997  -2.9354700000000000  -0.5672000000000000
H     5.7480200000000004  -3.2630200000000000   0.9264300000000001
H    -0.5664600000000000   2.0853299999999999   4.5419600000000004
H     0.9287700000000003   1.8703000000000001   4.8939100000000000
H    -0.1343200000000000   0.8451400000000000   5.3665799999999999
H     4.0647300000000000   1.4802400000000000   3.2781199999999999
H     2.5930499999999999   1.9128099999999999   3.0454300000000001
H     3.2650299999999999   0.8951400000000003   2.0855500000000000
                """)
qatom.unit = unit.angstrom

#qmolecule = molecule( geom, charge=2, mult=3, sym=sym.C1 )
qmolecule = molecule( geom, charge=2, mult=1, sym=sym.C1 )
print qmolecule

qatom.basis = baslib("def2-tzvpp/jkfit")
#qatom.basis = myribasis
acene = [ i.new_basis() for i in geom]
qmolecule_RI_JK = molecule(acene, charge=0, mult=1, sym=sym.C1)
casscf.no4c_RI_JK = True
hint.use_RI_JK = True
hint.itrf_RI_JK_memory = 2000

qmolecule_RI_C = qmolecule_RI_JK

#qrel.sr1e = "dk2"
#prop.dipmom = True
#prop.soc = True
#qrel.so1e = "dk1"

scf.maxloop = 300
scf.tol_density = 1e-4

## Generate int
scf.maxloop = 0
scf.guess = "moread"

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
casscf.closed = [188-1]
casscf.occ    = [ 2  ]
#casscf.roots = {1.0:7}
casscf.roots = {1.0:1}

##-#
#occ_active = [167,168,169,170] # avigadro ordering
#vir_active = [171,172,177,181] # avigadro ordering
#occ_active = map((lambda x : x-1), occ_active) # C/C++ ordering
#vir_active = map((lambda x : x-1), vir_active) # C/C++ ordering
#
#active = occ_active+vir_active
#docc   = filter(lambda x: not x in occ_active, range(0,170))
#
#casscf.scfinp = key.scfread
#casscf.orbconfig = "orblist"
#casscf.frozen = []
#casscf.closed = docc
#casscf.occ    = active
##-#

casscf.maxMacroloop = 100
casscf.tolMacroloop = 5e-5

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
icmr.frozen = [52]
icmr.closed = [188-1-52]
icmr.occ    = [2]
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
#icmr.pt.toliter = 1e-10
icmr.pt.toliter = 9e-7
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

scf.dft_ang = 11
scf.dft_intacc  = 13. / 3.

#OLD# lct.TCutPre = 1.0e-6

lct.DoPNO = False

# LCT
lct.test        = False
lct.DoPNO       = True
lct.UseOrthPNOs = True

lct.DoLoc       = True

lct.DoCEPT2     = True
lct.Make4EXT    = False

lct.TCutPNOrho0 = 1e-8
lct.TCutPNOrho1 = 1e-8
lct.TCutPNOrho2 = 1e-8
lct.TCutPairs   = 5e-6

lct.TCutPre = 1e-6
#lct.TCutPre = 0.0

#lct.TCutPNOrho0 = 0.0
#lct.TCutPNOrho1 = 0.0
#lct.TCutPNOrho2 = 0.0
#lct.TCutPairs   = 0.0

lct.MaxIter = 50
lct.NewTrafo    = True

### For testing performance of PNO-CASPT2 #####
lct.DoCEPT2     = False
lct.NNewTrafo   = True
lct.NewTrafo    = (not lct.NNewTrafo)
lct.TrafoMode   = "Disk"
lct.OVLMode     = "Disk"
#lct.InfoMode    = "Disk"
#lct.NSegments   = 2
#lct.StackSize   = 30000000
#lct.UseStackKij = True #
lct.NewAlgoPNO  = True
# Use of Local PAO/PNO
#lct.UsePAOs     = True
lct.UseVM1_CD   = True
lct.UseVM12     = (not lct.UseVM1_CD)

# Just for debugging PAO-based implementation
#lct.TCutMKN      = 1e-3
#lct.TCutMKNFit   = 0.0
#lct.DoHylleraas  = False
#lct.DoFullCASPT2 = False

#lct.TCutDeloc        = 0.03
lct.PrintPairDistDBG = True
lct.PrintMapsDBG     = True

lct.UseCholeskyOrb  = True
#lct.LocMet          = "FB"
#lct.LocMet          = "PSM"
#lct.LocMet          = "FBNR"
lct.LocPower        = 1
#hint.loc_thresh     = 1e-14
hint.randomize      = False
hint.maximize_niter = 2000
hint.nmicroiter     = 20000

lct.UsePAOs = False
lct.FormLVOs = True
lct.RIMP2 = False 
lct.LocMet = "PMNR"
hint.isOnTheFly = True
hint.ChargeType = "Loewdin"
hint.ImplTypePM = "incore"
hint.PMNRdebug = "debug"

hint.jacobi_thresh  = 1e-5
hint.cg_thresh      = 1e-5
hint.loc_thresh     = 1e-5
hint.res_tol        = 1e-5
hint.nroots         = 1
hint.nconvroots     = 1
hint.maxdvd         = 100
hint.stepThresh     = 0.2
#hint.PSMVersion     = 2
hint.fastConv       = False
hint.print_dvd      = True
lct.LocRecursive    = True
lct.LocMeasure      = True
#lct.FormLVOs        = False
lct.UseJacobiGuess  = True
# LVO truncation therhold
lct.DomScheme       = "Scheme1"
lct.TCutCRV         = 99.0
lct.TCutDOI         = 1e-3
lct.TCutVDO         = 1e-2

#hint.jacobi_thresh=1e-5

#lct.RIMP2 = True
lct.DoFullCASPT2 = True

#TIGHT# ###
#TIGHT# lct.TCutPNOrho0 = 5e-9
#TIGHT# lct.TCutPNOrho1 = 1e-8
#TIGHT# lct.TCutPNOrho2 = 1e-8
#TIGHT# lct.TCutPairs   = 3e-6
#TIGHT# lct.TCutPre     = 5e-7
