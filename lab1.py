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

# Objective function that we want to maximize
# f(x) = -x² + 5
# Maximum value occurs at x = 0
def objective(x):
    return -x**2 + 5


# Hill Climbing Algorithm
def hill_climbing(start, step):

    # Start from the initial state
    current = start

    # Repeat until no better neighbor is found
    while True:

        # Generate neighboring states
        # One step to the left
        left = current - step

        # One step to the right
        right = current + step

        # If left neighbor has a better value,
        # move to the left neighbor
        if objective(left) > objective(current):
            current = left

        # Otherwise, if right neighbor has a better value,
        # move to the right neighbor
        elif objective(right) > objective(current):
            current = right

        # If neither neighbor is better,
        # we have reached the peak
        else:
            break

    # Return the best solution found
    return current


# Starting point of the search
solution = hill_climbing(-0.1, 0.1)

# Display the optimal solution
print("Best Solution:", solution)

# Display the maximum value of the objective function
print("Maximum Value:", objective(solution))