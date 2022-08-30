from sci import *

import os

qatom.basis = baslib("sto-3g")
#qatom.basis = baslib("def2-svp")

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
    
qatom.basis = mybasis

geom = convert_g09("""
S         -2.72257       -1.58165       -2.40087
O          2.77628       -2.25715       -1.92852
N          0.52366       -1.62455       -1.89200
C         -1.65219       -0.37985       -1.68230
C         -3.76341        0.62126       -1.56509
H         -4.49688        1.37535       -1.31909
C         -2.37973        0.73888       -1.29184
H         -1.90865        1.59085       -0.81242
C         -0.23175       -0.51768       -1.52346
C          1.91496       -1.41716       -1.64800
C          0.65841        0.42689       -1.01129
C          0.04268       -2.89488       -2.39708
H         -0.65050       -3.33962       -1.67728
H          0.91582       -3.54105       -2.49919
H         -0.44018       -2.78370       -3.37238
C         -4.09833       -0.57135       -2.15719
H         -5.07750       -0.93102       -2.43882
S          5.36132        1.90524        0.32590
O         -0.13602        2.58456       -0.15540
N          2.11666        1.95210       -0.19086
C          4.29162        0.70561       -0.39716
C          6.40127       -0.30045       -0.50392
H          7.13385       -1.05708       -0.74564
C          5.01848       -0.41493       -0.78380
H          4.54737       -1.26603       -1.26486
C          2.87147        0.84567       -0.55980
C          0.72453        1.74516       -0.43629
C          1.98161       -0.09855       -1.07378
C          2.59661        3.22223        0.31584
H          3.28918        3.66856       -0.40356
H          1.72293        3.86740        0.41908
H          3.07989        3.11116        1.29082
C          6.73603        0.89170        0.08935
H          7.71423        1.24918        0.37710
S         -6.52817       -2.03878        0.58371
O         -1.02818       -2.71960        1.06675
N         -3.27872       -2.07761        1.07797
C         -5.45538       -0.83518        1.29534
C         -7.56954        0.15670        1.43834
H         -8.30368        0.90625        1.69709
C         -6.18359        0.27866        1.69822
H         -5.71147        1.12941        2.17894
C         -4.03388       -0.97028        1.44589
C         -1.88865       -1.87461        1.33375
C         -3.14423       -0.02703        1.96118
C         -3.76027       -3.35071        0.58001
H         -4.44387       -3.79802        1.30764
H         -2.88571       -3.99343        0.46902
H         -4.25416       -3.24265       -0.38969
C         -7.90546       -1.03479        0.84443
H         -8.88586       -1.39755        0.57090
S          1.55423        1.44157        3.32272
O         -3.94035        2.12501        2.83066
N         -1.68858        1.48990        2.80071
C          0.48536        0.24085        2.60044
C          2.59453       -0.76660        2.50074
H          3.32863       -1.52175        2.25944
C          1.21229       -0.88106        2.21808
H          0.74164       -1.73201        1.73620
C         -0.93363        0.38355        2.43098
C         -3.07970        1.28628        2.54720
C         -1.82206       -0.55498        1.90519
C         -1.20969        2.75508        3.31999
H         -0.51138        3.20579        2.60873
H         -2.08284        3.40127        3.42197
H         -0.73308        2.63549        4.29742
C          2.92889        0.42681        3.09155
H          3.90777        0.78542        3.37563
H         -2.43955       -0.57698       -5.37779
C         -3.31415        0.06572       -5.26679
H         -3.80805        0.17382       -6.23649
H         -3.99775       -0.38158       -4.53919
O         -0.58205        0.69682       -4.78009
S         -6.08205        1.37762       -5.26309
N         -2.83255        1.33882       -4.76879
C         -1.44255        1.54182       -4.51299
H          1.18775        1.68442       -4.11059
H         -8.43975        2.01892       -5.27589
H          3.77475        1.89462       -3.58739
C         -7.45935        2.38162       -5.00239
C         -3.58775        2.44612       -4.40089
C         -5.00925        2.58122       -4.55149
C          1.65845        2.53532       -3.62869
C          3.04065        2.64982       -3.34609
C         -1.37595        2.86142       -3.94159
C         -2.69805        3.38942       -3.88559
C         -7.12335        3.57312       -4.40849
C         -5.73745        3.69512       -4.14859
C          0.93155        3.65732       -3.24639
C         -0.48745        3.79992       -3.41579
C          3.37505        3.84322       -2.75529
H         -7.85755        4.32272       -4.14969
H          4.35395        4.20182       -2.47119
C         -2.63355        4.70272       -3.29959
H         -5.26535        4.54582       -3.66789
S          2.00035        4.85802       -2.52409
N         -1.24245        4.90632       -3.04609
O         -3.49425        5.54142       -3.01609
C         -0.76355        6.17152       -2.52679
H         -0.06525        6.62222       -3.23809
H         -0.28695        6.05192       -1.54939
H         -1.63665        6.81772       -2.42479
C          1.50504        0.25690        6.02028
H          1.98834        0.14590        6.99528
H          0.63134        0.90210        6.12358
N          1.02514       -1.01320        5.51358
C         -0.36706       -1.22010        5.26818
O         -1.22756       -0.38070        5.54908
C         -0.43316       -2.53840        4.69318
C          0.89004       -3.06380        4.63068
C          0.82344       -4.38250        4.05648
N         -0.56786       -4.58990        3.81248
C         -1.04886       -5.86020        3.30738
H         -1.74206       -6.30490        4.02718
H         -0.17576       -6.50630        3.20528
H         -1.53176       -5.74900        2.33208
O          1.68474       -5.22240        3.77598
C         -1.32326       -3.48300        4.18098
C         -2.74376       -3.34510        4.02218
C         -3.47126       -2.22640        4.41268
H         -3.00026       -1.37440        4.89208
C         -4.85496       -2.34400        4.13938
H         -5.58846       -1.58990        4.38538
C         -5.18986       -3.53670        3.54728
H         -6.16906       -3.89630        3.26568
S         -3.81416       -4.54700        3.30358
C          1.77994       -2.11960        5.14468
C          3.20004       -2.25970        5.30728
S          4.26974       -1.06010        6.03038
C          5.64444       -2.07360        5.79388
H          6.62264       -1.71610        6.08158
C          5.30974       -3.26570        5.20058
H          6.04234       -4.02240        4.95888
C          3.92694       -3.38020        4.92068
H          3.45584       -4.23130        4.43958
H          2.19764        0.70330        5.30088
                """)
qatom.unit = unit.angstrom

qmolecule = molecule( geom, charge=0, mult=1, sym=sym.C1 )
print qmolecule

qatom.basis = baslib("def2-svp/jkfit")
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

scf.maxloop = 1000
scf.tol_density = 1e-6

## Generate int
#scf.maxloop = 0
scf.guess = "moread"

scf.dft_ang = 11
scf.dft_intacc  = 13. / 3.

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
casscf.closed = [85*3-3*2]
casscf.occ    = [     4*3]
#casscf.roots = {1.0:7}
casscf.roots = {1.0:1}

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
icmr.frozen = [30*4]
icmr.closed = [85*4-30*4-2*4]
#icmr.occ    = [          4*4] #genuine
icmr.occ    = [          4*4-2]
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

## # LCT
## lct.test        = False
## lct.DoPNO       = True
## lct.UseOrthPNOs = True
## lct.DoLoc       = True
## lct.DoCEPT2     = True
## lct.NewTrafo    = True
## lct.Make4EXT    = False
## 
## lct.TCutPNOrho0 = 5e-8
## lct.TCutPNOrho1 = 5e-8
## lct.TCutPNOrho2 = 5e-8
## lct.TCutPairs   = 1e-5
## 
## lct.TCutPNOrho0 = 5e-8
## lct.TCutPNOrho1 = 5e-8
## lct.TCutPNOrho2 = 5e-8
## lct.TCutPairs   = 1e-5
## 
## #lct.TCutPNOrho0 = 0.0
## #lct.TCutPNOrho1 = 0.0
## #lct.TCutPNOrho2 = 0.0
## #lct.TCutPairs   = 0.0
## 
## lct.MaxIter = 50
## 
## lct.DoCEPT2     = False
## lct.NNewTrafo   = True
## lct.NewTrafo    = (not lct.NNewTrafo)
## lct.TrafoMode   = "Disk"
## lct.NewAlgoPNO  = True
## lct.OVLMode     = lct.TrafoMode
## #lct.OVLMode     = "InCore"

lct.DoPNO = False

# LCT
lct.test        = False
lct.DoPNO       = True
lct.UseOrthPNOs = True

lct.DoLoc       = True

lct.DoCEPT2     = True
lct.Make4EXT    = False

lct.TCutPNOrho0 = 1e-8
lct.TCutPNOrho1 = 5e-8
lct.TCutPNOrho2 = 5e-8
lct.TCutPairs   = 5e-6

lct.TCutPre = 5e-7
#lct.TCutPre = 0.0

#lct.TCutPNOrho0 = 0.0
#lct.TCutPNOrho1 = 0.0
#lct.TCutPNOrho2 = 0.0
#lct.TCutPairs   = 0.0

lct.MaxIter = 50
lct.NewTrafo    = False

### For testing performance of PNO-CASPT2 #####
lct.DoCEPT2     = False
lct.NNewTrafo   = True
#lct.PreScMode   = "InCore"
lct.TrafoMode   = "Disk"
lct.OVLMode     = "Disk"
#lct.StackSize   = 160000000
#lct.StackSize   = 320000000
lct.NewAlgoPNO  = True
# Use of Local PAO/PNO
#lct.UsePAOs     = False
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
hint.nmicroiter     = 200000

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
hint.kscal = 1e-3
hint.nroots         = 3
hint.nconvroots     = 3
hint.maxdvd         = 100
hint.stepThresh     = 0.5
hint.fastConv       = False
hint.print_dvd      = False
lct.LocRecursive    = True
lct.LocMeasure      = True
#lct.FormLVOs        = True
lct.UseJacobiGuess  = True
# LVO truncation therhold
lct.DomScheme       = "Scheme1"
lct.TCutCRV         = 99.0
lct.TCutDOI         = 1e-3
lct.TCutVDO         = 1e-2

