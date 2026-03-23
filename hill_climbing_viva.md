# 🧗 Hill Climbing Algorithm (AI Lab Program)

This program demonstrates the **Hill Climbing Algorithm**, a simple optimization technique used in **Artificial Intelligence** to find the best solution by iteratively improving the current state.

---

## 📌 Problem Statement

Implement the **Hill Climbing Algorithm** to find the **maximum value** of a mathematical function.

---

## 🧠 Concept Overview

Hill Climbing is a **local search algorithm** that:
- Starts from an initial solution
- Moves to a neighboring solution
- Chooses the neighbor with a **better value**
- Stops when no better neighbor exists

---

## 📈 Function Used

The function used in this program is:
-f(x) = -(x²) + 5


### 🔍 Properties:
- It is a **downward-opening parabola**
- The **maximum value occurs at x = 0**
- Maximum value = **5**

---

## ⚙️ Algorithm Steps

1. Start with an initial value of `x`
2. Evaluate `f(x)`
3. Check neighbors:
   - Left → `x - 1`
   - Right → `x + 1`
4. Move to the neighbor with a higher value
5. Repeat until no better neighbor exists
6. Return the optimal solution

---

## 🧪 Key Observations

- The algorithm always converges to **x = 0**
- This is because the function has **only one global maximum**
- No local maxima are present in this function

---

## ⚠️ Limitations of Hill Climbing

- ❌ Can get stuck in **local maxima**
- ❌ Cannot handle **flat regions (plateaus)**
- ❌ May fail in complex search spaces

---

## ✅ Advantages

- ✔️ Simple to implement  
- ✔️ Requires less memory  
- ✔️ Efficient for simple problems  

---

## 🎯 Applications

- Optimization problems  
- Artificial Intelligence search techniques  
- Game playing  
- Machine learning parameter tuning  

---

## ❓ Viva Questions & Answers

### 1. What is Hill Climbing?
Hill Climbing is a local search algorithm that continuously moves toward increasing value to find the optimal solution.

---

### 2. Is Hill Climbing complete?
No, it is **not complete** because it may get stuck in local maxima.

---

### 3. What is a local maximum?
A point where the function value is higher than its neighbors but not the highest overall.

---

### 4. What is a global maximum?
The highest value of the function across the entire search space.

---

### 5. Why does this program always give x = 0?
Because the function has a **single global maximum at x = 0**.

---

### 6. What are the limitations of Hill Climbing?
- Gets stuck in local maxima  
- Cannot move across flat regions  
- No backtracking  

---

### 7. How can we overcome limitations?
- Random restart hill climbing  
- Simulated annealing  
- Genetic algorithms  

---

### 8. What type of algorithm is Hill Climbing?
It is a **greedy local search algorithm**.

---

### 9. What is the role of the objective function?
It evaluates how good a solution is and guides the search.

---

### 10. What happens if multiple peaks exist?
The algorithm may stop at a **local maximum instead of global maximum**.

---

## 🏁 Conclusion

This program successfully demonstrates how the Hill Climbing algorithm works for optimization problems. It is simple yet powerful but has limitations in complex scenarios.
