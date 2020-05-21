import random as rand


class Perceptron:

    _weights = []
    size = 2
    learning_rate = 0.1

    def __init__(self):
        self._weights = [rand.randint(-1, 1) for k in range(self.size)]

    def guess(self, inputs):
        _sum = 0
        for w in self._weights:
            idx = self._weights.index(w)
            _sum += inputs[idx] * w

        return self.sign(_sum)

    def sign(self, value):
        if value >= 0:
            return 1
        return -1

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        for w in self._weights:
            idx = self._weights.index(w)
            w += error * inputs[idx] * self.learning_rate
