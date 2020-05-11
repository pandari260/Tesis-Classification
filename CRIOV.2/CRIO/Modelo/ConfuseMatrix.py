import Sample

def __rowConfuseMatrix(clasifier, sample, color):
    r1, r2 = 0, 0
    for i in sample:  
        if(clasifier.classify(Sample.Sample(i)).__eq__(color)):  r1+=1 
        else: r2+=1
    return r1, r2
    
def generateConfuseMatrix(clasifier, sampleC0, sampleC1, t0, t1):
    TP, FP = __rowConfuseMatrix(clasifier, sampleC0, t0)
    TN, FN = __rowConfuseMatrix(clasifier, sampleC1, t1)  
    return float(TP), float(FP), float(TN), float(FN)