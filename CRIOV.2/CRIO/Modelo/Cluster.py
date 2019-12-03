'''
Created on 3 dic. 2019

@author: javier
'''

class Cluster(object):
    '''
    esta clase representa un cluster para el metodo CRIO
    '''


    def __init__(self, s):
        '''
        un cluster contiene un conjunto de muestras
        '''
        self.__samples = s
    
    def getSamples(self):
        return self.__samples
    