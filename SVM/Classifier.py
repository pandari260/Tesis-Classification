from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#Svm clasifica el dataSet basado en el kernel que se definine, de manera supervisada en el target.
def classify(kernel, dataSet, target):
    sorter = SVC(C=1, degree=3, gamma='scale', kernel=kernel)
    X_train, X_test, Y_train, Y_test = train_test_split(dataSet, target, test_size = 0.22)
    sorter.fit(X_train, Y_train)
    return sorter.predict(X_test), Y_test

