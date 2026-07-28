from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()

# Display column names
print("Feature Names:")
print(iris.feature_names)

print("\nTarget Names:")
print(iris.target_names)

# X-axis: Sepal Length
x = iris.data[:, 0]

# Y-axis: Target
y = iris.target

# Scatter Plot
plt.scatter(x, y)

plt.xlabel("Sepal Length")
plt.ylabel("Target")
plt.title("Sepal Length vs Target")

plt.show()
#hill climbing
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
