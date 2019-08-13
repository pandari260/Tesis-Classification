import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


bankdata = pd.read_csv("input/input.csv")

bankdata.shape
bankdata.head()

X = bankdata.drop('Class', axis=1)
y = bankdata['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.7)

svclassifier = SVC(kernel='rbf')
svclassifier.fit(X_train, y_train)

print(svclassifier.score(X_test, y_test))
y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

