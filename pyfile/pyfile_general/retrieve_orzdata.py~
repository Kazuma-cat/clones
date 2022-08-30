import func_retorz as func
import sys
print(" ---------------------------- ")
print("        retrive_orzdata       ")
print(" ---------------------------- ")
filenames = ["DPP_def2svp_PM.py.lct","DPP_def2svp_PSM.py.lct"]
molnames = {filename.split("_")[0] for filename in filenames}
#infos =[func.get_loc_info(filename,True) for filename in filenames]
#for filename in filenames:    
#    info = func.get_loc_info(filename,True)
#    infos.append(info)
print("make loc_ info object")
orz_infos = {filename: func.get_loc_info(filename,True,False) for filename in filenames}
print(orz_infos)
DPP_svp = func.packing_methods(orz_infos,"DPP","def2svp")
print(DPP_svp)
func.tex_table_Energy(DPP_svp,"DPP","def2svp")

#orz_infos = dict(zip(filenames, infos))
#print(f'head = {orz["c4h6_def2svp_PM.py.lct"].head}')
#print(f"Etot = {loc_info.Etot}")
#print(f"Ecorr = {loc_info.Ecorr}")
#print(f"loc_info.info= {loc_info.info}")
#print(f'jacobi_OMO_closed = {loc_info.jacobi["closed"]}')
#print(f'jacobi_OMO_valence = {loc_info.jacobi["LOMO"]}')
#print(f'jacobi_VMO = {loc_info.jacobi["LVMO"]}')
#print(f'NR_OMO = {loc_info.NR["LOMO"]}')
#print(f'NR_VMO = {loc_info.NR["LVMO"]}')
#print(f'jacobi.split = {loc_info.jacobi["LOMO"][1]}')    
#print(f'jacobi.split = {loc_info.jacobi["LOMO"][1].split()}')
#print(f'NR.split = {loc_info.NR["LOMO"][0].split()}')
print("make table about convergence")
for filename in filenames:
    func.tex_table_CONV(orz_infos[filename])
