#!/usr/bin/env python3

"""Author: Peter Meyer, SBGrid Consortium
Documentation by Alice Eruera, SBGrid Consortium

This script can be used to replace the absolute paths in .settings or 
.xml files with a new absolute path. This is useful for cases where 
a WarpTools directory has been moved or renamed, and the old absolute path
is still present in all of settings and metadata files inside 
the /warp_frameseries/ folder. MTools and WarpTools need the path to the raw 
frames present in these files. You cannot use WarpTools or MTools inside the moved or
renamed directory if you don't change the path in all of the /warp_frameseries/*.xml files.

To use, adjust the 'old' and 'new' full paths as required. Adjust the 'gs' 
to include the file extension of your choice (i.e. if you want to replace
the paths of the .xml files, set gs = ['*.xml'] on line 24). 

"""

# previous full path
old=r'/nfs/hms/Sliz/aeruera/workshop/subset7/'
# new full path
new='/nfs/hms/Sliz/aeruera/workshop/nov6_subset7/'
# slight annoyance with file extensions and recursive globbing
gs = ['*.xml']
#gs = ['*.settings','*/*.xml']

import glob
import re
from itertools import chain

debug=True
p = re.compile(old)
fs = list( chain.from_iterable( [ glob.glob(g,recursive=True) for g in gs] ) )
if debug:
    print('%d files to change'%len(fs))

def snr(fn):
    with open(fn,'r') as inp:
        txt0 = inp.read()
    txt1 = p.sub(new, txt0)
    with open(fn,'w') as opf:
        opf.write(txt1)

for f in fs:
    if debug:
        print('\tprocessing %s : replacing "%s" with "%s"'%(f,old,new))
    snr(f)

print('done')
