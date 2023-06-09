#!/bin/bash
actmod(){
    Name=$1
    Dir=$2
    active=`echo $Name | grep -o 'act[0-9]\+'`
    echo $active
    active=${active:3}
    tmps=(${active//-/ })
    active_occ=${tmps[0]}
    active_vir=${tmps[1]}
    closed=`grep 'icmr.closed' $Dir$Name.py | grep -o '[0-9]\+'`
    occ=`grep 'icmr.occ' $Dir$Name.py | grep -o '[0-9]\+'`
    echo $active_occ
    echo $active_vir
    echo $closed
    echo $occ
    closed=`expr $closed + $occ - $active_occ`
    active=`expr $active_occ + $active_vir`
    echo $closed
    echo $active
    sed -i -e "s/icmr.closed\s*=.*/icmr.closed = \[$closed\]/g" $Dir$Name.py 
    sed -i -e "s/icmr.occ\s*=.*/icmr.occ = \[$active\]/g" $Dir$Name.py 
}
svptzvpp(){
    # argument
    pypath=$1
    molname=$2
    # body
    case $molname in
        cbi-cbi)
            sed -i -e "s/qatom(atom.Co, \[-0.9156048, 0.0390834, -0.8642740\]),/qatom(atom.Co, \[-0.9156048, 0.0390834, -0.8642740\],basis=Cotz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.8195824, 0.8147177, 0.8209597\]),/qatom(atom.N, \[-0.8195824, 0.8147177, 0.8209597\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-2.2850331, -1.1229302, -0.2508607\]),/qatom(atom.N, \[-2.2850331, -1.1229302, -0.2508607\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.7859032, -0.7294625, -2.5929226\]),/qatom(atom.N, \[-0.7859032, -0.7294625, -2.5929226\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.2829723, 1.3909292, -1.3165220\]),/qatom(atom.N, \[0.2829723, 1.3909292, -1.3165220\],basis=Ntz),/g" $pypath
            ;;
        cbi-mecbi)
            sed -i -e "s/qatom(atom.Co, \[-0.9277729, 0.0805031, -0.8561488\]),/qatom(atom.Co, \[-0.9277729, 0.0805031, -0.8561488\],basis=Cotz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.7743989, 0.7950721, 0.8464786\]),/qatom(atom.N, \[-0.7743989, 0.7950721, 0.8464786\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-2.2094081, -1.1514044, -0.1979500\]),/qatom(atom.N, \[-2.2094081, -1.1514044, -0.1979500\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.7145177, -0.7556392, -2.5403982\]),/qatom(atom.N, \[-0.7145177, -0.7556392, -2.5403982\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.3560117, 1.3534216, -1.2714341\]),/qatom(atom.N, \[0.3560117, 1.3534216, -1.2714341\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.C, \[-2.3771894, 1.2474442, -1.4619199\]),/qatom(atom.C, \[-2.3771894, 1.2474442, -1.4619199\],basis=Ctz),/g" $pypath
            ;;
        cbi-adocbi)
            sed -i -e "s/qatom(atom.Co, \[-0.1325164, -0.2500157, -0.6640851\]),/qatom(atom.Co, \[-0.1325164, -0.2500157, -0.6640851\],basis=Cotz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.0026118, 0.5100454, 1.0198611\]),/qatom(atom.N, \[-0.0026118, 0.5100454, 1.0198611\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-1.3365752, -1.5366358, 0.0589505\]),/qatom(atom.N, \[-1.3365752, -1.5366358, 0.0589505\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.1291755, -1.1368293, -2.3121006\]),/qatom(atom.N, \[0.1291755, -1.1368293, -2.3121006\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[1.1555950, 1.0300847, -1.0923081\]),/qatom(atom.N, \[1.1555950, 1.0300847, -1.0923081\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.C, \[-1.7567646, 0.6605027, -1.3253577\]),/qatom(atom.C, \[-1.7567646, 0.6605027, -1.3253577\],basis=Ctz),/g" $pypath
            ;;
        cbi-ch3)
            sed -i -e "s/qatom(atom.C, \[0.0000000, 0.0000000, 0.0000000\]),/qatom(atom.C, \[0.0000000, 0.0000000, 0.0000000\],basis=Ctz),/g" $pypath
            ;;
        cbi-ado)
            sed -i -e "s/qatom(atom.C, \[1.8911201, -2.9337929, 1.7338849\]),/qatom(atom.C, \[1.8911201, -2.9337929, 1.7338849\],basis=Ctz),/g" $pypath
            ;;
        cbl-cbl)
            sed -i -e "s/qatom(atom.Co, \[0.0, 0.0, 0.0\]),/qatom(atom.Co, \[0.0, 0.0, 0.0\],basis=Cotz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.5677310000000091, 0.5689624999999978, 1.6866629\]),/qatom(atom.N, \[0.5677310000000091, 0.5689624999999978, 1.6866629\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.5763948000000028, 1.6852339999999941, -0.7715195000000001\]),/qatom(atom.N, \[0.5763948000000028, 1.6852339999999941, -0.7715195000000001\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.47099219999999775, -0.8204904000000042, -1.6760753\]),/qatom(atom.N, \[-0.47099219999999775, -0.8204904000000042, -1.6760753\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.028360199999994506, -1.6837811000000045, 0.8333446000000002\]),/qatom(atom.N, \[-0.028360199999994506, -1.6837811000000045, 0.8333446000000002\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-2.0843606999999906, 0.5843051999999958, 0.2988528000000006\]),/qatom(atom.N, \[-2.0843606999999906, 0.5843051999999958, 0.2988528000000006\],basis=Ntz),/g" $pypath 
            ;;
        cbl-mecbl)
            sed -i -e "s/qatom(atom.Co, \[0.0, 0.0, 0.0\]),/qatom(atom.Co, \[0.0, 0.0, 0.0\],basis=Cotz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.4836255999999963, 0.5960138999999955, 1.7100990000000005\]),/qatom(atom.N, \[0.4836255999999963, 0.5960138999999955, 1.7100990000000005\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.42402299999999116, 1.7424594999999954, -0.7394483999999997\]),/qatom(atom.N, \[0.42402299999999116, 1.7424594999999954, -0.7394483999999997\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.6002676000000093, -0.7897720000000064, -1.6500312\]),/qatom(atom.N, \[-0.6002676000000093, -0.7897720000000064, -1.6500312\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.16466739999999902, -1.6524801000000053, 0.8743436000000004\]),/qatom(atom.N, \[-0.16466739999999902, -1.6524801000000053, 0.8743436000000004\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-2.0945893000000098, 0.5994516999999959, 0.3410346000000004\]),/qatom(atom.N, \[-2.0945893000000098, 0.5994516999999959, 0.3410346000000004\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.C, \[1.859710899999996, -0.4795408000000023, -0.4471097999999998\]),/qatom(atom.C, \[1.859710899999996, -0.4795408000000023, -0.4471097999999998\],basis=Ctz),/g" $pypath           
            ;;
        cbl-adocbl)
            sed -i -e "s/qatom(atom.Co, \[0.0, 0.0, 0.0\]),/qatom(atom.Co, \[0.0, 0.0, 0.0\],basis=Cotz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.40824250000000006, 0.6015011000000001, 1.7316289999999999\]),/qatom(atom.N, \[0.40824250000000006, 0.6015011000000001, 1.7316289999999999\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[0.3068669999999969, 1.7664769000000007, -0.7215834999999995\]),/qatom(atom.N, \[0.3068669999999969, 1.7664769000000007, -0.7215834999999995\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.6167166000000037, -0.7862610999999973, -1.6381128\]),/qatom(atom.N, \[-0.6167166000000037, -0.7862610999999973, -1.6381128\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-0.016998799999996095, -1.670447100000004, 0.8606149999999992\]),/qatom(atom.N, \[-0.016998799999996095, -1.670447100000004, 0.8606149999999992\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.N, \[-2.132317900000004, 0.45884639999999877, 0.3567916000000002\]),/qatom(atom.N, \[-2.132317900000004, 0.45884639999999877, 0.3567916000000002\],basis=Ntz),/g" $pypath
            sed -i -e "s/qatom(atom.C, \[1.9385895000000062, -0.30690220000000323, -0.3479473999999998\]),/qatom(atom.C, \[1.9385895000000062, -0.30690220000000323, -0.3479473999999998\],basis=Ctz),/g" $pypath
            ;;
        cbl-ch3)
            sed -i -e "s/qatom(atom.C, \[0.1965046, -0.4168260, -0.0000031\]),/qatom(atom.C, \[0.1965046, -0.4168260, -0.0000031\],basis=Ctz),/g" $pypath
            ;;
        cbl-ado)
            sed -i -e "s/qatom(atom.C, \[76.7727923, -57.5400357, 8.3515338\]),/qatom(atom.C, \[76.7727923, -57.5400357, 8.3515338\],basis=Ctz),/g" $pypath
            ;;
        *)
            echo 'undefined mybasis option'
            exit 1;;
    esac
}
mybasis(){
    # argument
    pypath=$1
    basistype=$2
    molname=$3
    # body
    case $basistype in
        svptzvpp)
            svptzvpp $pypath $molname
            ;;
    esac
}
xyz2orz(){
    xyzpath=$1
    pypath=$2
    filebase=`basename $xyzpath`
    geom=
    frozen=0
    closed=0
    casclosed=0
    occ=0
    act=0
    #cp ~/clones/pybase.py ${pypath}
    Nline=0
    while read -a line || [ -n $line ]; do
        #echo $line
        [ $Nline -eq 0 ] && { Nline=`expr $Nline + 1`;continue;}
        [ $Nline -eq 1 ] && { Nline=`expr $Nline + 1`;continue;}
        [ -z $line ] && break
        [ ${#line[@]} != 4 ] && { echo ${#line[@]};Nline=`expr $Nline + 1`;continue;}
        geom="${geom}\nqatom(atom.${line[0]}, [${line[1]}, ${line[2]}, ${line[3]}]),"
        case ${line[0]} in
            H)
                closed=$((closed + 1));;
            C)
                frozen=$((frozen + 2))
                closed=$((closed + 4));;
            N)
                frozen=$((frozen + 2))
                closed=$((closed + 5));;
            O)
                frozen=$((frozen + 2))
                closed=$((closed + 6));;
            P)
                frozen=$((frozen + 10))
                closed=$((closed + 5));;
            S)
                frozen=$((frozen + 10))
                closed=$((closed + 6));;
            Cl)
                frozen=$((frozen + 10))
                closed=$((closed + 7));;
            Co)
                frozen=$((frozen + 10))
                closed=$((closed + 17));;
            Ni)
                frozen=$((frozen + 10))
                closed=$((closed + 18));;
            *)
                echo "detect undefined atom"
        esac
        Nline=`expr $Nline + 1`
    done < $xyzpath
    #frozen=`python -c "print($frozen/2)"`
    frozen="`echo "scale=2; $frozen/2 " | bc`"
    closed="`echo "scale=2; $closed/2 " | bc`"
    #[ ${frozen: -1} -ne 0 || ${closed: -1} -ne 0 ] && exit "uncorrect electron number was detected"
    [ ${frozen: -1} -ne 0 ] && exit "uncorrect electron number was detected"
    [ ${closed: -1} -ne 0 ] && exit "uncorrect electron number was detected"
    sed -i -e "s/# orb info bgn ------------/# orb info bgn ------------\n# orig frozen ... ${frozen}\n# orig closed ... ${closed}/g" ${pypath}
    
    frozen=`printf '%.0f\n' $frozen`
    closed=`printf '%.0f\n' $closed`
    #echo "geom=${geom}"
    # active modification
    tmp=(${xyzpath//\// })
    case_benzalk="benzc[0-9]*h[0-9]*.xyz"
    case ${tmp[-1]} in
        $case_benzalk)
            act=3;;
        pyfile_benzalkane)
            act=3;;
        pyfile_benzalkane3)
            act=3;;
        pyfile_general)
            act=0
    esac
    closed=$((closed - act))
    occ=$((act * 2))
    casclosed=$((frozen + closed))
    sed -i -e "s/geom = \[/geom = \[${geom}/g" ${pypath}
    sed -i -e "s/acene = .*\[/acene = \[${geom}/g" ${pypath}
    sed -i -e "s/casscf.closed = \[0\]/casscf.closed = \[$casclosed\]/g" ${pypath}
    sed -i -e "s/casscf.occ = \[0\]/casscf.occ = \[$occ\]/g" ${pypath}
    sed -i -e "s/icmr.frozen = \[0\]/icmr.frozen = \[$frozen\]/g" ${pypath}
    sed -i -e "s/icmr.closed = \[0\]/icmr.closed = \[$closed\]/g" ${pypath}
    sed -i -e "s/icmr.occ = \[0\]/icmr.occ = \[$occ\]/g" ${pypath}
    
    
}
geom2py(){
    molname=$1
    pypath=$2
    geompath=`geomdet $molname`
    xyz2orz $geompath $pypath
}
