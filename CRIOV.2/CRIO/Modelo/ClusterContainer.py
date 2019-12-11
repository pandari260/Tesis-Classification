'''
Created on 11 dic. 2019

@author: javier
'''

class ClusterContainer(object):
    '''
    esta clase sirve para contener y brindar acceso a un conjunto de clusters
    '''


    def __init__(self, c,d):
        '''
        un clusterContainer contiene un conjunto de clusters y una dimension
        '''
        self.__clusters = set(c)
        self.__dimension = d
    
    def getClusters(self):
        return self.__clusters
    
    def dimension(self):
        return len(self.__clusters)