'''
Created on 17 dic. 2019

@author: javier
'''

class GroupContainer(object):
    '''
    Clase que da acceso a un conjunto de grupos de muestras
    '''


    def __init__(self, g,d):
        '''
        Un GroupContainer contiene un conjunto de grupos de muestras y la dimension de dichas muestras
        '''
        self.__goups = set(g)
        self.__dimension =d