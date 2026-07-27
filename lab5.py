# 5) Visualize the n-dimensional data using Box Plot.
# Write a program to implement Alpha-Beta Pruning Algorithm.

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()                                      # Load Iris dataset

plt.boxplot(iris.data)                                  # Draw box plot
plt.xticks([1,2,3,4], ['Sepal Length','Sepal Width','Petal Length','Petal Width'], rotation=15)
plt.title("Box Plot of Iris Dataset")
plt.ylabel("Values")
plt.show()

# Alpha-Beta Pruning Algorithm

MAX, MIN = 1000, -1000

def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == max_depth:                              # Leaf node reached
        return values[nodeIndex]

    if maximizingPlayer:                                # MAX player's turn
        best = MIN
        for i in range(2):
            val = alpha_beta(depth+1, nodeIndex*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:                           # Pruning
                break
        return best
    else:                                               # MIN player's turn
        best = MAX
        for i in range(2):
            val = alpha_beta(depth+1, nodeIndex*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:                           # Pruning
                break
        return best

max_depth = int(input("Enter maximum depth: "))         # Read tree depth
n = 2 ** max_depth                                      # Number of leaf nodes

values = []                                             # Store leaf values
print(f"Enter {n} leaf node values:")

for i in range(n):
    values.append(int(input(f"Value {i+1}: ")))
maximising=bool(int(input("enter 0-Min or 1 for MAX"))) #to decide who is playing first whether it is max or min
result = alpha_beta(0, 0, maximising, values, MIN, MAX)       # Start from root

print("Optimal Value:", result)