# 5)Visualize the n-dimensional data using Box-plot. 
# Write a program to implement Alpha-beta pruning algorithm. 
# Box Plot using Iris Dataset

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()

# Create box plot for all 4 features
plt.boxplot(iris.data)

# Feature names on x-axis
plt.xticks(
    [1, 2, 3, 4],
    ['Sepal Length', 'Sepal Width',
     'Petal Length', 'Petal Width'],
    rotation=15
)

plt.title("Box Plot of Iris Dataset")
plt.ylabel("Values")

plt.show()

# Alpha-Beta Pruning Algorithm

MAX, MIN = 1000, -1000

def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    # Leaf node reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN

        for i in range(2):
            val = alpha_beta(depth + 1,
                             nodeIndex * 2 + i,
                             False,
                             values,
                             alpha,
                             beta)

            best = max(best, val)
            alpha = max(alpha, best)

            # Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for i in range(2):
            val = alpha_beta(depth + 1,
                             nodeIndex * 2 + i,
                             True,
                             values,
                             alpha,
                             beta)

            best = min(best, val)
            beta = min(beta, best)

            # Pruning
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alpha_beta(0, 0, True, values, MIN, MAX)

print("Optimal Value:", result)