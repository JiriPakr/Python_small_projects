import numpy as np
import pandas as pd

from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression 

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

data= pd.read_csv("train.csv", sep = ';')
if 'fnlwgt' in data: #not used metric
    data.pop('fnlwgt')
#X = data[['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status','occupation','relationship','race','sex','capital-gain','capital-gain',
#'capital-loss','hours-per-week','native-country']].values
#y = data['income'].values

income_raw = data['income']
features_raw = data.drop('income', axis = 1)

skewed= ['capital-gain', 'capital-loss']
features_log_transformed= pd.DataFrame(data=features_raw)
features_log_transformed[skewed]= features_raw[skewed].apply(lambda x: np.log(x+1))

scaler =MinMaxScaler()               #default=0,1
numerical= ['age','education-num','capital-gain','capital-loss','hours-per-week']

features_log_minmax_transform = pd.DataFrame(data = features_log_transformed)
features_log_minmax_transform[numerical] = scaler.fit_transform(features_log_transformed[numerical])

#print(features_log_minmax_transform.head(n=3))

features_final = pd.get_dummies(features_log_minmax_transform)

income = income_raw.map({'<=50K':0,'>50K':1})

encoded = list(features_final.columns)
dummies = features_final.columns

X_train, X_test, y_train, y_test = train_test_split(features_final,income,test_size = 0.1) 
#print("Training set has {} samples.".format(X_train.shape[0]))
#print("Testing set has {} samples.".format(X_test.shape[0]))

model = KNeighborsClassifier(n_neighbors=5, metric= 'euclidean')
#model.fit(X_train, y_train)

#y_pred1 = model.predict(X_test)

#cm1 = confusion_matrix(y_test,y_pred1)
#print(cm1)


#y_pred = model.predict(X)
#score = (y == y_pred).sum() / y.shape[0]
#print(score)

#--------------------------------------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()                       # inicializace predka
        self.setWindowTitle('Classification')
        self.setMinimumSize(QSize(800,600))
        self.content = QWidget()
        layout = QGridLayout()


        self.a_input = QLineEdit('1')
        self.b_input = QLineEdit('2')
        self.c_input = QLineEdit('3')

        layout.addWidget(self.a_input, 0, 1)

        self.setCentralWidget(self.content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()