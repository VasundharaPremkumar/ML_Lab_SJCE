# 2)Visualize the n-dimensional data using 3D surface plots. 
# Write a program to implement the Best First Search (BFS) algorithm. 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
iris = load_iris()

# Select three dimensions
x = iris.data[:,0]   # Sepal Length
y = iris.data[:,1]   # Sepal Width
z = iris.data[:,2]   # Petal Length

# Create 3D figure
fig = plt.figure()

# Create 3D axes
ax = fig.add_subplot(111, projection='3d')

# Plot surface points
ax.scatter(x, y, z)

# Labels
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Length")

plt.title("3D Surface Plot")
plt.show()

from queue import PriorityQueue

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['G'],
    'G': []
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 4,
    'E': 2,
    'G': 0
}

def best_first_search(start, goal):

    visited = set()

    pq = PriorityQueue()

    pq.put((heuristic[start], start))

    while not pq.empty():

        h, node = pq.get()

        print(node, end=" ")

        if node == goal:
            print("\nGoal Reached")
            return

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

best_first_search('A', 'G')