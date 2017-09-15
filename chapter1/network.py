import numpy as np


class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, input):
        a = input
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, lr, test_data=None):
        if test_data is not None: num_tests = len(test_data)
        num = len(training_data)
        for j in xrange(epochs):
            np.random.shuffle(training_data)



def sigmoid(z):
    return 1.0/(1.0 + np.exp(-z))