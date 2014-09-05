'''
Created on Oct 9, 2013
count the number of facts from each extraction method
@author: cx
'''

import site
site.addsitedir('/bos/usr4/cx/local/lib/python2.7/site-packages')
site.addsitedir('/bos/usr4/cx/cxPylib')
site.addsitedir('/bos/usr4/cx/Dropbox/workspace/python/Nell/')
import sys
from NellBasic.NellGeneralC import *
from operator import itemgetter

#simply read each line, get candidate string and then put to dict


if (3 != len(sys.argv)):
    print "2 para: NELl_General + Count result of candidate sources"
    sys.exit()
    
bIsHead = True
OutCnt = open(sys.argv[2] + '_count','w')
hCandSource={}
out = open(sys.argv[2]+'_RawSource','w')
for line in open(sys.argv[1]):
    line = line.strip()
    if bIsHead:
        bIsHead = False;
        continue
    NellData = NellGeneralC()
    NellData.Set(line)
    lCandSource = NellData.GetCandidateSourceCategory()
    print >> out,NellData.GetField('Candidate Source').encode('utf8')
    for CandSource in lCandSource:
        if not CandSource in hCandSource:
            hCandSource[CandSource] = 0
        hCandSource[CandSource] += 1
    
out.close();
lCandSourceCnt= []
for item in hCandSource:
    lCandSourceCnt.append((item,hCandSource[item]))
lCandSourceCnt.sort(key=itemgetter(1),reverse=True)
for item in lCandSourceCnt:
    print >> OutCnt,'%s\t%d' %(item[0].encode('utf8'),item[1])
    
OutCnt.close()
