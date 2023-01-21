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
qatom(atom.C, [0, 0, 0]),
qatom(atom.C, [0.0, 1.391143447420143, 0.0]),
qatom(atom.C, [-1.2047655657741054, 2.086715171130214, 0.0]),
qatom(atom.C, [-2.4095311315482104, 1.3911434474201414, 0.0]),
qatom(atom.C, [-2.409531131548209, -1.5543122344752192e-15, 0.0]),
qatom(atom.C, [-1.204765565774103, -0.6955717237100716, 0.0]),
qatom(atom.H, [0.9480550773161863, -0.5473598540950914, 0.0]),
qatom(atom.H, [0.9480550773161859, 1.9385033015152353, 0.0]),
qatom(atom.H, [-1.2047655657741065, 3.1814348793203973, 0.0]),
qatom(atom.H, [-3.3575862088643973, 1.9385033015152318, 0.0]),
qatom(atom.H, [-3.3575862088643946, -0.5473598540950945, 0.0]),
qatom(atom.C, [-1.2047655657741012, -2.211821723710072, 0.0]),
qatom(atom.H, [-1.7185965588616896, -2.575155242094386, 0.8899811598910946]),
qatom(atom.H, [-1.7185965588616896, -2.575155242094386, -0.8899811598910946]),
qatom(atom.C, [0.23678964235603317, -2.7214878712153623, 0.0]),
qatom(atom.H, [0.7506206354436212, -2.358154352831048, 0.8899811598910946]),
qatom(atom.H, [0.7506206354436212, -2.358154352831048, -0.8899811598910946]),
qatom(atom.C, [0.2367896423560351, -4.250487871215363, 0.0]),
qatom(atom.H, [-0.2770413507315533, -4.613821389599677, 0.8899811598910946]),
qatom(atom.H, [-0.2770413507315533, -4.613821389599677, -0.8899811598910946]),
qatom(atom.C, [1.6783448504861695, -4.7601540187206535, 0.0]),
qatom(atom.H, [2.1921758435737577, -4.3968205003363385, 0.8899811598910946]),
qatom(atom.H, [2.1921758435737577, -4.3968205003363385, -0.8899811598910946]),
qatom(atom.C, [1.678344850486171, -6.289154018720653, 0.0]),
qatom(atom.H, [1.1645138573985827, -6.652487537104967, 0.8899811598910946]),
qatom(atom.H, [1.1645138573985827, -6.652487537104967, -0.8899811598910946]),
qatom(atom.C, [3.1199000586163055, -6.798820166225944, 0.0]),
qatom(atom.H, [3.6337310517038937, -6.435486647841629, 0.8899811598910946]),
qatom(atom.H, [3.6337310517038937, -6.435486647841629, -0.8899811598910946]),
qatom(atom.C, [3.119900058616307, -8.327820166225944, 0.0]),
qatom(atom.H, [2.606069065528718, -8.691153684610258, 0.8899811598910946]),
qatom(atom.H, [2.606069065528718, -8.691153684610258, -0.8899811598910946]),
qatom(atom.C, [4.561455266746441, -8.837486313731235, 0.0]),
qatom(atom.H, [5.07528625983403, -8.474152795346921, 0.8899811598910946]),
qatom(atom.H, [5.07528625983403, -8.474152795346921, -0.8899811598910946]),
qatom(atom.C, [4.561455266746443, -10.366486313731235, 0.0]),
qatom(atom.H, [4.047624273658855, -10.729819832115549, 0.8899811598910946]),
qatom(atom.H, [4.047624273658855, -10.729819832115549, -0.8899811598910946]),
qatom(atom.C, [6.003010474876578, -10.876152461236526, 0.0]),
qatom(atom.H, [6.516841467964166, -10.512818942852212, 0.8899811598910946]),
qatom(atom.H, [6.516841467964166, -10.512818942852212, -0.8899811598910946]),
qatom(atom.C, [6.00301047487658, -12.405152461236526, 0.0]),
qatom(atom.H, [5.489179481788991, -12.76848597962084, 0.8899811598910946]),
qatom(atom.H, [5.489179481788991, -12.76848597962084, -0.8899811598910946]),
qatom(atom.C, [7.444565683006714, -12.914818608741816, 0.0]),
qatom(atom.H, [7.958396676094303, -12.551485090357502, 0.8899811598910946]),
qatom(atom.H, [7.958396676094303, -12.551485090357502, -0.8899811598910946]),
qatom(atom.C, [7.444565683006716, -14.443818608741816, 0.0]),
qatom(atom.H, [6.930734689919127, -14.80715212712613, 0.8899811598910946]),
qatom(atom.H, [6.930734689919127, -14.80715212712613, -0.8899811598910946]),
qatom(atom.C, [8.886120891136851, -14.953484756247107, 0.0]),
qatom(atom.H, [9.39995188422444, -14.590151237862793, 0.8899811598910946]),
qatom(atom.H, [9.39995188422444, -14.590151237862793, -0.8899811598910946]),
qatom(atom.C, [8.886120891136853, -16.482484756247107, 0.0]),
qatom(atom.H, [8.372289898049265, -16.845818274631423, 0.8899811598910946]),
qatom(atom.H, [8.372289898049265, -16.845818274631423, -0.8899811598910946]),
qatom(atom.C, [10.327676099266988, -16.992150903752396, 0.0]),
qatom(atom.H, [10.841507092354576, -16.62881738536808, 0.8899811598910946]),
qatom(atom.H, [10.841507092354576, -16.62881738536808, -0.8899811598910946]),
qatom(atom.C, [10.327676099266991, -18.521150903752396, 0.0]),
qatom(atom.H, [9.813845106179404, -18.884484422136712, 0.8899811598910946]),
qatom(atom.H, [9.813845106179404, -18.884484422136712, -0.8899811598910946]),
qatom(atom.C, [11.769231307397126, -19.030817051257685, 0.0]),
qatom(atom.H, [12.283062300484714, -18.66748353287337, 0.8899811598910946]),
qatom(atom.H, [12.283062300484714, -18.66748353287337, -0.8899811598910946]),
qatom(atom.C, [11.76923130739713, -20.559817051257685, 0.0]),
qatom(atom.H, [11.255400314309542, -20.923150569642, 0.8899811598910946]),
qatom(atom.H, [11.255400314309542, -20.923150569642, -0.8899811598910946]),
qatom(atom.C, [13.210786515527264, -21.069483198762974, 0.0]),
qatom(atom.H, [13.724617508614852, -20.706149680378658, 0.8899811598910946]),
qatom(atom.H, [13.724617508614852, -20.706149680378658, -0.8899811598910946]),
qatom(atom.C, [13.210786515527268, -22.598483198762974, 0.0]),
qatom(atom.H, [12.69695552243968, -22.96181671714729, 0.8899811598910946]),
qatom(atom.H, [12.69695552243968, -22.96181671714729, -0.8899811598910946]),
qatom(atom.C, [14.652341723657402, -23.108149346268263, 0.0]),
qatom(atom.H, [15.16617271674499, -22.744815827883947, 0.8899811598910946]),
qatom(atom.H, [15.16617271674499, -22.744815827883947, -0.8899811598910946]),
qatom(atom.C, [14.652341723657406, -24.637149346268263, 0.0]),
qatom(atom.H, [14.138510730569818, -25.00048286465258, 0.8899811598910946]),
qatom(atom.H, [14.138510730569818, -25.00048286465258, -0.8899811598910946]),
qatom(atom.C, [16.09389693178754, -25.146815493773552, 0.0]),
qatom(atom.H, [16.607727924875128, -24.783481975389236, 0.8899811598910946]),
qatom(atom.H, [16.607727924875128, -24.783481975389236, -0.8899811598910946]),
qatom(atom.C, [16.093896931787544, -26.675815493773552, 0.0]),
qatom(atom.H, [15.580065938699956, -27.039149012157868, 0.8899811598910946]),
qatom(atom.H, [15.580065938699956, -27.039149012157868, -0.8899811598910946]),
qatom(atom.C, [17.53545213991768, -27.18548164127884, 0.0]),
qatom(atom.H, [18.049283133005268, -26.822148122894525, 0.8899811598910946]),
qatom(atom.H, [18.049283133005268, -26.822148122894525, -0.8899811598910946]),
qatom(atom.C, [17.535452139917684, -28.71448164127884, 0.0]),
qatom(atom.H, [17.021621146830096, -29.077815159663157, 0.8899811598910946]),
qatom(atom.H, [17.021621146830096, -29.077815159663157, -0.8899811598910946]),
qatom(atom.C, [18.97700734804782, -29.22414778878413, 0.0]),
qatom(atom.H, [19.490838341135408, -28.860814270399814, 0.8899811598910946]),
qatom(atom.H, [19.490838341135408, -28.860814270399814, -0.8899811598910946]),
qatom(atom.C, [18.977007348047824, -30.75314778878413, 0.0]),
qatom(atom.H, [18.463176354960236, -31.116481307168446, 0.8899811598910946]),
qatom(atom.H, [18.463176354960236, -31.116481307168446, -0.8899811598910946]),
qatom(atom.C, [20.41856255617796, -31.26281393628942, 0.0]),
qatom(atom.H, [20.932393549265548, -30.899480417905103, 0.8899811598910946]),
qatom(atom.H, [20.932393549265548, -30.899480417905103, -0.8899811598910946]),
qatom(atom.C, [20.418562556177964, -32.791813936289415, 0.0]),
qatom(atom.H, [19.904731563090376, -33.15514745467373, 0.8899811598910946]),
qatom(atom.H, [19.904731563090376, -33.15514745467373, -0.8899811598910946]),
qatom(atom.C, [21.8601177643081, -33.3014800837947, 0.0]),
qatom(atom.H, [22.373948757395688, -32.938146565410385, 0.8899811598910946]),
qatom(atom.H, [22.373948757395688, -32.938146565410385, -0.8899811598910946]),
qatom(atom.C, [21.860117764308107, -34.8304800837947, 0.0]),
qatom(atom.H, [21.34628677122052, -35.19381360217901, 0.8899811598910946]),
qatom(atom.H, [21.34628677122052, -35.19381360217901, -0.8899811598910946]),
qatom(atom.C, [23.301672972438244, -35.34014623129998, 0.0]),
qatom(atom.H, [23.81550396552583, -34.97681271291567, 0.8899811598910946]),
qatom(atom.H, [23.81550396552583, -34.97681271291567, -0.8899811598910946]),
qatom(atom.C, [23.30167297243825, -36.86914623129998, 0.0]),
qatom(atom.H, [22.787841979350663, -37.232479749684295, 0.8899811598910946]),
qatom(atom.H, [22.787841979350663, -37.232479749684295, -0.8899811598910946]),
qatom(atom.C, [24.743228180568387, -37.378812378805264, 0.0]),
qatom(atom.H, [25.257059173655975, -37.01547886042095, 0.8899811598910946]),
qatom(atom.H, [25.257059173655975, -37.01547886042095, -0.8899811598910946]),
qatom(atom.C, [24.743228180568394, -38.90781237880526, 0.0]),
qatom(atom.H, [24.229397187480807, -39.27114589718958, 0.8899811598910946]),
qatom(atom.H, [24.229397187480807, -39.27114589718958, -0.8899811598910946]),
qatom(atom.C, [26.18478338869853, -39.417478526310546, 0.0]),
qatom(atom.H, [26.69861438178612, -39.05414500792623, 0.8899811598910946]),
qatom(atom.H, [26.69861438178612, -39.05414500792623, -0.8899811598910946]),
qatom(atom.C, [26.184783388698538, -40.94647852631054, 0.0]),
qatom(atom.H, [25.67095239561095, -41.30981204469486, 0.8899811598910946]),
qatom(atom.H, [25.67095239561095, -41.30981204469486, -0.8899811598910946]),
qatom(atom.C, [27.626338596828674, -41.45614467381583, 0.0]),
qatom(atom.H, [28.140169589916262, -41.09281115543151, 0.8899811598910946]),
qatom(atom.H, [28.140169589916262, -41.09281115543151, -0.8899811598910946]),
qatom(atom.C, [27.62633859682868, -42.985144673815824, 0.0]),
qatom(atom.H, [27.112507603741093, -43.34847819220014, 0.8899811598910946]),
qatom(atom.H, [27.112507603741093, -43.34847819220014, -0.8899811598910946]),
qatom(atom.C, [29.067893804958818, -43.49481082132111, 0.0]),
qatom(atom.H, [29.581724798046405, -43.131477302936794, 0.8899811598910946]),
qatom(atom.H, [29.581724798046405, -43.131477302936794, -0.8899811598910946]),
qatom(atom.C, [29.067893804958825, -45.023810821321106, 0.0]),
qatom(atom.H, [28.554062811871237, -45.38714433970542, 0.8899811598910946]),
qatom(atom.H, [28.554062811871237, -45.38714433970542, -0.8899811598910946]),
qatom(atom.C, [30.50944901308896, -45.53347696882639, 0.0]),
qatom(atom.H, [31.02328000617655, -45.170143450442076, 0.8899811598910946]),
qatom(atom.H, [31.02328000617655, -45.170143450442076, -0.8899811598910946]),
qatom(atom.C, [30.509449013088968, -47.06247696882639, 0.0]),
qatom(atom.H, [29.99561802000138, -47.425810487210704, 0.8899811598910946]),
qatom(atom.H, [29.99561802000138, -47.425810487210704, -0.8899811598910946]),
qatom(atom.C, [31.951004221219105, -47.572143116331674, 0.0]),
qatom(atom.H, [32.46483521430669, -47.20880959794736, 0.8899811598910946]),
qatom(atom.H, [32.46483521430669, -47.20880959794736, -0.8899811598910946]),
qatom(atom.C, [31.95100422121911, -49.10114311633167, 0.0]),
qatom(atom.H, [31.437173228131524, -49.464476634715986, 0.8899811598910946]),
qatom(atom.H, [31.437173228131524, -49.464476634715986, -0.8899811598910946]),
qatom(atom.C, [33.39255942934925, -49.610809263836956, 0.0]),
qatom(atom.H, [33.906390422436836, -49.24747574545264, 0.8899811598910946]),
qatom(atom.H, [33.906390422436836, -49.24747574545264, -0.8899811598910946]),
qatom(atom.C, [33.392559429349255, -51.13980926383695, 0.0]),
qatom(atom.H, [32.87872843626167, -51.50314278222127, 0.8899811598910946]),
qatom(atom.H, [32.87872843626167, -51.50314278222127, -0.8899811598910946]),
qatom(atom.C, [34.83411463747939, -51.64947541134224, 0.0]),
qatom(atom.H, [35.347945630566976, -51.28614189295792, 0.8899811598910946]),
qatom(atom.H, [35.347945630566976, -51.28614189295792, -0.8899811598910946]),
qatom(atom.H, [34.834114637479395, -52.73947541134224, 0.0]),
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

acene = [
qatom(atom.C, [0, 0, 0]),
qatom(atom.C, [0.0, 1.391143447420143, 0.0]),
qatom(atom.C, [-1.2047655657741054, 2.086715171130214, 0.0]),
qatom(atom.C, [-2.4095311315482104, 1.3911434474201414, 0.0]),
qatom(atom.C, [-2.409531131548209, -1.5543122344752192e-15, 0.0]),
qatom(atom.C, [-1.204765565774103, -0.6955717237100716, 0.0]),
qatom(atom.H, [0.9480550773161863, -0.5473598540950914, 0.0]),
qatom(atom.H, [0.9480550773161859, 1.9385033015152353, 0.0]),
qatom(atom.H, [-1.2047655657741065, 3.1814348793203973, 0.0]),
qatom(atom.H, [-3.3575862088643973, 1.9385033015152318, 0.0]),
qatom(atom.H, [-3.3575862088643946, -0.5473598540950945, 0.0]),
qatom(atom.C, [-1.2047655657741012, -2.211821723710072, 0.0]),
qatom(atom.H, [-1.7185965588616896, -2.575155242094386, 0.8899811598910946]),
qatom(atom.H, [-1.7185965588616896, -2.575155242094386, -0.8899811598910946]),
qatom(atom.C, [0.23678964235603317, -2.7214878712153623, 0.0]),
qatom(atom.H, [0.7506206354436212, -2.358154352831048, 0.8899811598910946]),
qatom(atom.H, [0.7506206354436212, -2.358154352831048, -0.8899811598910946]),
qatom(atom.C, [0.2367896423560351, -4.250487871215363, 0.0]),
qatom(atom.H, [-0.2770413507315533, -4.613821389599677, 0.8899811598910946]),
qatom(atom.H, [-0.2770413507315533, -4.613821389599677, -0.8899811598910946]),
qatom(atom.C, [1.6783448504861695, -4.7601540187206535, 0.0]),
qatom(atom.H, [2.1921758435737577, -4.3968205003363385, 0.8899811598910946]),
qatom(atom.H, [2.1921758435737577, -4.3968205003363385, -0.8899811598910946]),
qatom(atom.C, [1.678344850486171, -6.289154018720653, 0.0]),
qatom(atom.H, [1.1645138573985827, -6.652487537104967, 0.8899811598910946]),
qatom(atom.H, [1.1645138573985827, -6.652487537104967, -0.8899811598910946]),
qatom(atom.C, [3.1199000586163055, -6.798820166225944, 0.0]),
qatom(atom.H, [3.6337310517038937, -6.435486647841629, 0.8899811598910946]),
qatom(atom.H, [3.6337310517038937, -6.435486647841629, -0.8899811598910946]),
qatom(atom.C, [3.119900058616307, -8.327820166225944, 0.0]),
qatom(atom.H, [2.606069065528718, -8.691153684610258, 0.8899811598910946]),
qatom(atom.H, [2.606069065528718, -8.691153684610258, -0.8899811598910946]),
qatom(atom.C, [4.561455266746441, -8.837486313731235, 0.0]),
qatom(atom.H, [5.07528625983403, -8.474152795346921, 0.8899811598910946]),
qatom(atom.H, [5.07528625983403, -8.474152795346921, -0.8899811598910946]),
qatom(atom.C, [4.561455266746443, -10.366486313731235, 0.0]),
qatom(atom.H, [4.047624273658855, -10.729819832115549, 0.8899811598910946]),
qatom(atom.H, [4.047624273658855, -10.729819832115549, -0.8899811598910946]),
qatom(atom.C, [6.003010474876578, -10.876152461236526, 0.0]),
qatom(atom.H, [6.516841467964166, -10.512818942852212, 0.8899811598910946]),
qatom(atom.H, [6.516841467964166, -10.512818942852212, -0.8899811598910946]),
qatom(atom.C, [6.00301047487658, -12.405152461236526, 0.0]),
qatom(atom.H, [5.489179481788991, -12.76848597962084, 0.8899811598910946]),
qatom(atom.H, [5.489179481788991, -12.76848597962084, -0.8899811598910946]),
qatom(atom.C, [7.444565683006714, -12.914818608741816, 0.0]),
qatom(atom.H, [7.958396676094303, -12.551485090357502, 0.8899811598910946]),
qatom(atom.H, [7.958396676094303, -12.551485090357502, -0.8899811598910946]),
qatom(atom.C, [7.444565683006716, -14.443818608741816, 0.0]),
qatom(atom.H, [6.930734689919127, -14.80715212712613, 0.8899811598910946]),
qatom(atom.H, [6.930734689919127, -14.80715212712613, -0.8899811598910946]),
qatom(atom.C, [8.886120891136851, -14.953484756247107, 0.0]),
qatom(atom.H, [9.39995188422444, -14.590151237862793, 0.8899811598910946]),
qatom(atom.H, [9.39995188422444, -14.590151237862793, -0.8899811598910946]),
qatom(atom.C, [8.886120891136853, -16.482484756247107, 0.0]),
qatom(atom.H, [8.372289898049265, -16.845818274631423, 0.8899811598910946]),
qatom(atom.H, [8.372289898049265, -16.845818274631423, -0.8899811598910946]),
qatom(atom.C, [10.327676099266988, -16.992150903752396, 0.0]),
qatom(atom.H, [10.841507092354576, -16.62881738536808, 0.8899811598910946]),
qatom(atom.H, [10.841507092354576, -16.62881738536808, -0.8899811598910946]),
qatom(atom.C, [10.327676099266991, -18.521150903752396, 0.0]),
qatom(atom.H, [9.813845106179404, -18.884484422136712, 0.8899811598910946]),
qatom(atom.H, [9.813845106179404, -18.884484422136712, -0.8899811598910946]),
qatom(atom.C, [11.769231307397126, -19.030817051257685, 0.0]),
qatom(atom.H, [12.283062300484714, -18.66748353287337, 0.8899811598910946]),
qatom(atom.H, [12.283062300484714, -18.66748353287337, -0.8899811598910946]),
qatom(atom.C, [11.76923130739713, -20.559817051257685, 0.0]),
qatom(atom.H, [11.255400314309542, -20.923150569642, 0.8899811598910946]),
qatom(atom.H, [11.255400314309542, -20.923150569642, -0.8899811598910946]),
qatom(atom.C, [13.210786515527264, -21.069483198762974, 0.0]),
qatom(atom.H, [13.724617508614852, -20.706149680378658, 0.8899811598910946]),
qatom(atom.H, [13.724617508614852, -20.706149680378658, -0.8899811598910946]),
qatom(atom.C, [13.210786515527268, -22.598483198762974, 0.0]),
qatom(atom.H, [12.69695552243968, -22.96181671714729, 0.8899811598910946]),
qatom(atom.H, [12.69695552243968, -22.96181671714729, -0.8899811598910946]),
qatom(atom.C, [14.652341723657402, -23.108149346268263, 0.0]),
qatom(atom.H, [15.16617271674499, -22.744815827883947, 0.8899811598910946]),
qatom(atom.H, [15.16617271674499, -22.744815827883947, -0.8899811598910946]),
qatom(atom.C, [14.652341723657406, -24.637149346268263, 0.0]),
qatom(atom.H, [14.138510730569818, -25.00048286465258, 0.8899811598910946]),
qatom(atom.H, [14.138510730569818, -25.00048286465258, -0.8899811598910946]),
qatom(atom.C, [16.09389693178754, -25.146815493773552, 0.0]),
qatom(atom.H, [16.607727924875128, -24.783481975389236, 0.8899811598910946]),
qatom(atom.H, [16.607727924875128, -24.783481975389236, -0.8899811598910946]),
qatom(atom.C, [16.093896931787544, -26.675815493773552, 0.0]),
qatom(atom.H, [15.580065938699956, -27.039149012157868, 0.8899811598910946]),
qatom(atom.H, [15.580065938699956, -27.039149012157868, -0.8899811598910946]),
qatom(atom.C, [17.53545213991768, -27.18548164127884, 0.0]),
qatom(atom.H, [18.049283133005268, -26.822148122894525, 0.8899811598910946]),
qatom(atom.H, [18.049283133005268, -26.822148122894525, -0.8899811598910946]),
qatom(atom.C, [17.535452139917684, -28.71448164127884, 0.0]),
qatom(atom.H, [17.021621146830096, -29.077815159663157, 0.8899811598910946]),
qatom(atom.H, [17.021621146830096, -29.077815159663157, -0.8899811598910946]),
qatom(atom.C, [18.97700734804782, -29.22414778878413, 0.0]),
qatom(atom.H, [19.490838341135408, -28.860814270399814, 0.8899811598910946]),
qatom(atom.H, [19.490838341135408, -28.860814270399814, -0.8899811598910946]),
qatom(atom.C, [18.977007348047824, -30.75314778878413, 0.0]),
qatom(atom.H, [18.463176354960236, -31.116481307168446, 0.8899811598910946]),
qatom(atom.H, [18.463176354960236, -31.116481307168446, -0.8899811598910946]),
qatom(atom.C, [20.41856255617796, -31.26281393628942, 0.0]),
qatom(atom.H, [20.932393549265548, -30.899480417905103, 0.8899811598910946]),
qatom(atom.H, [20.932393549265548, -30.899480417905103, -0.8899811598910946]),
qatom(atom.C, [20.418562556177964, -32.791813936289415, 0.0]),
qatom(atom.H, [19.904731563090376, -33.15514745467373, 0.8899811598910946]),
qatom(atom.H, [19.904731563090376, -33.15514745467373, -0.8899811598910946]),
qatom(atom.C, [21.8601177643081, -33.3014800837947, 0.0]),
qatom(atom.H, [22.373948757395688, -32.938146565410385, 0.8899811598910946]),
qatom(atom.H, [22.373948757395688, -32.938146565410385, -0.8899811598910946]),
qatom(atom.C, [21.860117764308107, -34.8304800837947, 0.0]),
qatom(atom.H, [21.34628677122052, -35.19381360217901, 0.8899811598910946]),
qatom(atom.H, [21.34628677122052, -35.19381360217901, -0.8899811598910946]),
qatom(atom.C, [23.301672972438244, -35.34014623129998, 0.0]),
qatom(atom.H, [23.81550396552583, -34.97681271291567, 0.8899811598910946]),
qatom(atom.H, [23.81550396552583, -34.97681271291567, -0.8899811598910946]),
qatom(atom.C, [23.30167297243825, -36.86914623129998, 0.0]),
qatom(atom.H, [22.787841979350663, -37.232479749684295, 0.8899811598910946]),
qatom(atom.H, [22.787841979350663, -37.232479749684295, -0.8899811598910946]),
qatom(atom.C, [24.743228180568387, -37.378812378805264, 0.0]),
qatom(atom.H, [25.257059173655975, -37.01547886042095, 0.8899811598910946]),
qatom(atom.H, [25.257059173655975, -37.01547886042095, -0.8899811598910946]),
qatom(atom.C, [24.743228180568394, -38.90781237880526, 0.0]),
qatom(atom.H, [24.229397187480807, -39.27114589718958, 0.8899811598910946]),
qatom(atom.H, [24.229397187480807, -39.27114589718958, -0.8899811598910946]),
qatom(atom.C, [26.18478338869853, -39.417478526310546, 0.0]),
qatom(atom.H, [26.69861438178612, -39.05414500792623, 0.8899811598910946]),
qatom(atom.H, [26.69861438178612, -39.05414500792623, -0.8899811598910946]),
qatom(atom.C, [26.184783388698538, -40.94647852631054, 0.0]),
qatom(atom.H, [25.67095239561095, -41.30981204469486, 0.8899811598910946]),
qatom(atom.H, [25.67095239561095, -41.30981204469486, -0.8899811598910946]),
qatom(atom.C, [27.626338596828674, -41.45614467381583, 0.0]),
qatom(atom.H, [28.140169589916262, -41.09281115543151, 0.8899811598910946]),
qatom(atom.H, [28.140169589916262, -41.09281115543151, -0.8899811598910946]),
qatom(atom.C, [27.62633859682868, -42.985144673815824, 0.0]),
qatom(atom.H, [27.112507603741093, -43.34847819220014, 0.8899811598910946]),
qatom(atom.H, [27.112507603741093, -43.34847819220014, -0.8899811598910946]),
qatom(atom.C, [29.067893804958818, -43.49481082132111, 0.0]),
qatom(atom.H, [29.581724798046405, -43.131477302936794, 0.8899811598910946]),
qatom(atom.H, [29.581724798046405, -43.131477302936794, -0.8899811598910946]),
qatom(atom.C, [29.067893804958825, -45.023810821321106, 0.0]),
qatom(atom.H, [28.554062811871237, -45.38714433970542, 0.8899811598910946]),
qatom(atom.H, [28.554062811871237, -45.38714433970542, -0.8899811598910946]),
qatom(atom.C, [30.50944901308896, -45.53347696882639, 0.0]),
qatom(atom.H, [31.02328000617655, -45.170143450442076, 0.8899811598910946]),
qatom(atom.H, [31.02328000617655, -45.170143450442076, -0.8899811598910946]),
qatom(atom.C, [30.509449013088968, -47.06247696882639, 0.0]),
qatom(atom.H, [29.99561802000138, -47.425810487210704, 0.8899811598910946]),
qatom(atom.H, [29.99561802000138, -47.425810487210704, -0.8899811598910946]),
qatom(atom.C, [31.951004221219105, -47.572143116331674, 0.0]),
qatom(atom.H, [32.46483521430669, -47.20880959794736, 0.8899811598910946]),
qatom(atom.H, [32.46483521430669, -47.20880959794736, -0.8899811598910946]),
qatom(atom.C, [31.95100422121911, -49.10114311633167, 0.0]),
qatom(atom.H, [31.437173228131524, -49.464476634715986, 0.8899811598910946]),
qatom(atom.H, [31.437173228131524, -49.464476634715986, -0.8899811598910946]),
qatom(atom.C, [33.39255942934925, -49.610809263836956, 0.0]),
qatom(atom.H, [33.906390422436836, -49.24747574545264, 0.8899811598910946]),
qatom(atom.H, [33.906390422436836, -49.24747574545264, -0.8899811598910946]),
qatom(atom.C, [33.392559429349255, -51.13980926383695, 0.0]),
qatom(atom.H, [32.87872843626167, -51.50314278222127, 0.8899811598910946]),
qatom(atom.H, [32.87872843626167, -51.50314278222127, -0.8899811598910946]),
qatom(atom.C, [34.83411463747939, -51.64947541134224, 0.0]),
qatom(atom.H, [35.347945630566976, -51.28614189295792, 0.8899811598910946]),
qatom(atom.H, [35.347945630566976, -51.28614189295792, -0.8899811598910946]),
qatom(atom.H, [34.834114637479395, -52.73947541134224, 0.0]),
]
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
# orig frozen ... 56.00
# orig closed ... 165.00
# orb info end ------------
### CASSCF calculations
casscf.scfinp = key.scfread
casscf.orbconfig = "symlist"
casscf.frozen = [0]
casscf.closed = [218]
casscf.occ = [6]
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
icmr.frozen = [56]
icmr.closed = [162]
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
lct.UseNaiveMapPAOs = False
lct.DomScheme = 'Scheme1'
lct.TCutDOI = 1e-3
lct.TCutDOI_Active = 5e-3
lct.TCutDOI_PAO = 1e-2
lct.UseNewDomain = True
lct.FormLVOs = True
lct.UseVM1_CD   = True
lct.UseVM12     = (not lct.UseVM1_CD)
# Crude screening
lct.DoTwoStepGuess = True
lct.TCutPairs_Crude = 5e-6
lct.TCutDOI_PAO_Crude = 1e-1
lct.TCutDOI_Crude = 1e-2
lct.PrintAllEps = False


lct.PrintPairDistDBG = True
lct.PrintMapsDBG     = True

lct.LocMet = "PSM"
lct.LocRecursive = True
lct.LocMeasure = True
hint.nroots = 1
hint.nconvroots = 1

# new PMNR scheme threshold (impl = sparse, locrec = True)
lct.PMMaxIt = 20
lct.PMStep = 0.1
lct.GThresh = 5.0e-3
lct.IterLevel = 2
#hint.PM_nontrunc_incore = False
hint.PM_trunc_thresh = 1e-1
hint.PM_AB_thresh = 5e-2
hint.PM_ang_thresh = 5e-4
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

