from sci import *

import os

qatom.basis = baslib("sto-3g")
qatom.basis = baslib("def2-svp")
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
S        -2.72256585   -1.58164979   -2.40086472
O         2.77627865   -2.25714887   -1.92851866
N         0.52365957   -1.62455339   -1.89200093
C        -1.65219406   -0.37984559   -1.68229588
C        -3.76340488    0.62126492   -1.56509226
H        -4.49688181    1.37535038   -1.31908734
C        -2.37973306    0.73888067   -1.29183651
H        -1.90865405    1.59085398   -0.81242307
C        -0.23174584   -0.51768520   -1.52346142
C         1.91496189   -1.41716199   -1.64800029
C         0.65840725    0.42688956   -1.01129233
C         0.04268278   -2.89488188   -2.39708059
H        -0.65049948   -3.33962433   -1.67727777
H         0.91582156   -3.54104605   -2.49918723
H        -0.44018299   -2.78369757   -3.37238201
C        -4.09833063   -0.57135389   -2.15719032
H        -5.07749881   -0.93102095   -2.43882271
S         5.36132289    1.90523721    0.32590120
O        -0.13601563    2.58456410   -0.15539742
N         2.11666449    1.95209597   -0.19086018
C         4.29162463    0.70560537   -0.39715673
C         6.40126758   -0.30044811   -0.50392479
H         7.13385289   -1.05708061   -0.74563606
C         5.01848322   -0.41492917   -0.78380034
H         4.54737159   -1.26603426   -1.26485859
C         2.87147284    0.84566886   -0.55979903
C         0.72453131    1.74515606   -0.43629134
C         1.98160893   -0.09854639   -1.07377616
C         2.59661274    3.22223244    0.31583849
H         3.28917824    3.66855965   -0.40356103
H         1.72292955    3.86740325    0.41908163
H         3.07989071    3.11115970    1.29081529
C         6.73602590    0.89170197    0.08935297
H         7.71423042    1.24918334    0.37710219
S        -6.52817090   -2.03878082    0.58370485
O        -1.02818050   -2.71960358    1.06674815
N        -3.27872143   -2.07760847    1.07796938
C        -5.45538219   -0.83518182    1.29533852
C        -7.56953674    0.15669588    1.43834530
H        -8.30368101    0.90625272    1.69708836
C        -6.18359226    0.27865917    1.69822333
H        -5.71146646    1.12941015    2.17893551
C        -4.03388426   -0.97027732    1.44588539
C        -1.88865127   -1.87461374    1.33375359
C        -3.14422520   -0.02702564    1.96118483
C        -3.76026932   -3.35070600    0.58001288
H        -4.44386550   -3.79802445    1.30763671
H        -2.88571437   -3.99343144    0.46901534
H        -4.25416349   -3.24264938   -0.38969005
C        -7.90546206   -1.03478682    0.84443303
H        -8.88585859   -1.39754632    0.57090408
S         1.55422909    1.44156752    3.32272384
O        -3.94035272    2.12500614    2.83065799
N        -1.68857765    1.48989876    2.80071440
C         0.48536319    0.24085024    2.60044132
C         2.59452921   -0.76660524    2.50073470
H         3.32862572   -1.52175247    2.25944253
C         1.21229107   -0.88105616    2.21808312
H         0.74163538   -1.73200975    1.73620153
C        -0.93362863    0.38354687    2.43098062
C        -3.07970309    1.28627849    2.54719812
C        -1.82206154   -0.55497579    1.90519133
C        -1.20968947    2.75507859    3.31998790
H        -0.51137656    3.20579272    2.60873431
H        -2.08284151    3.40126894    3.42196894
H        -0.73308455    2.63549166    4.29742129
C         2.92889014    0.42681434    3.09154639
H         3.90777177    0.78542346    3.37562913
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

scf.maxloop = 600
scf.tol_density = 1e-4

## Generate int
#scf.maxloop = 0
#scf.guess = "moread"

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
casscf.closed = [85*2-2*2]
casscf.occ    = [     4*2]
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
icmr.frozen = [30*2]
icmr.closed = [85*2-30*2-2*2]
icmr.occ    = [          4*2]
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
icmr.pt.toliter = 1.5e-7
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

## LCT
#lct.test        = False
#lct.DoPNO       = True
#lct.UseOrthPNOs = True
#lct.DoLoc       = True
#lct.DoCEPT2     = True
#lct.NewTrafo    = True
#lct.Make4EXT    = False
#
#lct.TCutPNOrho0 = 5e-8
#lct.TCutPNOrho1 = 5e-8
#lct.TCutPNOrho2 = 5e-8
#lct.TCutPairs   = 1e-5
#
#lct.TCutPNOrho0 = 5e-9
#lct.TCutPNOrho1 = 1e-8
#lct.TCutPNOrho2 = 1e-8
#lct.TCutPairs   = 3e-6
#
#lct.TCutPre     = 5e-7
##lct.TCutPre     = 0.0
##lct.PrintPairDistDBG = True
#
##lct.TCutPNOrho0 = 0.0
##lct.TCutPNOrho1 = 0.0
##lct.TCutPNOrho2 = 0.0
##lct.TCutPairs   = 0.0
#
#lct.MaxIter = 50
#
#lct.DoCEPT2     = False
#lct.NNewTrafo   = True
#lct.NewTrafo    = (not lct.NNewTrafo)
#lct.TrafoMode   = "Disk"
#lct.NewAlgoPNO  = True
#lct.OVLMode     = lct.TrafoMode
##lct.OVLMode     = "InCore"
#
#lct.UseVM1_CD   = True
#lct.UseVM12     = (not lct.UseVM1_CD)
#
##lct.TCutMKN     = 1e-20
#lct.UsePAOs     = True
#
#lct.PrintPairDistDBG = True
#lct.PrintMapsDBG     = True
#
##lct.LocMet = "FB"
#lct.UseCholeskyOrb  = True
#lct.LocMet          = "FBNR"

## lct.DoPNO = False
## 
## # LCT
## lct.test        = False
## lct.DoPNO       = True
## lct.UseOrthPNOs = True
## 
## lct.DoLoc       = True
## 
## lct.DoCEPT2     = True
## lct.Make4EXT    = False
## 
## lct.TCutPNOrho0 = 1e-8
## lct.TCutPNOrho1 = 1e-8
## lct.TCutPNOrho2 = 1e-8
## lct.TCutPairs   = 5e-6
## 
## lct.TCutPre = 5e-7
## #lct.TCutPre = 0.0
## 
## #lct.TCutPNOrho0 = 0.0
## #lct.TCutPNOrho1 = 0.0
## #lct.TCutPNOrho2 = 0.0
## #lct.TCutPairs   = 0.0
## 
## lct.MaxIter = 50
## lct.NewTrafo    = True
## 
## ### For testing performance of PNO-CASPT2 #####
## lct.DoCEPT2     = False
## lct.NNewTrafo   = True
## lct.NewTrafo    = (not lct.NNewTrafo)
## lct.TrafoMode   = "Disk"
## lct.NewAlgoPNO  = True
## lct.OVLMode     = lct.TrafoMode
## # Use of Local PAO/PNO
## lct.UseVM1_CD   = True
## lct.UseVM12     = (not lct.UseVM1_CD)
## 
## # Just for debugging PAO-based implementation
## #lct.TCutMKN      = 0.0
## #lct.TCutMKNFit   = 0.0
## #lct.DoHylleraas  = False
## #lct.DoFullCASPT2 = False
## 
## #lct.TCutDeloc        = 0.03
## lct.PrintPairDistDBG = True
## lct.PrintMapsDBG     = True
## 
## lct.UseCholeskyOrb  = True
## lct.LocMet          = "PSM"
## #lct.LocMet          = "FBNR"
## lct.LocPower        = 1
## #hint.loc_thresh     = 1e-14
## hint.randomize      = True
## hint.maximize_niter = 2000
## hint.nmicroiter     = 200000
## hint.jacobi_thresh  = 1e-5
## hint.cg_thresh      = 1e-5
## hint.loc_thresh     = 1e-5
## hint.res_tol        = 1e-5
## hint.nroots         = 4
## hint.nconvroots     = 4
## hint.maxdvd         = 100
## hint.stepThresh     = 0.5
## hint.fastConv       = False
## hint.print_dvd      = False
## lct.LocRecursive    = True
## lct.LocMeasure      = True
## 
## lct.UsePAOs         = False
## lct.FormLVOs        = not lct.UsePAOs
## 
## lct.UseJacobiGuess  = True
## # LVO truncation therhold
## lct.DomScheme       = "Scheme3"
## lct.TCutCRV         = 96.0
## lct.TCutDOI         = 1e-3
## lct.TCutVDO         = 1e-2
## 
## scf.dft_ang = 11
## scf.dft_intacc  = 13. / 3.
## 
## lct.TCutPre = 1.0e-6
## 
## #TIGHT# ###
## #TIGHT# lct.TCutPNOrho0 = 5e-9
## #TIGHT# lct.TCutPNOrho1 = 1e-8
## #TIGHT# lct.TCutPNOrho2 = 1e-8
## #TIGHT# lct.TCutPairs   = 3e-6
## #TIGHT# lct.TCutPre     = 5e-7

#lct.DoPNO = False

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
lct.OVLMode     = lct.TrafoMode
#lct.OVLMode     = "StackSpace"
#lct.StackSize   = 240000000
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
