import random as rand


class Perceptron:

    size = 2
    learning_rate = 0.1
    _weights = [rand.randint(-1, 1) for k in range(size)]

    def __init__(self):
        pass

    def guess(self, inputs):
        self.size = len(inputs)

        _sum = 0
        for w in range(len(self._weights)):
            _sum += inputs[w] * self._weights[w]

        return self.sign(_sum)

    def sign(self, value):
        if value >= 0:
            return 1
        return -1

    def train(self, inputs, target):
        self.size = len(inputs)

        guess = self.guess(inputs)
        error = target - guess

        for w in range(len(self._weights)):
            self._weights[w] += error * inputs[w] * self.learning_rate
