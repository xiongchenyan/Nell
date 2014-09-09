'''
Created on Sep 8, 2014
train naive bayesian classifier using NaiveBayesianClassifier
in: Nell gloss + target class
out: a model dumped by NaiveBayesianClassifierC
@author: cx
'''

'''
1, load target class name
2, read each line in nell gloss,
    check if class ok
    clean the gloss (case to lower, discard non-english non-digit words)
    put to nb classifier
3, dump
'''


import site
site.addsitedir('/bos/usr0/cx/PyCode/cxPyLib')
site.addsitedir('/bos/usr0/cx/PyCode/cxMachineLearning')

from cxBase.TextBase import *
from TextClassification.NaiveBayesianClassifier import *


def LoadTargetClassName(InName):
    hClass = {}
    for line in open(InName):
        line = line.strip()
        hClass[line] = True
    return hClass



def TrainOnGloss(InName,OutName,hClass):
    Classifier = NaiveBayesianClassifierC()
    for line in open(InName):
        line = line.strip()
        vCol = line.split('\t')
        cate = vCol[0].split(':')[0]
        if (len(vCol) < 3):
            continue
        if cate in hClass:
            continue
        text = vCol[2]
        Classifier.AddTrainText(cate, text)
    Classifier.ReduceSize()
    Classifier.dump(OutName)
    return True


import sys

if 4 !=len(sys.argv):
    print "train nb classifier on nell gloss"
    print "3 para:gloss + target class + output"
    sys.exit()
    
    
    
hClass = LoadTargetClassName(sys.argv[2])
TrainOnGloss(sys.argv[1],sys.argv[3],hClass)

print "finished"






