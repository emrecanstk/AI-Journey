import math


def relu(x):
    return max(0, x)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


print("=== 2.1 Single neuron ===")
x1 = 2
x2 = 3
w1 = 0.5
w2 = 0.8
bias = 0.1
output = (x1 * w1) + (x2 * w2) + bias
print(output)


print("\n=== 2.3 ReLU on the same z ===")
z = (x1 * w1) + (x2 * w2) + bias
output = relu(z)
print("z:", z)
print("relu(z):", output)


print("\n=== 2.3 ReLU when z is negative (bias = -5) ===")
bias_neg = -5
z_neg = (x1 * w1) + (x2 * w2) + bias_neg
print("z:", z_neg)
print("relu(z):", relu(z_neg))


print("\n=== 2.4 Sigmoid ===")
print("sigmoid(-10):", sigmoid(-10))
print("sigmoid(0):", sigmoid(0))
print("sigmoid(10):", sigmoid(10))


print("\n=== Two neurons / one hidden layer ===")
w11 = 0.5
w12 = 0.8
b1 = 0.1
z1 = x1 * w11 + x2 * w12 + b1
h1 = relu(z1)

w21 = -0.3
w22 = 0.4
b2 = 0.2
z2 = x1 * w21 + x2 * w22 + b2
h2 = relu(z2)

print("Neuron 1:", h1)
print("Neuron 2:", h2)
