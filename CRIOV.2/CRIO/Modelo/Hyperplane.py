'''
Created on 19 dic. 2019

@author: javier
'''
from pyscipopt import Model, quicksum

class Hyperplane(object):
    '''
    Esta clase representa a un hiperplano para el metodo CRIO
    '''


    def __init__(self, q,o):
        '''
        un hiperplano contiene una tupla de coheficientes y una ordenada al origen
        '''
        self.__coefficients = q
        self.__intercept =  o
    
    def __eq__(self,obj):
        return isinstance(Hyperplane) and all(abs(self.__coefficients(index) - obj.getHyperplanes().getCoefficient(index)) <= 0.0000000001 for index in range(0,self.getDimension())) and abs(self.__intercept - obj.getIntercept()) <= 0.000000001
    
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
        xVars = {}
        for i in range(dimension):
            xVars[i] = model.addVar(vtype="CONTINUOUS", name="x[%s]" %(i),lb=None)        
        
        print self
        for hiperplane in region.getHyperplanes().difference(set([self])):
            print hiperplane
            model.addCons(quicksum(hiperplane.getCoefficient(f)*xVars[f] for f in range(dimension)) <= hiperplane.getIntercept(),"r1%s" % (hiperplane))
        
        model.addCons(quicksum(self.getCoefficient(f)*xVars[f] for f in range(dimension)) <= self.getIntercept() + 1.0,"prevent_unbound")
        
        model.setObjective(quicksum(self.getCoefficient(f)*xVars[f] for f in range(dimension)), sense="maximize")  
        model.optimize()
        
        return model.getObjVal() <= self.getIntercept()      

