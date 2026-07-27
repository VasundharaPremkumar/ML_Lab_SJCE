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

# best first search
from queue import PriorityQueue
graph={}
heuristic={}
n=int(input("Enter the number of nodes"))
for i in range(n):
    node=input("Enter the node")
    neighbors=input(f"Enter the neighbors of the {node} (space separated)").split()
    graph[node]=neighbors
    heuristic[node]=input(f"Enter the heuristic value of {node}")

def best_first_search(start,goal):
    pq=PriorityQueue()
    visited=set()
    pq.put((heuristic[start],start))
    while not pq.empty():
        h,node=pq.get()
        print(node,end=" ")
        if node==goal:
            print("Goal Reached")
            return
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor],neighbor))       
    print("Goal not reachable")
start=input("Enter the beginning node")
goal=input("enter the end node")
best_first_search(start,goal)
