import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

data_path = "./data/"

NUM_INPUT = 784  # Number of input neurons
NUM_HIDDEN = 40  # Number of hidden neurons
NUM_OUTPUT = 10  # Number of output neurons
NUM_CHECK = 5  # Number of examples on which to check the gradient

# Given a vector w containing all the weights and biased vectors, extract
# and return the individual weights and biases W1, b1, W2, b2.
# This is useful for performing a gradient check with check_grad.
def unpack (w):
    return W1, b1, W2, b2

# Given individual weights and biases W1, b1, W2, b2, concatenate them and
# return a vector w containing all of them.
# This is useful for performing a gradient check with check_grad.
def pack (W1, b1, W2, b2):
    pass

# Load the images and labels from a specified dataset (train or test).
def loadData (which):
    images = np.load("{}mnist_{}_images.npy".format(data_path,which))
    labels = np.load("{}mnist_{}_labels.npy".format(data_path,which))
    return images, labels

# Given training images X, associated labels Y, and a vector of combined weights
# and bias terms w, compute and return the cross-entropy (CE) loss. You might
# want to extend this function to return multiple arguments (in which case you
# will also need to modify slightly the gradient check code below).
def fCE (X, Y, w):
    W1, b1, W2, b2 = unpack(w)
    '''
    z(1) = W(1)x + b(1)
    h(1) = relu(z(1)))
    z(2) = W(2)h(1) + b(2)
    ^y = g(x) = softmax(z(2))
    '''
    z1 = predictor(W1, X, b1)
    h1 = reLU(z1)
    z2 = predictor(W2, h1, b2)
    Yhat = np.softmax(z2)
    cost = -np.mean(np.log(Yhat[Y==1]))
    return cost

def predictor(W, x, b):
    z = W.dot(x) + b

def reLU(s):
    if s >= 0: return s
    return 0

def softmax(z):
    e_z = np.exp(z - np.max(z))
    return e_z/e_z.sum()

# Given training images X, associated labels Y, and a vector of combined weights
# and bias terms w, compute and return the gradient of fCE. You might
# want to extend this function to return multiple arguments (in which case you
# will also need to modify slightly the gradient check code below).
def gradCE (X, Y, w):
    W1, b1, W2, b2 = unpack(w)
    return grad

# Given training and testing datasets and an initial set of weights/biases b,
# train the NN. Then return the sequence of w's obtained during SGD.
def train (trainX, trainY, testX, testY, w):
    return ws

if __name__ == "__main__":
    # Load data
    if "trainX" not in globals():
        trainX, trainY = loadData("train")
        testX, testY = loadData("test")

    # Initialize weights randomly
    W1 = 2*(np.random.random(size=(NUM_INPUT, NUM_HIDDEN))/NUM_INPUT**0.5) - 1./NUM_INPUT**0.5
    b1 = 0.01 * np.ones(NUM_HIDDEN)
    W2 = 2*(np.random.random(size=(NUM_HIDDEN, NUM_OUTPUT))/NUM_HIDDEN**0.5) - 1./NUM_HIDDEN**0.5
    b2 = 0.01 * np.ones(NUM_OUTPUT)
    w = pack(W1, b1, W2, b2)

    # Check that the gradient is correct on just a few examples (randomly drawn).
    idxs = np.random.permutation(trainX.shape[0])[0:NUM_CHECK]
    print(scipy.optimize.check_grad(lambda w_: fCE(np.atleast_2d(trainX[idxs,:]), np.atleast_2d(trainY[idxs,:]), w_), \
                                    lambda w_: gradCE(np.atleast_2d(trainX[idxs,:]), np.atleast_2d(trainY[idxs,:]), w_), \
                                    w))

    # Train the network and obtain the sequence of w's obtained using SGD.
    ws = train(trainX, trainY, testX, testY, w)
