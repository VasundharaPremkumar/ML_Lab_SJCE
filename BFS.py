e = int(input("Enter the number of edges: "))
graph = {}

for i in range(e):
    u = input("Start: ")
    v = input("End: ")
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
        
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    print(i, "->", graph[i])
    
start = input("Enter starting node: ")

visited = []
queue = [start]

print("BFS Traversal:")

while queue:
    node = queue.pop(0)
    
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
