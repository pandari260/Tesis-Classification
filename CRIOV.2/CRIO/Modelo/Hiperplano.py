'''
Created on 19 dic. 2019

@author: javier
'''

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