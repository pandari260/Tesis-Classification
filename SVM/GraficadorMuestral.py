import numpy as np
import matplotlib.pyplot as plt

class GraficadorMuestral:

    @staticmethod
    def graficarUnidimensional(s, mu, sigma):
        count, bins, ignored = plt.hist(s, 30, density=True)
        plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
                linewidth=2, color='r')
        plt.show()
        
    @staticmethod
    def graficarBidimensional( x, y):        
        plt.plot(x, y, 'x')
        plt.axis('equal')
        plt.show()