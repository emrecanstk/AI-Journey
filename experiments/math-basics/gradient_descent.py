# Tiny gradient-descent story.
# prediction = 2 * weight, target = 10, loss = (prediction - target) ** 2

weight = 2.5
target = 10
lr = 0.05

print("start weight:", weight)

for step in range(8):
    prediction = 2 * weight
    loss = (prediction - target) ** 2
    # d(loss)/d(weight) for (2w - 10)^2 is 2 * (2w - 10) * 2 = 8w - 40
    gradient = 8 * weight - 40
    weight = weight - lr * gradient
    print(
        f"step {step + 1}: pred={prediction:.2f} loss={loss:.2f} "
        f"grad={gradient:.2f} weight={weight:.2f}"
    )
