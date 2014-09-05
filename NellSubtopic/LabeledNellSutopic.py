'''
Created on Oct 14, 2013
generated subtopic from manually labeled data
input: manually labeled trec query, XML format, nell label put in as tags for each subtopic
IE:C:\Users\cx\Dropbox\LTI\FreebaseAndSearch\data\labeling\nell\trec_diversity_all_ami_label.xml
output: subtopic
@author: cx
'''



import sys
import xml.etree.ElementTree as ET
FreebaseTar = "./freebase/name"
FreebaseMid = "./freebase/mid"
ManualTar = "./manual"
NellTar = "./nell/url"


TargetStr = NellTar

if (len(sys.argv) != 3):
    print '2 argc: input + output'
    sys.exit()
    

tree=ET.parse(sys.argv[1])

eQ = tree.findall('./topic')
print "# of st %d" %(len(eQ))

out = open(sys.argv[2],'w')

for QNode in eQ:
    number= QNode.attrib['number'];        
    text = QNode[0].text
    print "Query:" + text
    hSt = {}
    lSubtopic = QNode.findall('./subtopic')
    if TargetStr == NellTar:
        for st in lSubtopic:
            lName = st.findall(TargetStr)
            for i in range(0,len(lName)):
                name = lName[i]       
                name.text = name.text.strip()
                if (name.text != None):
                    vCol =   name.text.strip().split(':')
                    if (len(vCol) < 3):
                        continue
                    entity =vCol[2].replace('_',' ')                    
                    if(entity != ""): 
                        hSt[entity] = entity                                      
    if (len(hSt) == 0):
        print >> out, number + "\t" + text.strip() + "\t1\t#empty#\t#empty#"                         
    for sSubDes in hSt:        
        print >> out, number + "\t" + text.strip() + "\t1\t" + sSubDes.strip().replace("\t","").replace("\n","") + "\t" + hSt[sSubDes].strip().replace("\t","").replace("\n","")
    print "# of st: [%d] covered st [%d]" %(len(lSubtopic), len(hSt))    
out.close()
