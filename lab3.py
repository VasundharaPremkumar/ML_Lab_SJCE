# 3)Visualize the n-dimensional data using contour plots.
#  Write a program to implement the A* algorithm 
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt

# Load dataset
wine = load_wine()

# Select features
x = wine.data[:,0]      # Alcohol
y = wine.data[:,1]      # Malic Acid
z = wine.target         # Wine Class

# Contour Plot
plt.tricontourf(x, y, z, levels=3)

# Show actual points
# plt.scatter(x, y, c=z)

plt.colorbar(label="Wine Class")

plt.xlabel("Alcohol")
plt.ylabel("Malic Acid")
plt.title("Contour Plot of Wine Dataset")

plt.show()

from queue import PriorityQueue

graph = {
    'A': [('B',1), ('C',3)],
    'B': [('G',2)],
    'C': [('G',1)],
    'G': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'G': 0
}

def a_star(start, goal):

    pq = PriorityQueue()

    pq.put((0, start))

    cost = {start:0}

    while not pq.empty():

        f, node = pq.get()

        print(node, end=" ")

        if node == goal:
            print("\nGoal Reached")
            return

        for neighbor, weight in graph[node]:

            g = cost[node] + weight

            if neighbor not in cost or g < cost[neighbor]:

                cost[neighbor] = g

                f = g + heuristic[neighbor]

                pq.put((f, neighbor))

a_star('A','G')