# 🌐 Breadth First Search (BFS) Algorithm

This program implements the **Breadth First Search (BFS)** algorithm using a graph represented with an adjacency list.

---

## 📌 Problem Statement

Write a program to perform **Breadth First Search (BFS)** traversal on a graph starting from a given node.

---

## 🧠 Concept Overview

**Breadth First Search (BFS)** is a graph traversal algorithm that:
- Visits nodes **level by level**
- Explores all neighbors of a node before moving deeper
- Uses a **queue (FIFO - First In First Out)**

---

## 📊 Key Idea

- Start from a node
- Visit all its neighbors
- Then visit neighbors of neighbors
- Continue until all reachable nodes are visited

---

## ⚙️ Algorithm Steps

1. Create an empty graph (dictionary)
2. Take edges as input and build adjacency list
3. Choose a starting node
4. Initialize:
   - `visited` list
   - `queue` with starting node
5. Repeat until queue is empty:
   - Remove node from queue
   - If not visited:
     - Print node
     - Mark as visited
     - Add unvisited neighbors to queue

---
## 🔍 Code Explanation

### 1. Graph Creation

- A dictionary is used to store the graph  
- Each node maps to a list of its neighbors  

---

### 2. Input Handling

- User enters edges  
- Graph is built as an **undirected graph**  

---

### 3. BFS Traversal

- `queue` → stores nodes to visit  
- `visited` → keeps track of visited nodes  

---

### 4. Main Logic

- Remove node from queue  
- If not visited:
  - Print the node  
  - Add its neighbors to the queue

---

## 🧪 Key Observations

- BFS visits nodes **level by level**
- Uses a **queue**
- Avoids cycles using `visited`
- Ensures each node is visited **only once**

---

## ⚠️ Limitations

- ❌ Uses more memory than DFS  
- ❌ Not efficient for very deep graphs  
- ❌ Requires queue management  

---

## ✅ Advantages

- ✔️ Guarantees shortest path in unweighted graph  
- ✔️ Simple and easy to understand  
- ✔️ Works well for level-order traversal  

---

## 🎯 Applications

- Shortest path in unweighted graphs  
- Social networks  
- Web crawling  
- GPS/navigation systems  
- AI search problems  

---

## ❓ Viva Questions & Answers

### 1. What is BFS?
BFS is a traversal algorithm that explores nodes level by level using a queue.

---

### 2. What data structure is used in BFS?
A **queue (FIFO)** is used.

---

### 3. What is the difference between BFS and DFS?
- BFS → level-wise traversal (uses queue)  
- DFS → depth-wise traversal (uses stack/recursion)  

---

### 4. Why do we use a visited list?
To avoid revisiting nodes and prevent infinite loops.

---

### 5. What is the time complexity of BFS?
**O(V + E)**  
(V = vertices, E = edges)

---

### 6. What is the space complexity?
**O(V)** due to queue and visited list.

---

### 7. Can BFS be used to find shortest path?
Yes, in **unweighted graphs**, BFS gives the shortest path.

---

### 8. What type of graph is used here?
An **undirected graph**.

---

### 9. What happens if we don’t check visited?
The algorithm may go into an **infinite loop**.

---

### 10. Why do we check `neighbor not in queue`?
To avoid adding duplicate nodes into the queue.

---

### 11. What is adjacency list?
A representation where each node stores a list of its neighbors.

---

### 12. Can BFS work on directed graphs?
Yes, with slight modification (remove reverse edge).

---

### 13. What is FIFO?
First In First Out — the first element added is the first to be removed.

---

### 14. What happens if starting node is not in graph?
It will cause an **error (KeyError)**.

---

### 15. Is BFS complete?
Yes, BFS is **complete** for finite graphs.

---

## 🏁 Conclusion

This program demonstrates BFS traversal using a queue and adjacency list. It is widely used in graph problems and guarantees shortest paths in unweighted graphs.
