# Training data for AND gate (Input combinations)
X = [[0,0],[0,1],[1,0],[1,1]]      # Input features
y = [0,0,0,1]                      # Expected (target) outputs for AND gate

# Initial weights and bias
w1 = 0                             # Weight for first input
w2 = 0                             # Weight for second input
b = 0                              # Bias value
lr = 1                             # Learning rate (α)

# Step Activation Function
def step(x):
    if x >= 0:                     # If net input is greater than or equal to 0
        return 1                   # Output is 1
    return 0                       # Otherwise output is 0

epoch = 0                          # Counts the number of training iterations

# Train until there are no errors
while True:
    error_count = 0                # Counts wrong predictions in one epoch
    epoch += 1                     # Move to the next epoch

    print("\nEpoch", epoch)        # Display current epoch number

    # Check every training sample
    for i in range(len(X)):        # Loop through all 4 input combinations
        x1, x2 = X[i]              # Extract the two input values

        # Calculate net input
        net = x1*w1 + x2*w2 + b    # Net = x1*w1 + x2*w2 + bias

        # Predict output using activation function
        output = step(net)         # Apply step function to get predicted output

        # Calculate prediction error
        error = y[i] - output      # Error = Target - Predicted Output

        # Update weights and bias using Perceptron Learning Rule
        w1 = w1 + lr*error*x1      # Update weight w1
        w2 = w2 + lr*error*x2      # Update weight w2
        b = b + lr*error           # Update bias

        # Display current training result
        print(X[i], "Target:", y[i], "Output:", output)

        # Check whether prediction was wrong
        if error != 0:             # If error exists
            error_count += 1       # Increase error count

    # Stop training if all predictions are correct
    if error_count == 0:           # No errors in the entire epoch
        break                      # Exit the training loop

# Display final learned parameters
print("\nFinal Weights")
print("w1 =", w1)                 # Final weight for first input
print("w2 =", w2)                 # Final weight for second input
print("bias =", b)                # Final bias

# Test the trained perceptron
print("\nTesting")
for x1, x2 in X:                  # Test all input combinations
    net = x1*w1 + x2*w2 + b       # Calculate net input
    print([x1,x2], "->", step(net)) # Display predicted output