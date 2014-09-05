'''
Created on Oct 9, 2013
General class of NELl.
set from each line of NELL_General
@author: cx
'''

import urllib
import json
class NellGeneralC:
    lField = []
    hField = []
    llValue = []
    concept = ""
    
    
    def __init__(self):
        self.lField = ["Entity","Relation","Value","Iteration of Promotion","Probability","Source","Entity literalStrings","Value literalStrings","Best Entity literalString","Best Value literalString","Categories for Entity","Categories for Value","Candidate Source"];
        for i in range(len(self.lField)):
            self.lField[i] = self.lField[i].replace(" ","")
        self.hField = dict(zip(self.lField,range(0,len(self.lField))))
        self.llValue = []
        self.concept = ""
        return    
    def Append(self,line):
        vCol = line.strip().split('\t')
        if self.concept == "":
            self.concept = vCol[0]
        else:
            if self.concept != vCol[0]:
                return False            
        self.llValue.append(line.strip().split('\t'))
        return True    
    def GetField(self,field):
        field = field.replace(" ","")
        if not field in self.hField:
            return ""
        p = self.hField[field]
        lRes = []
        for lValue in self.llValue:
            res = lValue[p]
            if (field == 'CandidateSource'):
                res = urllib.unquote(res).decode('utf8').strip('[').strip(']')
            lRes.append(res)
        return lRes    
    def GetCandidateSourceCategory(self):
        lCandCate = []
        lCandidateRawStr = self.GetField('CandidateSource')
        for CandidateRawStr in lCandidateRawStr:
            lMethodRaw = CandidateRawStr.split(',+')
            for MethodRaw in lMethodRaw:
                lCandCate.append(MethodRaw.split(':')[0])            
        return lCandCate
    
    def ConstructDespFromCPL(self):
        lCandidateRawStr = self.GetField('CandidateSource')
        desp = ""
#         print "start making desp for [%s]" %(self.concept)
        for CandidateRawStr in lCandidateRawStr:
#             print "In Candidate str [%s]" %(CandidateRawStr)
            lMethodRaw = CandidateRawStr.split(',+')
#             print "split to: [%s]" %(json.dumps(lMethodRaw))
            for MethodRaw in lMethodRaw:
                vCol = MethodRaw.split(':')
#                 print "method :[%s]" %(vCol[0])
                if 'CPL' in vCol[0]:
#                     print "is CPL :[%s]" %(' '.join(vCol[1:]))
#                     print "clean to [%s]" %(self.CleanDespStrCPL(' '.join(vCol[1:])))
                    desp += self.CleanDespStrCPL(' '.join(vCol[1:])) + ' '
        return desp.strip()
    
    def OutTrecWeb(self):
        TrecWebStr = ""
        DocNo = self.concept.replace(":","-")
        TrecWebStr += self.MakeTrecWebHead(DocNo)
        for lValue in self.llValue:
            TrecWebStr += self.MakeOneField(lValue)
        TrecWebStr +="<description>"
        mid = ""
        try:
            mid = "%s" %(self.ConstructDespFromCPL())
            TrecWebStr += mid 
        except UnicodeDecodeError:
            mid = ""
            TrecWebStr += mid    
        TrecWebStr += "</description>"
        TrecWebStr += self.MakeTrecWebTail()
        return TrecWebStr
    
    def MakeOneField(self,lValue):        
        if len(lValue) != len(self.lField):
            print "value col [%d] != field col [%d]" %(len(lValue),len(self.lField))
            return ""
        res = "<relation>\n"
        for i in range(len(lValue)):
            res += "<%s>%s</%s>\n" %(self.lField[i],lValue[i],self.lField[i])
        res += "</relation>\n";
        return res
        
    
    def MakeTrecWebHead(self,MachineId):
        res = "<DOC>\n<DOCNO>" + MachineId + "</DOCNO>\n"
        res += "<DOCHDR>\nhttp://fakeurl.com/" + MachineId + "\n</DOCHDR>\n"  
    #     res += "<MachineId>\nMachineId" + Mid + "\n</MachineId>"  
        return res 

    def MakeTrecWebTail(self):
        return '</DOC>\n'  
    
    
    def CleanDespStrCPL(self,DespStr):
        vCol = DespStr.split('\t')
        res = ""
        for i in range(len(vCol)):
            if 1 == (i % 2):
                continue
            if 0 == i:
                mid = vCol[i].split('-')
                pattern = mid[len(mid) - 1]
                res += self.DiscardArg(pattern) + " "
                continue
            res += self.DiscardArg(vCol[i]) + " "
        return res.strip()
    
    def DiscardArg(self,Pattern):
        vCol = Pattern.split('+')
        res = ""
        for col in vCol:
            if "arg" in col:
                continue
            res += col + " "
        return res.strip()
        
    
    
                  
        