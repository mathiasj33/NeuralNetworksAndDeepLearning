from network import Network
import numpy as np

if __name__ == '__main__':
    net = Network([2, 2, 1])
    xs = [np.array([0, 0]).reshape((2, 1)), np.array([0, 1]).reshape(2, 1), np.array([1, 0]).reshape(2, 1),
          np.array([1, 1]).reshape(2, 1)]
    ys = [0, 1, 1, 0]
    net.SGD(zip(xs, ys), 1000, 4, 10, zip(xs, ys))
    print net.feedforward(
        xs[0])  # note that the evaluation method is not correct for XOR and therefore prints wrong results
    print net.feedforward(xs[1])
    print net.feedforward(xs[2])
    print net.feedforward(xs[3])
