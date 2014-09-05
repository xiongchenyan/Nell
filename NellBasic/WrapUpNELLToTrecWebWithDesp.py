'''
Created on Dec 4, 2013
wrap up NELL, but with description extracted from CPL format
input must be sorted so that same concept in first column is grouped together
@author: cx
'''

import sys
from NellGeneralC import *


if 3 != len(sys.argv):
    print "NELL General sorted + output trec web file"
    sys.exit()

OneConcept = NellGeneralC()    
cnt = 0
errcnt = 0
out = open(sys.argv[2],'w')
for line in open(sys.argv[1]):
    line = line.strip()    
    if not OneConcept.Append(line):
        try:
            print >>out, OneConcept.OutTrecWeb().decode('utf8',"ignore")
        except UnicodeEncodeError:
            errcnt += 1
        cnt += 1
        if 0 == (cnt % 100):
            print "processed [%d] concepts [%d] decode error" %(cnt,errcnt)
        OneConcept = NellGeneralC()
        OneConcept.Append(line)
print "finished [%d] [%d] err" %(cnt,errcnt)
out.close()  
