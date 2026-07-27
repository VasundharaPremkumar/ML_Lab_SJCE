# 4) Visualize the n-dimensional data using Heat Map.
# Write a program to implement Min-Max Algorithm.

from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris()                                      # Load Iris dataset
df = pd.DataFrame(iris.data, columns=iris.feature_names) # Convert dataset into DataFrame

sns.heatmap(df.corr(), annot=True)                      # Draw heat map
plt.title("Heat Map")
plt.show()

# Min-Max Algorithm

def minimax(depth, node, maximizing, values):
    if depth == max_depth:                              # Leaf node reached
        return values[node]
    if maximizing:                                      # MAX player's turn
        return max(minimax(depth+1, node*2, False, values),
                   minimax(depth+1, node*2+1, False, values))
    else:                                               # MIN player's turn
        return min(minimax(depth+1, node*2, True, values),
                   minimax(depth+1, node*2+1, True, values))

max_depth = int(input("Enter maximum depth: "))         # Read tree depth
n = 2 ** max_depth                                      # Number of leaf nodes

values = []                                             # Store leaf values
print(f"Enter {n} leaf node values:")

for i in range(n):
    values.append(int(input(f"Value {i+1}: ")))

result = minimax(0, 0, True, values)                    # Start from root
print("Optimal Value:", result)