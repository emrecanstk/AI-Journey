import numpy as np

labels = ["sat", "sleeping", "running", "blue"]


def softmax(logits):
    exp_values = np.exp(logits)
    probabilities = exp_values / exp_values.sum()
    return probabilities


def show(title, logits):
    probabilities = softmax(logits)
    print(title)
    print("logits:", logits)
    for label, p in zip(labels, probabilities):
        print(f"  {label:8} {p:.4f}")
    print("Total:", probabilities.sum())
    print()


show("=== logits 7.2, 6.4, 3.1, 1.2 ===", np.array([7.2, 6.4, 3.1, 1.2]))
show("=== first logit raised to 10.0 ===", np.array([10.0, 6.4, 3.1, 1.2]))
