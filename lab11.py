# Import Perceptron model
from sklearn.linear_model import Perceptron

# Input combinations
X = [[0,0],
     [0,1],
     [1,0],
     [1,1]]

# ---------------- AND ----------------

# AND truth table outputs
y = [0,0,0,1]

# Create perceptron model
model = Perceptron()

# Train model
model.fit(X,y)

print("AND Function")

# Test all inputs
for i in X:
    print(i,"->",model.predict([i])[0])

# ---------------- OR ----------------

# OR truth table outputs
y = [0,1,1,1]

# Create perceptron model
model = Perceptron()

# Train model
model.fit(X,y)

print("\nOR Function")

# Test all inputs
for i in X:
    print(i,"->",model.predict([i])[0])