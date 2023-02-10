import numpy as np
import pandas as pd
import sys
import pathlib

from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn.neural_network import MLPClassifier

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Train data --------------------------------------

# Train data initialization
data = pd.read_csv("train.csv", sep = ';')
cur_path = pathlib.Path().resolve()
# dropping messy col
if 'fnlwgt' in data: 
    data.pop('fnlwgt')

#X = data[['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status','occupation','relationship','race','sex','capital-gain','capital-gain',
#'capital-loss','hours-per-week','native-country']]
#y = data['income']

# Spliting data, income - target, features - rest
income_raw = data['income']
features_raw = data.drop('income', axis = 1)

# Data preprocessing
scaler =MinMaxScaler()               #default=0,1
numerical= ['age','education-num','capital-gain','capital-loss','hours-per-week']
features_minmax = pd.DataFrame(data = features_raw)
features_minmax[numerical] = scaler.fit_transform(features_raw[numerical])
features_nums = pd.get_dummies(features_minmax)

# Income maping to 0 or 1
income = income_raw.map({'<=50K':0,'>50K':1})
# Dummies for matching with valid dataset
dummies = features_nums.columns

# Data spliting for training and testing
X_train, X_test, y_train, y_test = train_test_split(features_nums,income,test_size = 0.2) 
#print("Training set has {} samples.".format(X_train.shape[0]))
#print("Testing set has {} samples.".format(X_test.shape[0]))

# Valid Data --------------------------------------

# Valid data initialization
data_valid = pd.read_csv("valid_student.csv", sep = ';')
cur_path_valid = pathlib.Path().resolve()
# dropping messy col
if 'fnlwgt' in data_valid: 
    data_valid.pop('fnlwgt')

# Spliting data, income - target, features - rest
income_raw_valid = data_valid['income']
features_raw_valid = data_valid.drop('income', axis = 1)

# Data preprocessing
scaler =MinMaxScaler()               #default=0,1
numerical= ['age','education-num','capital-gain','capital-loss','hours-per-week']
features_minmax_valid = pd.DataFrame(data = features_raw_valid)
features_minmax_valid[numerical] = scaler.fit_transform(features_raw_valid[numerical])
features_nums_valid = pd.get_dummies(features_minmax_valid)
# resizing to match train data
features_nums_valid= features_nums_valid.reindex(columns = dummies, fill_value = 0)

# Income maping to 0 or 1
income_valid = income_raw_valid.map({'<=50K':0,'>50K':1})

# renaming
X_valid, y_valid = features_nums_valid , income_valid 

#-------------------------------------------------------------------------------------*
# NN Classifer - used only numpy 

def init_params():
    W1 = np.random.randn(2,107) - 0.5
    b1 = np.random.randn(2, 1) - 0.5
    W2 = np.random.randn(2,2) - 0.5
    b2 = np.random.randn(2, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(Z, 0)

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A

def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def ReLU_deriv(Z):
    return Z > 0

def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    m = Y.size
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, aplha):
    W1 = W1 - aplha * dW1
    b1 = b1 - aplha *db1
    W2 = W2 - aplha * dW2
    b2 = b2 - aplha *db2
    return W1, b1, W2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predicitons, Y):
    #print(predicitons, Y)
    return np.sum(predicitons == Y) / Y.size

def gradient_descent(X, Y, iterations, aplha):
    W1, b1, W2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)                  # 
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, aplha)
        if i % 50 == 0:
            print("Iteration: ", i)
        #    print("Accuracy: ", get_accuracy(get_predictions(A2), Y))
        acurracy = get_accuracy(get_predictions(A2), Y)
    return W1, b1, W2, b2, acurracy

def make_predictions(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    return predictions

    #X_train_T = X_train.T
    #W1, b1, W2, b2, acurracy= gradient_descent(X_train_T.values, y_train.values, 5000, 0.1)


#-------------------------------------------------------------------------------------*
# GUI - PyQT5

def train():
    if window.case == "MLP_LIB":
        global model
        window.text.setText("Working...")
        window.path.setText("Train file:\n" + cur_path.__str__() + "\\train.csv")
        window.text.repaint()
        model = MLPClassifier(max_iter=5000)
        model.fit(X_train, y_train)
        y_pred1 = model.predict(X_test)
        cm1 = confusion_matrix(y_test,y_pred1)
        TP = int(cm1[0,0])
        FP = int(cm1[1,0])
        FN = int(cm1[0,1])
        TN = int(cm1[1,1])
        accuracy = (TP + TN)/ (TP + FP + TN + FN)
        window.text.setText("Binary accuracy:" + accuracy.__str__())
        window.set_trained_true()

    if window.case == "MLP_WRITTEN":
        global test_predictions
        window.text.setText("Working...")
        window.path.setText("Train file:\n" + cur_path.__str__() + "\\train.csv")
        window.text.repaint()
        X_train_T = X_train.T
        W1, b1, W2, b2, acurracy  = gradient_descent(X_train_T.values, y_train.values, 5000, 0.1)
        window.text.setText("Binary accuracy:" + acurracy.__str__())
        X_valid_T = X_valid.T                                                          
        test_predictions = make_predictions(X_valid_T.values, W1, b1, W2, b2)
        window.set_trained_true()

def test():
    if window.trained == True:

        if window.case == "MLP_LIB":
            window.text.setText("Working...")
            window.path.setText("Test file:\n" + cur_path_valid.__str__() + "\\valid.csv")
            window.text.repaint()
            #model = MLPClassifier()
            y_pred = model.predict(X_valid)
            cm2 = confusion_matrix(y_valid,y_pred)
            TP_2 = int(cm2[0,0])
            FP_2 = int(cm2[1,0])
            FN_2 = int(cm2[0,1])
            TN_2 = int(cm2[1,1])
            accuracy_valid = (TP_2 + TN_2)/ (TP_2 + FP_2 + TN_2 + FN_2)
            window.text.setText("Test binary accuracy:" + accuracy_valid.__str__() + "\n\nExample predictions:\n" + y_pred[5000:6000].__str__())

        if window.case == "MLP_WRITTEN":
            window.text.setText("Working...")
            window.path.setText("Test file:\n" + cur_path_valid.__str__() + "\\valid.csv")
            window.text.repaint()
            acurracy_test = get_accuracy(test_predictions, y_valid.values)
            window.text.setText("Test binary accuracy:" + acurracy_test.__str__() + "\n\nExample predictions:\n" + test_predictions[5000:6000].__str__())
            
    if window.trained == False:
        window.text.setText("Please train first")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()                       # inicializace predka
        self.setWindowTitle('Classification')
        self.setMinimumSize(QSize(800,600))
        self.content = QWidget()
        layout = QGridLayout()

        # Buttons
        self.trainbtn = QPushButton('Train')
        self.trainbtn.clicked.connect(train)
        self.testbtn = QPushButton('Test')
        self.testbtn.clicked.connect(test)
        self.path = QTextBrowser(self.content)
        self.path.setText("File directory:\n" + cur_path.__str__())
        self.text = QTextBrowser(self.content)
        self.text.setText("Income classification, classes '<=50K':0,'>50K':1\n\
Based on age, workclass, education, education count, marital status, occupation, relationship,\nrace, sex, capital gain, capital loss, hours per week, native country\n\n\
Classifier choices:\nMLP_LIB - sklearn.neural_network - MLPClassifier - 5k iterations\n\
MLP_WRITTEN - NN classifier written using only Numpy - 5k iterations\n\nIf binary accuracy <= 76% please retrain")
        self.mlp_lib = QCheckBox('MLP_LIB')
        self.mlp_lib.setChecked(True)
        self.mlp_lib.toggled.connect(self.mlp_lib_toggle)
        self.mlp_written = QCheckBox('MLP_WRITTEN')
        self.mlp_written.toggled.connect(self.mlp_written_toggle)
        
        self.set_trained_false()
        self.set_case_mlp_lib()  

        ## Side labels
        #layout.addWidget(QLabel('a'), 0, 0)
        #layout.addWidget(QLabel('b'), 1, 0)
        #layout.addWidget(QLabel('c'), 3, 0)
        #layout.addWidget(QLabel('d'), 4, 0)

        # Layout main widgets
        layout.addWidget(self.trainbtn, 0, 1)
        layout.addWidget(self.testbtn, 1, 1)
        layout.addWidget(self.text, 2, 1)
        layout.addWidget(self.path, 3, 1)
        layout.addWidget(self.mlp_lib, 0, 0)
        layout.addWidget(self.mlp_written, 1, 0)

        # dont delete
        self.content.setLayout(layout)
        self.setCentralWidget(self.content)

    def mlp_lib_toggle(self):
        if self.mlp_lib.isChecked() == True:
            self.set_case_mlp_lib()
            self.set_trained_false()
            self.text.setText("Income classification, classes '<=50K':0,'>50K':1\n\
Based on age, workclass, education, education count, marital status, occupation, relationship,\nrace, sex, capital gain, capital loss, hours per week, native country\n\n\
Classifier choices:\nMLP_LIB - sklearn.neural_network - MLPClassifier - 5k iterations\n\
MLP_WRITTEN - NN classifier written using only Numpy - 5k iterations\n\nIf binary accuracy <= 76% please retrain")
            self.path.setText("File directory:\n" + cur_path.__str__())
            self.mlp_written.setChecked(False)

    def mlp_written_toggle(self):
        if self.mlp_written.isChecked() == True:
            self.set_case_mlp_written()
            self.set_trained_false()
            self.text.setText("Income classification, classes '<=50K':0,'>50K':1\n\
Based on age, workclass, education, education count, marital status, occupation, relationship,\nrace, sex, capital gain, capital loss, hours per week, native country\n\n\
Classifier choices:\nMLP_LIB - sklearn.neural_network - MLPClassifier - 5k iterations\n\
MLP_WRITTEN - NN classifier written using only Numpy - 5k iterations\n\nIf binary accuracy <= 76% please retrain")
            self.path.setText("File directory:\n" + cur_path.__str__())
            self.mlp_lib.setChecked(False)

    def set_trained_false(self):
        self.trained = False

    def set_trained_true(self):
        self.trained = True
    
    def set_case_mlp_lib(self):
        self.case = "MLP_LIB"

    def set_case_mlp_written(self):
        self.case = "MLP_WRITTEN"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


    

