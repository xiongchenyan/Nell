'''
Created on Oct 11, 2013
read and write test of indri packed doc res.
with DocRaw
@author: cx
'''


import site
site.addsitedir('/bos/usr4/cx/local/lib/python2.7/site-packages')
site.addsitedir('/bos/usr4/cx/cxPylib')
site.addsitedir('/bos/usr4/cx/Dropbox/workspace/python/Nell/')

from IndriRelate.IndriPackedRes import *
import sys


if 3 != len(sys.argv):
    print "2 para: input + output (will simple read and write)"
    sys.exit()
    


out = open(sys.argv[2],'w')

lPackedIndriRes = ReadPackedIndriRes(sys.argv[1])

for res in lPackedIndriRes:
    print >> out, res.out()
    
out.close()