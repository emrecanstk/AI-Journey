import math

import torch
import torch.nn.functional as F


print("=== 9.1 residual connection ===")
x = torch.tensor([1.0, 2.0, 3.0])
transformed = torch.tensor([0.5, -0.2, 0.1])
output = x + transformed
print("input:", x.tolist())
print("transformation(input):", transformed.tolist())
print("output = input + transformation(input):", output.tolist())


print("\n=== 9.2 tiny feed forward ===")
x = torch.tensor([1.0, -2.0, 0.5])
W1 = torch.tensor([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.5, 0.5, 0.0],
])
b1 = torch.zeros(4)
hidden = torch.relu(x @ W1.T + b1)
W2 = torch.tensor([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
])
b2 = torch.zeros(3)
ffn_out = hidden @ W2.T + b2
print("x:", x.tolist())
print("after Linear + ReLU:", hidden.tolist())
print("after second Linear:", ffn_out.tolist())


print("\n=== 10 next-token logits ===")
labels = ["mat", "floor", "chair", "table"]
logits = torch.tensor([2.1, 1.4, 0.4, -0.3])


def probs_at_temperature(logits, temperature):
    scaled = logits / temperature
    return F.softmax(scaled, dim=-1)


print("logits:", {k: round(v, 3) for k, v in zip(labels, logits.tolist())})

for t in [0.5, 1.0, 2.0]:
    probs = probs_at_temperature(logits, t)
    print(f"\ntemperature={t}")
    for label, p in zip(labels, probs.tolist()):
        print(f"  {label}: {p:.3f}")

print("\nloop: context -> Transformer -> logits -> probabilities -> next token")
print("then append token to context and repeat")
print('example context: "The cat sat on the"')
print('after picking mat: "The cat sat on the mat"')
