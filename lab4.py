# 4)Visualize the n-dimensional data using heat-map. 
# Write a program to implement Min-Max algorithm. 
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

sns.heatmap(df.corr(), annot=True)

plt.title("Heat Map")
plt.show()

# Min-Max Algorithm

def minimax(depth, node, maximizing, values):

    # Base Condition:
    # If leaf node is reached, return its value
    if depth == 3:
        return values[node]

    # MAX player's turn
    if maximizing:

        # Choose maximum among left and right child
        return max(
            minimax(depth + 1, node * 2, False, values),      # Left child
            minimax(depth + 1, node * 2 + 1, False, values)   # Right child
        )

    # MIN player's turn
    else:

        # Choose minimum among left and right child
        return min(
            minimax(depth + 1, node * 2, True, values),       # Left child
            minimax(depth + 1, node * 2 + 1, True, values)    # Right child
        )


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Start from:
# depth = 0 (root)
# node = 0 (first node)
# maximizing = True (root is MAX)
result = minimax(0, 0, True, values)

print("Optimal Value:", result)