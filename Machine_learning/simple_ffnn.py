import numpy as np

# sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# derivative of sigmoid activation function
def sigmoid_derivative(x):
    return x * (1 - x)

# input dataset
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# output dataset
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation deterministic
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1

for i in range(10000):

    # forward propagation
    l0 = X
    l1 = sigmoid(np.dot(l0, syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * sigmoid_derivative(l1)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l1)
