# Hill Climbing Algorithm with Manual Step Size

def f(x):
    return -(x**2) + 5

# User inputs
x = float(input("Enter the starting value: "))
step = float(input("Enter the step size: "))

print("Step by step movement")

while True:
    print("Current x =", x, " f(x) =", f(x))

    left = x - step
    right = x + step

    if f(left) > f(x):
        x = left
    elif f(right) > f(x):
        x = right
    else:
        break

print("\nOptimal solution found!")
print("Best x =", x)
print("Maximum value f(x) =", f(x))