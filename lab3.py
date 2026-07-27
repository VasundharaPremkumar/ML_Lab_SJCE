# 3) Visualize the n-dimensional data using contour plots.
# Write a program to implement the A* algorithm

from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
from queue import PriorityQueue      # Imports Priority Queue (removes smallest f value first)

# Load dataset
wine = load_wine()

# Select features
x = wine.data[:,0]      # Alcohol
y = wine.data[:,1]      # Malic Acid
z = wine.target         # Wine Class

# Draw contour plot
plt.tricontourf(x, y, z, levels=3)
# plt.scatter(x, y, c=z)      # Uncomment to show actual data points
plt.colorbar(label="Wine Class")
plt.xlabel("Alcohol")
plt.ylabel("Malic Acid")
plt.title("Contour Plot of Wine Dataset")
plt.show()

# A* Algorithm
graph = {}                          # Dictionary to store graph

n = int(input("Enter number of edges: "))

# Take graph input
for i in range(n):
    u = input("Source: ")
    v = input("Destination: ")
    w = int(input("Cost: "))

    if u not in graph:              # Create source node if not present
        graph[u] = []
    if v not in graph:              # Create destination node if not present
        graph[v] = []

    graph[u].append((v, w))         # Store (destination, cost)

heuristic = {}                      # Dictionary to store heuristic values

# Take heuristic value for each node
for node in graph:
    heuristic[node] = int(input(f"Heuristic of {node}: "))

start = input("Enter Start Node: ") # Read start node
goal = input("Enter Goal Node: ")   # Read goal node

def a_star(start, goal):
    pq = PriorityQueue()            # Create priority queue
    pq.put((0, start))              # Insert start node
    cost = {start: 0}               # Store actual cost (g)

    while not pq.empty():           # Continue until queue becomes empty
        f, node = pq.get()          # Remove node with smallest f value
        print(node, end=" ")

        if node == goal:            # Check if goal is reached
            print("\nGoal Reached")
            return

        for neighbor, weight in graph[node]:     # Visit all neighbours
            g = cost[node] + weight              # Calculate actual cost

            if neighbor not in cost or g < cost[neighbor]:  # Better path found
                cost[neighbor] = g               # Update cost
                f = g + heuristic[neighbor]      # Calculate f = g + h
                pq.put((f, neighbor))            # Insert into priority queue

a_star(start, goal)                 # Call A* algorithm