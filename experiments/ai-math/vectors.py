import numpy as np


print("=== vector ===")
a = np.array([1.0, 0.0])
b = np.array([0.0, 1.0])
print("a:", a)
print("b:", b)


print("\n=== matrix ===")
Q = np.array([
    [1.0, 0.0],
    [0.0, 1.0],
])
K = np.array([
    [1.0, 0.0],
    [0.0, 1.0],
])
print("Q:\n", Q)
print("K:\n", K)


print("\n=== dot product of two vectors ===")
dot_ab = float(np.dot(a, b))
print("a · b =", dot_ab)
print("same direction would be closer to 1 after normalize; these are orthogonal so 0")


print("\n=== matrix multiply is many dot products ===")
scores = Q @ K.T
print("Q @ K.T =\n", scores)
print("This is yesterday's attention scores step.")


print("\n=== same idea as cosine, without the divide-by-length yet ===")
u = np.array([0.2, 0.4, 0.8])
v = np.array([0.3, 0.5, 0.7])
print("u · v =", float(np.dot(u, v)))
print("cosine =", float(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))))
