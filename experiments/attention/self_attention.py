import math

import torch


def self_attention(Q, K, V):
    d_k = K.shape[-1]
    scores = Q @ K.T
    scores = scores / math.sqrt(d_k)
    weights = torch.softmax(scores, dim=-1)
    output = weights @ V
    return output, weights, scores


def show(title, Q, K, V):
    print(f"=== {title} ===")
    print("Q:")
    print(Q)
    raw_scores = Q @ K.T
    print("\nScores (Q @ K.T):")
    print(raw_scores)
    d_k = K.shape[-1]
    scaled = raw_scores / math.sqrt(d_k)
    print("\nScaled scores:")
    print(scaled)
    output, weights, _ = self_attention(Q, K, V)
    print("\nAttention weights:")
    print(weights)
    print("\nOutput:")
    print(output)
    print()


K = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0],
])

V = torch.tensor([
    [10.0, 0.0],
    [0.0, 20.0],
])

Q_identity = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0],
])

Q_tilted = torch.tensor([
    [0.9, 0.1],
    [0.1, 0.9],
])

Q_mixed = torch.tensor([
    [0.5, 0.5],
    [0.5, 0.5],
])

show("original Q (each token looks at itself)", Q_identity, K, V)
show("tilted Q [0.9, 0.1] / [0.1, 0.9]", Q_tilted, K, V)
show("mixed Q [0.5, 0.5] both rows", Q_mixed, K, V)
