from perceptron import Perceptron
import random
import matplotlib.pyplot as plt

# This code will try to predict with Perceptron
# if a number a number is under or above the line

raw = [
    [random.randint(-100, 100), random.randint(-100, 100)] for i in range(1000)
]
train = []
for value in raw:
    if value[1] > 0:
        train.append([value, 1])
    else:
        train.append([value, -1])

p = Perceptron()
print(p.guess([-3, 100]))

for row in train:
    p.train(row[0], row[1])


test = [
    [random.randint(-100, 100), random.randint(-100, 100)] for i in range(1000)
]
ok = 0
plotted = []
colors = []
for t in test:

    label = 1 if t[1] > 0 else -1
    guessing = p.guess(t)
    if guessing == label:
        colors.append('#c242f5')
    else:
        colors.append('#000000')

    plotted.append(t)

xs = [p[0] for p in plotted]
ys = [p[1] for p in plotted]
cs = [p for p in colors]
plt.scatter(xs, ys, s=10, c=cs)
plt.show()
