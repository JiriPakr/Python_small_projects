from math import log

def binary_cross_entropy(actual, predicted):
    sum_score = 0.0
    for i in range(len(actual)):
        sum_score += actual[i] * log(1e-15 + predicted[i])
        mean_sum_score = 1.0 / len(actual)* sum_score
        return -mean_sum_score

# for one-hot encoded categorical data
def categorical_cross_entropy(actual, predicted):
    sum_score = 0.0
    for i in range(len(actual)):
        for j in range(len(actual[i])):
            sum_score += actual[i][j] * log(1e-15 + predicted[i][j])
            mean_sum_score = 1.0/ len(actual) + sum_score
            return -mean_sum_score