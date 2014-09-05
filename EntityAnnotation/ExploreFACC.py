'''
Created on Oct 11, 2013
check how to match FACC1's offset and DocVec
@author: cx
'''


import site
site.addsitedir('/bos/usr4/cx/local/lib/python2.7/site-packages')
site.addsitedir('/bos/usr4/cx/cxPylib')
from AnnotationRelate.AnnotationPacked import *
from IndriRelate.IndriPackedRes import *
import sys


if 4 != len(sys.argv):
    print "3 para: PackedIndriRankRes + FACC1 Dir + outname"
    sys.exit()
    
#read packed IndriRank
#for first docno read its annotation.
#show strings at each offset.
#show offset matched for each annotation. both in DocRaw and DocVec




lDoc = ReadPackedIndriRes(sys.argv[1])




OutStr = open(sys.argv[3] + 'StrNearOffset','w')
OutStringMatch = open(sys.argv[3] + 'MatcedOffset','w')
for i in range(len(lDoc)):
    #get the annotation for this document
    PackedDoc = lDoc[i]
    FName = MakeAnnotationName(sys.argv[2],PackedDoc.DocNo)
    lAnnotation = ReadAnnotation(FName)
    print >> OutStr, PackedDoc.DocNo
    print >> OutStringMatch,PackedDoc.DocNo
    print "running for [%s]" %(PackedDoc.DocNo)
    lAnnotationForDoc = SplitAnnotationForDoc(lAnnotation,PackedDoc.DocNo)
    #read all finished
    #show string near offset
    for Annotation in lAnnotationForDoc:
        print >>OutStr, Annotation.entity + "\t" +  ShowStrAtOffset(Annotation, PackedDoc,50)

    #show matched entity at offset
    for Annotation in lAnnotationForDoc:
        lIndex = StringMatchOffSet(Annotation,PackedDoc)
        print >> OutStringMatch, "#Entity:\t" + Annotation.entity
        for offset in lIndex:
            print >> OutStringMatch,PackedDoc.RawContent[offset[0]:offset[1]] + "\t[%d:%d]" %(offset[0],offset[1])
    
    
OutStr.close()
OutStringMatch.close() 

