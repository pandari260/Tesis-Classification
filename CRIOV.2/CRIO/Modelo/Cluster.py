'''
Created on 3 dic. 2019

@author: javier
'''
from CRIO.Modelo.SampleContainer import SampleContainer

class Cluster(SampleContainer):
    '''
    esta clase representa un cluster para el metodo CRIO
    '''
    

#toma dos clusters y los fusiona. Los clusters deben tener el mismo valor de dimension
def mergeClusters(clusterA,clusterB):
    return Cluster(clusterA.getSamples() | clusterB.getSamples(), clusterA.getDimension())

