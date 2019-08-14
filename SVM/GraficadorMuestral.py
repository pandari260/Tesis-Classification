import numpy as np
import matplotlib.pyplot as plt

class GraficadorMuestral:

    @staticmethod
    def graficarBidimensional( x, y):        
        plt.plot(x, y, 'x')
        plt.axis('equal')
        plt.show()