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
     qatom(atom.H, [-0.9398288600990078, -0.542610445370341, 0.0]), 
     qatom(atom.H, [0.9398288600990078, -0.542610445370341, 0.0]), 
     qatom(atom.H, [-0.9411514043181364, 1.878344871032219, 0.0]), 
     qatom(atom.H, [2.221330007543493, 1.5297553401681898, 0.0]), 
     qatom(atom.H, [0.3382019123911302, 3.951950707223903, 0.0]), 
     qatom(atom.H, [3.5006833242527593, 3.603361176359874, 0.0]), 
     qatom(atom.H, [1.6175552291003965, 6.025556543415587, 0.0]), 
     qatom(atom.H, [4.7800366409620265, 5.676967012551558, 0.0]), 
     qatom(atom.H, [2.898231090028792, 8.098398808346342, 0.0]), 
     qatom(atom.C, [5.117413266837066, 8.294423344766736, 0.0]), 
     qatom(atom.C, [5.117413266837066, 9.68556679218688, 0.0]), 
     qatom(atom.C, [6.322178832611172, 10.38113851589695, 0.0]), 
     qatom(atom.C, [7.526944398385277, 9.685566792186878, 0.0]), 
     qatom(atom.C, [7.526944398385276, 8.294423344766734, 0.0]), 
     qatom(atom.C, [6.32217883261117, 7.598851621056664, 0.0]), 
     qatom(atom.H, [4.16935818952088, 10.232926646281971, 0.0]), 
     qatom(atom.H, [6.322178832611173, 11.475858224087133, 0.0]), 
     qatom(atom.H, [8.474999475701464, 10.23292664628197, 0.0]), 
     qatom(atom.H, [8.474999475701463, 7.747063490671643, 0.0]), 
     qatom(atom.H, [6.322178832611169, 6.50413191286648, 0.0]), 
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
icmr.frozen = [14]
icmr.closed = [33.0]
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
