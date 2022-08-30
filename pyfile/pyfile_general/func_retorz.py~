import tex_command as tex
import copy
class loc_info:
    # info is list:[molecule name, basis set, localization method]
    # jacobi_results = [closed LOMO, valence LOMO, LVMO]
    # NR_results = [valence LOMO,LVMO]    
    def __init__(self,head,jacobi_results,NR_results,Etot,Ecorr):
        self.head = head
        self.jacobi = jacobi_results
        self.NR = NR_results
        self.Etot = Etot
        self.Ecorr = Ecorr

def packing_methods(orz_infos,molname,basisset):
    packed = {}
    for info in orz_infos.values():
        if molname == info.head["MOLNAME"] and basisset == info.head["BASIS"]:
            packed[info.head["METHOD"]] = info
    return packed
            
                    
# brief get orbital localization results from orz output
# date 2020
# param filename The name of orz output(string class)
# jacobi_results = [closed LOMO, valence LOMO, LVMO]
# NR_results = [valence LOMO,LVMO]    
def get_loc_info(filename,opt_bool,jacobi_occ):
    MO_info = filename.split(".")[0].split("_")
    info_tag = ["MOLNAME","BASIS","METHOD"]
    head = dict(zip(info_tag, MO_info))
    #beginning of get information from orz's output file
    jacobi_bool = False
    NR_bool = False
    jacobi_pos = 0
    NR_pos = 0
    jacobi_results = [[],[],[]]
    if jacobi_occ == True:
        jacobi_keys = ["closed", "LOMO", "LVMO"]
    else:
        jacobi_keys = ["LOMO", "LVMO"]
    NR_results = [[],[]]
    NR_keys = ["LOMO","LVMO"]
    with open(filename) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            # jacobi terms in CONV info
            if "      Iter       <L>            Change           Time " in line:
                jacobi_bool = True
            if jacobi_bool == True:
                if line == "\n":
                    jacobi_bool = False
                    jacobi_pos+=1
                    continue
                jacobi_results[jacobi_pos].append(line)
            # NR terms in CONV info
            if "MACRO:" in line:
                NR_results[NR_pos].append(line)
                if "CONVERGED" in line:
                    NR_pos+=1
            # energy terms
            if "FINAL CORRELATION ENERGY" in line:
                Ecorr = [line.split()[4],line.split()[5]]
            if "FINAL TOTAL ENERGY" in line:
                Etot = [line.split()[4],line.split()[5]]
                    

                    
    jacobi_dic = dict(zip(jacobi_keys,jacobi_results))
    NR_dic = dict(zip(NR_keys, NR_results))

    
    ##opt if
    if opt_bool == True:
        # modify jacobi results
        jacobi_pos = [0,1]
        #jacobi pos is position of deserved jacobi results
        #here, get begging and end of iteration in each space(closed, LOMO, LVMO)
        for choice in jacobi_keys:
            jacobi_tmp1 = []
            jacobi_tmp2 = []
            if not len(jacobi_dic[choice]) == 2:
                for pos in jacobi_pos:
                    jacobi_tmp1.append(jacobi_dic[choice][1].split()[pos])
                    jacobi_tmp2.append(jacobi_dic[choice][-1].split()[pos])
                jacobi_dic[choice] = [jacobi_tmp1,jacobi_tmp2]
            else:
                for pos in jacobi_pos:
                    jacobi_tmp1.append(jacobi_dic[choice][1].split()[pos])
                jacobi_dic[choice] = [jacobi_tmp1]
        # get NR's iter and L at the first one and the end one
        NR_pos = [2,4]
        for choice in NR_keys:
            NR_tmp1 = []
            NR_tmp2 = []
            if not len(NR_dic[choice]) == 1:
                for pos in NR_pos:
                    if pos ==2:
                        tmp1 = NR_dic[choice][0].split()[pos].split("-")
                        tmp2 = NR_dic[choice][-1].split()[pos].split("-")
                        NR_tmp1.append(tmp1[0])
                        NR_tmp2.append(tmp2[0])
                    else:
                        tmp1 = NR_dic[choice][0].split()
                        tmp2 = NR_dic[choice][-1].split()
                        NR_tmp1.append(tmp1[pos])
                        NR_tmp2.append(tmp2[pos])
                NR_dic[choice] = [NR_tmp1,NR_tmp2]
            else:
                for pos in NR_pos:
                    if pos ==2:
                        tmp1 = NR_dic[choice][0].split()[pos].split("-")
                        NR_tmp1.append(tmp1[0])
                    else:
                        NR_tmp1.append(NR_dic[choice][0].split()[pos])
                NR_dic[choice] = [NR_tmp1]
    ##opt if end
    loc_info_return = loc_info(head,jacobi_dic,NR_dic,Etot,Ecorr)
    return loc_info_return

def tex_table_CONV(loc_info):
    newline = "\n"
    ntable = ["LOMO","LVMO"]
    for head in loc_info.head:
        info = str(head) + "/"
    outputname = "loc_table2.tex"
    #with open ("~/research/my_thesis/loc_table.tex",mode = "w") as doc:
    with open (outputname,mode = "w") as doc:
        print(f"name of outputfile is {outputname}")
        doc.write(tex.table_package)
        doc.write(tex.doc_i)
        for choice in ntable:
            caption = "localization"
            col2 = "L(" + choice +")"
            table = tex.ftable_i_simple(caption,"lcc","iterarion",col2)
            row0="jacobi"
            for jac in loc_info.jacobi[choice]:
                table += tex.fbodyline(jac,row0)
                row0=""
            row0 ="NR"
            for NR in loc_info.NR[choice]:
                table += tex.fbodyline(NR,row0)
                row0 =""
            table += tex.hline + tex.hline + newline
            tex.labelname = "loc"
            table += tex.ftable_f("loc") +newline
            
            doc.write(table)
        doc.write(tex.doc_f)
    return

def tex_table_Energy(method_set,molname,basis):
    newline = "\n"
    info_tags = ["MOLNAME","BASIS"]
    for tag in info_tags:
        info = str(method_set["PM"].head[tag]) + "/"
    info.strip()
    outputname = "E_"+basis+"_table.tex"
    with open (outputname,mode = "w") as doc:
        doc.write(tex.table_package)
        doc.write(tex.doc_i)
        ntable =[1]
        for choice in ntable:
            caption = " Dependence of the energy on the localiztion method." + "basisset is " + basis +"."
            table = tex.ftable_i(caption,"lcccccc")
            #form table head(this part strongly depend on each table
            table += r' &\multicolumn{2}{c}{$E_{\rm tot}$}&\multicolumn{2}{c}{$E_{\rm corr}$}&multirow{2}{*}{$\Delta E_{\rm tot}$}&multirow{2}{*}{$\Delta E_{\rm corr}$} \\ \cline{2-3} \cline{4-5}' + newline
            headtmp = ""
            for method in method_set:
                headtmp += tex.div + method
            table += headtmp + headtmp + tex.div +tex.newline + tex.hline
            PMinfo = method_set["PM"]
            PSMinfo = method_set["PSM"]
            dEtot = str(float(PMinfo.Etot[0])-float(PSMinfo.Etot[0]))
            dEcorr = str(float(PMinfo.Ecorr[0])-float(PSMinfo.Ecorr[0]))
            table += newline + molname + tex.div + PMinfo.Etot[0] + tex.div + PSMinfo.Etot[0] + tex.div + PMinfo.Ecorr[0] + tex.div + PSMinfo.Ecorr[0] + tex.div + dEtot + tex.div + dEcorr + tex.newline
            table += tex.hline + tex.hline + newline
            labelname = "locmet"
            table += tex.ftable_f(labelname) +newline
            
            doc.write(table)
        doc.write(tex.doc_f)
    return









