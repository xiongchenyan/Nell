'''
Created on Sep 18, 2013
wrap up nell to trec web format
@author: cx
'''

import sys

#Get first line as tags, wrap up all others
#doc no is the first column

lTags=[]

def MakeTrecWebHead(MachineId):
#     res = ""
    res = "<DOC>\n<DOCNO>" + MachineId + "</DOCNO>\n"
    res += "<DOCHDR>\nhttp://fakeurl.com/" + MachineId + "\n</DOCHDR>\n"  
#     res += "<MachineId>\nMachineId" + Mid + "\n</MachineId>"  
    return res 

def MakeTrecWebTail():
    return '</DOC>\n'


def TransferLine(line):
    vCol = line.split('\t')
    res = ""
    n = min(len(vCol),len(lTags))
#     if (len(vCol) != len(lTags)):
#         print "[%s] col [%d] error" %(line,len(vCol))
    for i in range(n):
        res += "<" + lTags[i] + ">" + vCol[i] + "</" + lTags[i] + ">\n"
    return res


if 3 != len(sys.argv):
    print "2 para: NELL input + output file"
    sys.exit()

DocNo = 0    
out = open(sys.argv[2],'w')
for line in open(sys.argv[1]):
    line = line.strip()
    if DocNo == 0:
        lTags = line.split('\t')
        for i in range(len(lTags)):
            lTags[i] = lTags[i].replace(' ','')
            print "<metadata><field>%s</field></metadata>" %(lTags[i])
            print "<field><name>%s</name></field>" %(lTags[i])
        DocNo += 1
#         break
        continue
#     print "%s\t[%d]" %(str(lTags),len(lTags))
    print >> out, MakeTrecWebHead(str(DocNo))
    print >> out, TransferLine(line)
    print >> out, MakeTrecWebTail()
    DocNo += 1
    if 0 == (DocNo % 10000):
        print "processed [%d]" %(DocNo)    
out.close();
        
    