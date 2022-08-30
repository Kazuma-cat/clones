#!/usr/bin/env python3
import sys
import os
filename=sys.argv[1]
refpoint=[]
with open(filename,'r') as f:
    for line in f.readlines():
        words=line.split()
        if len(words) == 0:
            continue
        if words[0] == 'Co':
            refpoint=[float(tmp) for i,tmp in enumerate(words) if not i == 0]
            pass
        pass
    pass
print(refpoint)
geom=""
geomlist=[]
with open(filename,'r') as f:
    for line in f.readlines():
        words=line.split()
        print(words)
        if not len(words) == 4:
            #geom=f'{geom}{line}\n'
            #geom='%s %s\n' %geom %line
            geom='{}{}'.format(geom, line)
            print(geom)
        else:
            if words[1] == 'Energy':
                geom='{}{}'.format(geom, line)
                print(geom)
                continue
            newpoint=[float(tmp) - refpoint[i-1] for i,tmp in enumerate(words) if not i == 0]
            #tmp="{line[0]} {newpoint[0]} {newpoint[1] {newpoint[2]}}"
            tmp="{} {} {} {}".format(words[0],newpoint[0],newpoint[1],newpoint[2])
            #geom=f'{geom}{tmp}\n'
            geom='{}{}\n'.format(geom,tmp)
            #print(geom)
            pass
        pass
    pass
#print(geom)
print(filename)
print(os.path.basename(filename))
basename = os.path.basename(filename)
outname = '/home/20/kazuma/clones/func/funcgeom/' + basename
print(outname)
with open(outname,'w') as f:
    f.write(geom)
    
