print("=== squared error ===")
prediction = 6
target = 10
loss = (prediction - target) ** 2
print(loss)

print("\n=== change the weight ===")
target = 10
for weight in [0.5, 1.0, 1.5, 2.0, 2.5]:
    prediction = 2 * weight
    loss = (prediction - target) ** 2
    print(
        "weight:",
        weight,
        "prediction:",
        prediction,
        "loss:",
        loss
    )
