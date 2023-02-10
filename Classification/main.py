import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier



data= pd.read_csv("train.csv", sep = ';')

#print(data.head(n=30))


# Split the data into features and target label
income_raw = data['income']
features_raw = data.drop('income', axis = 1)

skewed= ['capital-gain', 'capital-loss']
features_log_transformed= pd.DataFrame(data=features_raw)
features_log_transformed[skewed]= features_raw[skewed].apply(lambda x: np.log(x+1))

#initialize a scaler, then apply it to the features
#prevents large impact of bigger numbers
scaler =MinMaxScaler()               #default=0,1
numerical= ['age','education-num','capital-gain','capital-loss','hours-per-week']

features_log_minmax_transform = pd.DataFrame(data = features_log_transformed)
features_log_minmax_transform[numerical] = scaler.fit_transform(features_log_transformed[numerical])

#Show an example of a record with scalling applied 
#print(features_log_minmax_transform.head(n=3))

# Preprocessing categorical features 
# creates category for each type of cat. feature
features_final = pd.get_dummies(features_log_minmax_transform)

# Encode the 'income_raw' data to numerical values
income = income_raw.map({'<=50K':0,'>50K':1})

# Print the number of features after one-hot encoding
encoded = list(features_final.columns)
dummies = features_final.columns
print("{} total features after one-hot encoding.".format(len(encoded)))

#Spite the 'features' and 'income' data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(features_final,income,test_size = 0.1) 

#Show the results of the split 
print("Training set has {} samples.".format(X_train.shape[0]))
print("Testing set has {} samples.".format(X_test.shape[0]))

#y_pred1 = model.predict(X_test)

#cm1 = confusion_matrix(y_test,y_pred1)
#print(cm1)

#-----------------------------------

m, n = X_train.shape

def init_params():
    W1 = np.random.randn(108,10) - 0.5
    b1 = np.random.randn(10, 1) - 0.5
    W2 = np.random.randn(108,10) - 0.5
    b2 = np.random.randn(10, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(0, Z)

def softmax(Z):
    return np.exp(Z) / np.sum(np.exp(Z))

def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arrange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def ReLU_deriv(Z):
    return Z > 0

def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
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
    print(predicitons, Y)
    return np.sum(predicitons == Y) / Y.size

def gradient_descent(X, Y, alpha, iterations):
    W1, b1, W2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 10 == 0:
            print("Iteration: ", i)
            predictions = get_predictions(A2)
            print(get_accuracy(predictions, Y))
    return W1, b1, W2, b2
#---------------------------------

#plt.scatter(data['age'], data['education-num'])
W1, b1, W2, b2 = gradient_descent(X_train, y_train, 0.1, 500)


# data = np.array(data)
# m, n = data.shape
# np.random.shuffle(data)

# data_dev = data[0:1000].T
# Y_dev = data_dev[0]
# X_dev = data_dev[1:n]

# data_train = data[0:1000]
# Y_train = data_dev[0]
# X_train = data_dev[1:n]



#print(X_train)