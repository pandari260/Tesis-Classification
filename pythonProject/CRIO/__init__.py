
from CRIO.Classifier import Classifier
from CRIO.Exporter import writeSolution

def main():
    classifier = Classifier("model/class0.dat","model/class1.dat",2,2,"azul", "rojo")
    
    classifier.printRegions()
    writeSolution(classifier.regions, "model/solution")
    
    print("la muestra " + str((8,4)) +  " es de color: " +  str(classifier.classify((8,4))))
    print("la muestra " + str((2,4)) +  " es de color: " +  str(classifier.classify((2,4))))
    print("la muestra " + str((4,8)) +  " es de color: " +  str(classifier.classify((4,8))))
    print("la muestra " + str((4,2)) +  " es de color: " +  str(classifier.classify((4,2))))

    
    

main()