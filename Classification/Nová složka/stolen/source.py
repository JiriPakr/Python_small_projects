import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier



# input data as csv should have 1st row with names of features
# separated by ;
# no spaces
# training data file is train.csv
# test data file is valid.csv
# check data for incosistency, possibly dots randomly at end of row, this will cause error
def train(path = "train.csv"):
    global dummies
    data= pd.read_csv(path, sep = ';')
    if 'fnlwgt' in data: #not used metric
        data.pop('fnlwgt')
    #Success- Display the the first ten records 
    print(data.head(n=3))

    #data preparation
    # Total number of records
    n_records = data.shape[0]
    # Number of records where individual's income is more than $50,000
    n_greater_50k = data[data['income'] == '>50K'].shape[0]
    # Number of records where individual's income is at most $50,000
    n_at_most_50k = data[data['income'] == '<=50K'].shape[0]
    # Percentage of individuals whose income is more than $50,000
    greater_percent =  round(((n_greater_50k /  n_records) * 100),3)

    # Print the results
    print("Total number of records: {}".format(n_records))
    print("Individuals making more than $50,000: {}".format(n_greater_50k))
    print("Individuals making at most $50,000: {}".format(n_at_most_50k))
    print("Percentage of individuals making more than $50,000: {}%".format(greater_percent))


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
    print(features_log_minmax_transform.head(n=3))

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


    #Fitting Classifier to the Training Set 
    classifier= KNeighborsClassifier(n_neighbors=5, metric= 'euclidean')
    classifier.fit(X_train, y_train)

    #Predicting the Test Set Result 
    y_pred1 = classifier.predict(X_test)

    #Making the Confusion Matrix 
    cm1 = confusion_matrix(y_test,y_pred1)
    print(cm1)

    # Specific to the figures
    TP = int(cm1[0,0])
    FP = int(cm1[1,0])
    FN = int(cm1[0,1])
    TN = int(cm1[1,1])


    # Calculate accuracy, precision and recall
    accuracy = (TP + TN)/ (TP + FP + TN + FN)
    return classifier, accuracy

def test(classifier, path = "valid.csv"):
    data= pd.read_csv(path, sep = ';')
    if 'fnlwgt' in data:
        data.pop('fnlwgt')
    #Success- Display the the first ten records 
    print(data.head(n=3))

    # Split the data into features and target label
    income_raw = data['income']
    features_raw = data.drop('income', axis = 1)

    #log- transform the skewed features 
    skewed= ['capital-gain', 'capital-loss']
    features_log_transformed= pd.DataFrame(data=features_raw)
    features_log_transformed[skewed]= features_raw[skewed].apply(lambda x: np.log(x+1))

    #initialize a scaler, then apply it to the features
    scaler =MinMaxScaler()               #default=0,1
    numerical= ['age','education-num','capital-gain','capital-loss','hours-per-week']

    features_log_minmax_transform = pd.DataFrame(data = features_log_transformed)
    features_log_minmax_transform[numerical] = scaler.fit_transform(features_log_transformed[numerical])

    #Show an example of a record with scalling applied 
    print(features_log_minmax_transform.head(n=3))

    # Preprocessing categorical features 
    # One-hot encode the 'features_log_minmax_transform' data 
    features_final = pd.get_dummies(features_log_minmax_transform)
    # reindex to number of inputs used in training
    features_final = features_final.reindex(columns = dummies, fill_value = 0)
    # Encode the 'income_raw' data to numerical values
    income = income_raw.map({'<=50K':0,'>50K':1})

    # Print the number of features after one-hot encoding
    encoded = list(features_final.columns)
    print("{} total features after one-hot encoding.".format(len(encoded)))

    X_test, y_test = features_final, income

    #Predicting the Test Set Result 
    y_pred1 = classifier.predict(X_test)

    #Making the Confusion Matrix 
    cm1 = confusion_matrix(y_test,y_pred1)
    print(cm1)


    # Specific to the figures
    TP = int(cm1[0,0])
    FP = int(cm1[1,0])
    FN = int(cm1[0,1])
    TN = int(cm1[1,1])


    # Calculate accuracy, precision and recall
    accuracy = (TP + TN)/ (TP + FP + TN + FN)
    return accuracy

