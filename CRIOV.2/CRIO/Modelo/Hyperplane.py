'''
Created on 19 dic. 2019

@author: javier
'''
from pyscipopt import Model, quicksum

class Hiperplano(object):
    '''
    Esta clase representa a un hiperplano para el metodo CRIO
    '''


    def __init__(self, q,o):
        '''
        un hiperplano contiene una tupla de coheficientes y una ordenada al origen
        '''
        self.__coefficients = q
        self.__intercept =  o
    
    def getDimension(self):
        return len(self.__coefficients)
    
    def getCoefficient(self, index):
        return self.__coefficients[index]
    
    def getIntercept(self):
        return self.__intercept
    
    #TODO: Se debe verificar que el hiperplano pertenesca a la region dada
    def isRedundant(self, region):
        
        dimension = self.getDimension()
        ############ model ##############################
        model = Model()
        for i in range(dimension):
            xVars = model.addVar(vtype="CONTINUOUS", name="x[%s]" %(i),lb=None)        
        
        
        for hiperplane in region.getHiperplanes().difference(self):
            model.addCons(quicksum(hiperplane.getCoefficient(f)*xVars(f) for f in range(dimension)) <= hiperplane.getIntercept(),"r1%s" % (hiperplane))
        
        model.addCons(quicksum(self.getCoefficient(f)*xVars[f] for f in range(dimension)) <= self.getIntercept() + 1,"prevent unbound")
        
        model.setObjective(quicksum(self.getCoefficient(f)*xVars[f] for f in range(dimension)), sense="maximize")  
        model.optimize()
        
        return model.getObjVal() <= self.getIntercept()      

