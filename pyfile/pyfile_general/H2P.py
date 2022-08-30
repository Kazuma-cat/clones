
from sci import *

#qatom.basis=baslib("def2-TZVPP")
qatom.basis = baslib("def2-SVP") # Molecule Basis Set
#qatom.basis = baslib("def2-TZVPP")
#qatom.unit = unit.angstrom
# acene=[ 
#     qatom(atom.C, [        0.000000,    0.712654,    3.645610 ]),
#     qatom(atom.C, [        0.000000,   -0.712654,    3.645610 ]),
#     qatom(atom.C, [        0.000000,    1.401875,    2.472151 ]),
#     qatom(atom.C, [        0.000000,   -1.401875,    2.472151 ]),
#     qatom(atom.C, [        0.000000,    0.717143,    1.217813 ]),
#     qatom(atom.C, [        0.000000,   -0.717143,    1.217813 ]),
#     qatom(atom.C, [        0.000000,    1.396446,    0.000000 ]),
#     qatom(atom.C, [        0.000000,   -1.396446,    0.000000 ]),
#     qatom(atom.C, [        0.000000,    0.717143,   -1.217813 ]),
#     qatom(atom.C, [        0.000000,   -0.717143,   -1.217813 ]),
#     qatom(atom.C, [        0.000000,    1.401875,   -2.472151 ]),
#     qatom(atom.C, [        0.000000,   -1.401875,   -2.472151 ]),
#     qatom(atom.C, [        0.000000,    0.712654,   -3.645610 ]),
#     qatom(atom.C, [        0.000000,   -0.712654,   -3.645610 ]),
#     qatom(atom.H, [        0.000000,    1.245431,    4.591480 ]),
#     qatom(atom.H, [        0.000000,   -1.245431,    4.591480 ]),
#     qatom(atom.H, [        0.000000,    2.488356,    2.467861 ]),
#     qatom(atom.H, [        0.000000,   -2.488356,    2.467861 ]),
#     qatom(atom.H, [        0.000000,    2.483786,    0.000000 ]),
#     qatom(atom.H, [        0.000000,   -2.483786,    0.000000 ]),
#     qatom(atom.H, [        0.000000,    2.488356,   -2.467861 ]),
#     qatom(atom.H, [        0.000000,   -2.488356,   -2.467861 ]),
#     qatom(atom.H, [        0.000000,    1.245431,   -4.591480 ]),
#     qatom(atom.H, [        0.000000,   -1.245431,   -4.591480 ]),
# ]
#XY qatom.unit = unit.bohr
#XY H2P=[
#XY     qatom(atom.N, [         0.000000000000,     3.835164878753,     0.000000000000 ]),
#XY     qatom(atom.N, [        -4.001226439725,     0.000000000000,     0.000000000000 ]),
#XY     qatom(atom.N, [         0.000000000000,    -3.835164878753,     0.000000000000 ]),
#XY     qatom(atom.N, [         4.001226439725,     0.000000000000,     0.000000000000 ]),
#XY     qatom(atom.C, [        -2.050001208574,     5.395657136424,     0.000000000000 ]),
#XY     qatom(atom.C, [         2.050001208574,     5.395657136424,     0.000000000000 ]),
#XY     qatom(atom.C, [        -5.473151019764,     2.135458397230,     0.000000000000 ]),
#XY     qatom(atom.C, [        -5.473151019764,    -2.135458397230,     0.000000000000 ]),
#XY     qatom(atom.C, [        -2.050001208574,    -5.395657136424,     0.000000000000 ]),
#XY     qatom(atom.C, [         2.050001208574,    -5.395657136424,     0.000000000000 ]),
#XY     qatom(atom.C, [         5.473151019764,     2.135458397230,     0.000000000000 ]),
#XY     qatom(atom.C, [         5.473151019764,    -2.135458397230,     0.000000000000 ]),
#XY     qatom(atom.C, [        -1.281508230525,     8.045863664861,     0.000000000000 ]),
#XY     qatom(atom.C, [         1.281508230525,     8.045863664861,     0.000000000000 ]),
#XY     qatom(atom.C, [        -8.052056296925,    -1.296437065835,     0.000000000000 ]),
#XY     qatom(atom.C, [        -8.052056296925,     1.296437065835,     0.000000000000 ]),
#XY     qatom(atom.C, [        -1.281508230525,    -8.045863664861,     0.000000000000 ]),
#XY     qatom(atom.C, [         1.281508230525,    -8.045863664861,     0.000000000000 ]),
#XY     qatom(atom.C, [         8.052056296925,    -1n.296437065835,     0.000000000000 ]),
#XY     qatom(atom.C, [         8.052056296925,     1.296437065835,     0.000000000000 ]),
#XY     qatom(atom.C, [        -4.576685797768,     4.612630275796,     0.000000000000 ]),
#XY     qatom(atom.C, [         4.576685797768,    -4.612630275796,     0.000000000000 ]),
#XY     qatom(atom.C, [         4.576685797768,     4.612630275796,     0.000000000000 ]),
#XY     qatom(atom.C, [        -4.576685797768,    -4.612630275796,     0.000000000000 ]),
#XY     qatom(atom.H, [        -2.082568746261,     0.000000000000,     0.000000000000 ]),
#XY     qatom(atom.H, [         2.082568746261,     0.000000000000,     0.000000000000 ]),
#XY     qatom(atom.H, [         9.671012897231,    -2.546014596330,     0.000000000000 ]),
#XY     qatom(atom.H, [         9.671012897231,     2.546014596330,     0.000000000000 ]),
#XY     qatom(atom.H, [        -2.554389861912,     9.649165775077,     0.000000000000 ]),
#XY     qatom(atom.H, [         2.554389861912,     9.649165775077,     0.000000000000 ]),
#XY     qatom(atom.H, [        -9.671012897231,     2.546014596330,     0.000000000000 ]),
#XY     qatom(atom.H, [        -9.671012897231,    -2.546014596330,     0.000000000000 ]),
#XY     qatom(atom.H, [        -2.554389861912,    -9.649165775077,     0.000000000000 ]),
#XY     qatom(atom.H, [         2.554389861912,    -9.649165775077,     0.000000000000 ]),
#XY     qatom(atom.H, [         6.008395119043,     6.084598319532,     0.000000000000 ]),
#XY     qatom(atom.H, [        -6.008395119043,     6.084598319532,     0.000000000000 ]),
#XY     qatom(atom.H, [        -6.008395119043,    -6.084598319532,     0.000000000000 ]),
#XY     qatom(atom.H, [         6.008395119043,    -6.084598319532,     0.000000000000 ]),
#XY ]

qatom.unit = unit.bohr
H2P=[
    qatom(atom.N, [         0.000000000000,     3.835164878753,     0.000000000000 ]),
    qatom(atom.N, [         0.000000000000,     0.000000000000,     4.001226439725 ]),
    qatom(atom.N, [         0.000000000000,    -3.835164878753,     0.000000000000 ]),
    qatom(atom.N, [         0.000000000000,     0.000000000000,    -4.001226439725 ]),
    qatom(atom.C, [         0.000000000000,     5.395657136424,     2.050001208574 ]),
    qatom(atom.C, [         0.000000000000,     5.395657136424,    -2.050001208574 ]),
    qatom(atom.C, [         0.000000000000,     2.135458397230,     5.473151019764 ]),
    qatom(atom.C, [         0.000000000000,    -2.135458397230,     5.473151019764 ]),
    qatom(atom.C, [         0.000000000000,    -5.395657136424,     2.050001208574 ]),
    qatom(atom.C, [         0.000000000000,    -5.395657136424,    -2.050001208574 ]),
    qatom(atom.C, [         0.000000000000,     2.135458397230,    -5.473151019764 ]),
    qatom(atom.C, [         0.000000000000,    -2.135458397230,    -5.473151019764 ]),
    qatom(atom.C, [         0.000000000000,     8.045863664861,     1.281508230525 ]),
    qatom(atom.C, [         0.000000000000,     8.045863664861,    -1.281508230525 ]),
    qatom(atom.C, [         0.000000000000,    -1.296437065835,     8.052056296925 ]),
    qatom(atom.C, [         0.000000000000,     1.296437065835,     8.052056296925 ]),
    qatom(atom.C, [         0.000000000000,    -8.045863664861,     1.281508230525 ]),
    qatom(atom.C, [         0.000000000000,    -8.045863664861,    -1.281508230525 ]),
    qatom(atom.C, [         0.000000000000,    -1.296437065835,    -8.052056296925 ]),
    qatom(atom.C, [         0.000000000000,     1.296437065835,    -8.052056296925 ]),
    qatom(atom.C, [         0.000000000000,     4.612630275796,     4.576685797768 ]),
    qatom(atom.C, [         0.000000000000,    -4.612630275796,    -4.576685797768 ]),
    qatom(atom.C, [         0.000000000000,     4.612630275796,    -4.576685797768 ]),
    qatom(atom.C, [         0.000000000000,    -4.612630275796,     4.576685797768 ]),
    qatom(atom.H, [         0.000000000000,     0.000000000000,     2.082568746261 ]),
    qatom(atom.H, [         0.000000000000,     0.000000000000,    -2.082568746261 ]),
    qatom(atom.H, [         0.000000000000,    -2.546014596330,    -9.671012897231 ]),
    qatom(atom.H, [         0.000000000000,     2.546014596330,    -9.671012897231 ]),
    qatom(atom.H, [         0.000000000000,     9.649165775077,     2.554389861912 ]),
    qatom(atom.H, [         0.000000000000,     9.649165775077,    -2.554389861912 ]),
    qatom(atom.H, [         0.000000000000,     2.546014596330,     9.671012897231 ]),
    qatom(atom.H, [         0.000000000000,    -2.546014596330,     9.671012897231 ]),
    qatom(atom.H, [         0.000000000000,    -9.649165775077,     2.554389861912 ]),
    qatom(atom.H, [         0.000000000000,    -9.649165775077,    -2.554389861912 ]),
    qatom(atom.H, [         0.000000000000,     6.084598319532,    -6.008395119043 ]),
    qatom(atom.H, [         0.000000000000,     6.084598319532,     6.008395119043 ]),
    qatom(atom.H, [         0.000000000000,    -6.084598319532,     6.008395119043 ]),
    qatom(atom.H, [         0.000000000000,    -6.084598319532,    -6.008395119043 ]), 
]

qmolecule = molecule(H2P, charge=0, mult=1, sym=sym.C1 )

print qmolecule

qatom.basis = baslib("def2-tzvpp/jkfit") # Auxiliary Basis
#qatom.basis = baslib("aug-cc-pv5z-ri/jkfit")

acene = [ i.new_basis() for i in H2P]
qmolecule_RI_JK = molecule(acene, charge=0, mult=1, sym=sym.C1)
casscf.no4c_RI_JK = True
hint.use_RI_JK = True
hint.itrf_RI_JK_memory = 2000
ga_memory = 100000

#qatom.basis = baslib("cc-pvtz-ri/mp2fit")
#acene2 = [ i.new_basis() for i in c8h10]
#qmolecule_RI_C = molecule(acene2, charge=0, mult=1, sym=sym.C1)

qmolecule_RI_C = qmolecule_RI_JK

#scf.calc_ao_tei     = True
#scf.hund_occupation = True
scf.dodirect        = False
#scf.dft_xc = ["hyb_gga_xc_b3lyp"]
scf.show_orbitals   = True
#scf.guess = "moread"
#scf.maxloop = 0

scf.dft_ang = 11
scf.dft_intacc  = 13. / 3.

casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"

casscf.frozen = [ 0]
casscf.closed = [77]
casscf.occ    = [ 8]

casscf.roots = {1:1}
casscf.citype = "fullci"
casscf.localize_type = "orz"
casscf.maxMacroloop = 100
casscf.tolMacroloop = 5e-5
casscf.tolStepSize  = 5e-4
casscf.debugkeys=["noon","saveall","canonical"]

# ICMR
icmr.skip_itrf  = False
icmr.skip_casci = False
icmr.scfinp = casscf.scfinp
icmr.localize_type = casscf.localize_type
icmr.orbconfig = casscf.orbconfig

icmr.frozen = [24]
icmr.closed = [57]
icmr.occ    = [ 0]

icmr.roots  = {1:1}
icmr.citype = casscf.citype
icmr.use_3RDM = True
icmr.use_4RDM = True
icmr.use_d4cum_of = False
icmr.ampAllocType = 2 #a 1=disk, 2=GA
icmr.icb_type = -2 # ICBTYPE # 0=MS-MR, 1=MS-SR, 2=SS-SR, -1=MS-SR*, -2=SS-SR*
icmr.xms_type =  0 # XMSTYPE # 0=Non-XMS, 1=XMS
icmr.method = "caspt2"
icmr.pt.tolOrthExternal_1rdm = 1e-8
icmr.pt.tolOrthExternal      = 1e-8
icmr.pt.tolOrthInternal      = 1e-8
icmr.pt.ipeashift = 0.0
#icmr.pt.lvl_shift = 0.2
icmr.pt.lvl_shift = 0.0
icmr.pt.toliter   = 1e-10

## # LCT
## lct.test        = False
## lct.DoPNO       = True
## lct.UseOrthPNOs = True
## lct.DoLoc       = True
## lct.DoCEPT2     = False
## lct.NewTrafo    = True
## lct.Make4EXT    = False
## 
## lct.TCutPNOrho0 = 1e-9
## lct.TCutPNOrho1 = 1e-9
## lct.TCutPNOrho2 = 1e-9
## lct.TCutPairs   = 1e-5
## 
## #lct.TCutPNOrho0 = 0.0
## #lct.TCutPNOrho1 = 0.0
## #lct.TCutPNOrho2 = 0.0
## #lct.TCutPairs   = 0.0
## 
## lct.MaxIter = 50

lct.DoPNO = False

# LCT
lct.test        = False
lct.DoPNO       = True
lct.UseOrthPNOs = True

lct.DoLoc       = True

lct.DoCEPT2     = True
lct.Make4EXT    = False

lct.TCutPNOrho0 = 5e-8
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
lct.NewTrafo    = True

### For testing performance of PNO-CASPT2 #####
lct.DoCEPT2     = False
lct.NNewTrafo   = True
lct.NewTrafo    = (not lct.NNewTrafo)
lct.TrafoMode   = "Disk"
lct.NewAlgoPNO  = True
lct.OVLMode     = lct.TrafoMode
# Use of Local PAO/PNO
#lct.UsePAOs     = True
lct.UseVM1_CD   = True
lct.UseVM12     = (not lct.UseVM1_CD)

# Just for debugging PAO-based implementation
#lct.TCutMKN      = 1e-3
#lct.TCutMKNFit   = 0.0
#lct.DoHylleraas  = False
#lct.DoFullCASPT2 = False

#lct.TCutDeloc        = 0.1
lct.PrintPairDistDBG = True
lct.PrintMapsDBG     = True

lct.UseCholeskyOrb  = True
#lct.LocMet          = "PSM"
##lct.LocMet          = "FBNR"
#lct.LocPower        = 2
#hint.maximize_niter = 2000
#hint.nmicroiter     = 200000
#hint.cg_thresh      = 1e-5
#hint.res_tol        = 1e-5
#hint.nroots         = 3
#hint.nconvroots     = 3
#hint.maxdvd         = 100
#hint.stepThresh     = 0.5
#hint.fastConv       = False
#hint.print_dvd      = False
#lct.LocRecursive    = True
#lct.LocMeasure      = True
#lct.FormLVOs        = True

# options modified by clones
lct.UsePAOs = False
lct.FormLVOs = True
lct.RIMP2 = False 
lct.LocMet = "PMNR"
hint.isOnTheFly = True
hint.ChargeType = "Loewdin"
hint.ImplTypePM = "incore"


#hint.cg_thresh         = 1e-9 # Convergence threshold for preconditi
hint.jacobi_thresh     = 1e-5 # Convergence threshold for Jacobi rotations
hint.loc_thresh        = 1e-5 # Convergence thrshold for grad norm
hint.cg_thresh         = 1e-5 # Convergence threshold for preconditioned conjugate gradient(=PCG) iterations
hint.res_tol           = 1e-5
hint.print_dvd  = True
hint.stepThresh = 0.6
hint.nroots = 3
hint.nconvroots = 1

lct.UseJacobiGuess  = True
lct.LocMeasure      = True
#lct.FormLVOs        = True
lct.DomScheme       = "Scheme3"
lct.TCutCRV         = 99.3
lct.TCutDOI         = 1e-2

lct.DomScheme       = "Scheme2"
lct.TCutCRV         = 99.0
lct.TCutDOI         = 1e-2
lct.TCutVDO         = 1e-2

lct.DoFullCASPT2 = True
lct.DoHylleraas  = False
