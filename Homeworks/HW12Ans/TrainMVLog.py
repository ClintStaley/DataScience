import numpy as np
import numpy.random as rnd
import sys


# Read the file, creating a 1-D vector C from the first column and a 2-d tensor 
# D from the remaining columns.  Augment D with a column of 1's to account for 
# the bias term. Determine the maximum value of 0-based C, plus 1, to get 
# the number of classes. Create a y vector of rows, each a one-hot vector 
# of the class number.
def read_data(file_path):
    data = np.loadtxt(file_path, delimiter=' ')
    C = data[:, 0].astype(int)                   # First column of class numbers
    D = data[:, 1:]  # Remaining columns are attributes
    D = np.hstack((np.ones((D.shape[0], 1)), D))  # Add bias term
    num_classes = int(np.max(C)) + 1 
    Y = np.zeros((D.shape[0], num_classes)) 
    for i in range(D.shape[0]):
        Y[i, C[i]] = 1  # One-hot encoding of class number
    
    return Y, D

# Compute the weights for a multivariate logistic regression model.
# Start with a 0 weight vector of size (num_classes, num_features).
# Repeatedly:
#   - Save the existing weights for comparison
#   - Compute the gradient of the log-likelihood function with respect to the weights.
#   - Update the weights using the gradient and a learning rate.
#   - Check for convergence by computing the MSE between the old and new weights.
#   - If the MSE is less than a threshold, break the loop.
def compute_weights(Y, D, learning_rate, max_iterations, convergence_threshold):
    weights = np.zeros((Y.shape[1], D.shape[1]))  # Initialize weights
    for iteration in range(max_iterations):
        old_weights = weights.copy()
        
        # For each sample in D, compute per-class probabilities based on softmax
        # and the current weights
        exp_scores = np.exp(np.dot(D, weights.T))
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        
        gradients = (Y - probs)         # Gradient of the likelihood function
        gradients = gradients.T @ D     # Matrix multiplication for dot-product
        weights += learning_rate * gradients
        
        # Check for convergence using MSE
        mse = np.mean((old_weights - weights) ** 2)
        print(f"Epoch {iteration}: MSE = {mse:.6f}")
        if mse < convergence_threshold:
            print(f"Converged after {iteration} iterations.")
            break
        
    return weights
    

# Parse command line arguments: <TrainFile> <OutputFile> <learnRate> <maxIter>
# <convergenceThreshold>
# TrainFile contains rows comprising an integer class number and 5 attribute 
# coefficients each.
# Check commandline args, read data, compute weights, write them to output file.
def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 6:
        print("Usage: python TrainMVLog.py <TrainFile> <OutputFile> <learnRate> <maxIter> <convergenceThreshold>")
        sys.exit(1)
        
    train_file = sys.argv[1]
    output_file = sys.argv[2]
    learn_rate = float(sys.argv[3])
    max_itrs = int(sys.argv[4])
    convergence_threshold = float(sys.argv[5])
    
    # Read the test data
    Y, D = read_data(train_file)
    
    print("Computing weights...")
    weights = compute_weights(Y, D, learn_rate, max_itrs, convergence_threshold)
    np.savetxt(output_file, weights, delimiter=' ', fmt='%0.6f')
    
    
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()