from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import ManipuladorMuestral as manipulador
import Impresora as impresora


def clasificar(kernel, archivo):
    clasificador = SVC(C=1, degree=3, gamma='scale', kernel=kernel)
    datos, target = manipulador.obtenerMuestraSVM(archivo)
    X_train, X_test, Y_train, Y_test = train_test_split(datos, target, test_size = 0.22)
    clasificador.fit(X_train, Y_train)
    y_pred = clasificador.predict(X_test)
    impresora.imprimirOutSVM(Y_test, y_pred)

   