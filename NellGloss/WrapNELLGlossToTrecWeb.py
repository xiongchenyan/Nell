'''
Created on Sep 5, 2014
in: nell gloss provided by Bhavana
out: wrapped up in TrecWeb format to index

do:
in format: entity\t surface form \t gloss \t candidate entity
Will Ansign a DocNo nell-gloss-%d
entity treated as DocTitle
surface form as <surface>
gloss is the body <body>
candidate entity ignored
@author: cx
'''


def WrapOneGloss(line,DocNo):
    sOut = ""
    vCol = line.strip().split('\t')
    if len(vCol) < 3:
        print "error line: " + line
        return ""
    entity,surface,gloss = vCol[:3]
    sOut += MakeTrecWebHead(DocNo) + '\t'
    sOut += '<title>%s</title>\n' %(entity)
    sOut += '<surface>%s</surface>\n' %(surface)
    sOut += '<body>%s</body>\n' %(gloss)
    
    sOut += '</Doc>\n'
    
    return sOut
    
    
def MakeTrecWebHead(DocNo):
    res = "<DOC>\n<DOCNO>" + DocNo + "</DOCNO>\n"
    res += "<DOCHDR>\nhttp://fakeurl.com/" + DocNo + "\n</DOCHDR>\n"  
    return res 




import sys

if 3 != len(sys.argv):
    print "nell gloss + output"
    sys.exit()
    
out = open(sys.argv[2],'w')

DocNo = 0

for line in open(sys.argv[1]):
    sOut = WrapOneGloss(line,DocNo)
    if sOut == '':
        continue
    try:
        print >> out, sOut
        DocNo += 1
    except UnicodeDecodeError:
        continue
    
print 'finished total [%d] successful gloss' %(DocNo)
out.close()


    
    
