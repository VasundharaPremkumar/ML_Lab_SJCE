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

# Best first search program 
from queue import PriorityQueue      # Import the PriorityQueue class to always remove the node with the smallest heuristic value first.

graph = {}                           # Empty dictionary to store the graph (Adjacency List).
heuristic = {}                       # Empty dictionary to store heuristic values of each node.

n = int(input("Enter number of nodes: "))   # Read the total number of nodes from the user.

for i in range(n):                   # Repeat 'n' times to take input for every node.
    node = input("Enter node: ")     # Read the current node name (Example: A).
    
    # Read all neighbours of the current node in one line.
    # Example Input: B C
    # .split() converts "B C" into ['B', 'C']
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    
    graph[node] = neighbors          # Store the neighbours in the graph dictionary.
                                     # Example: graph['A'] = ['B', 'C']
    
    heuristic[node] = int(input(f"Enter heuristic value of {node}: "))
                                     # Read and store the heuristic value.
                                     # Example: heuristic['A'] = 10

def best_first_search(start, goal):  # Function takes start node and goal node as input.

    visited = set()                  # Empty set to keep track of visited nodes.

    pq = PriorityQueue()             # Create an empty Priority Queue.

    # Insert the start node into the priority queue.
    # Tuple format: (heuristic value, node)
    # Example: (10, 'A')
    pq.put((heuristic[start], start))

    # Continue until the priority queue becomes empty.
    while not pq.empty():

        # Remove the node having the smallest heuristic value.
        # Example returned tuple: (6, 'C')
        # Python automatically stores:
        # h = 6
        # node = 'C'
        h, node = pq.get()

        print(node, end=" ")         # Print the current node without moving to the next line.

        # Check if the current node is the goal.
        if node == goal:
            print("\nGoal Reached")  # Goal found.
            return                   # Exit the function immediately.

        visited.add(node)            # Mark the current node as visited.

        # Get all neighbours of the current node.
        # Example:
        # graph['A'] gives ['B', 'C']
        for neighbor in graph[node]:

            # Only insert neighbours that haven't been visited yet.
            if neighbor not in visited:

                # Insert neighbour into the priority queue.
                # Example:
                # heuristic['C'] = 6
                # Queue stores (6, 'C')
                pq.put((heuristic[neighbor], neighbor))

    # If queue becomes empty and goal was never found.
    print("\nGoal Not Reachable")

# Read the starting node from the user.
start = input("Enter start node: ")

# Read the goal node from the user.
goal = input("Enter goal node: ")

# Call the Best First Search function.
best_first_search(start, goal)
