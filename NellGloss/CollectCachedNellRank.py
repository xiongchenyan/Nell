'''
Created on Sep 5, 2014
collect nell rank for queries in a cached dir
in: query, cached dir
output: qid\tquery\tnell obj \n score
@author: cx
'''

import site
site.addsitedir('/bos/usr0/cx/cxPylib')
from IndriRelate.IndriPackedRes import *

import sys
if 4 > len(sys.argv):
    print "query  + cache dir + output + (num of doc to out: 50)"
    sys.exit()
    
    
out = open(sys.argv[3],'w')
NumOfDoc = 50
if len(sys.argv) > 4:
    NumOfDoc = int(sys.argv[4])

CachedDir = sys.argv[2]
for line in open(sys.argv[1]):
    qid,query = line.strip().split('\t')
    lDoc = ReadPackedIndriRes(CachedDir + "/" + query, NumOfDoc)
    for doc in lDoc:
        print >>out, qid + '\t' + query + '\t%s\t%f' %(doc.DocNo,doc.score)
        
out.close()