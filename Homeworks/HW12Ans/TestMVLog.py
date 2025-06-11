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
    Y = data[:, 0].astype(int)                   # First column of class numbers
    D = data[:, 1:]  # Remaining columns are attributes
    D = np.hstack((np.ones((D.shape[0], 1)), D))  # Add bias term
    
    return Y, D

# for each row of D, compute the per-class probabilities based on softmax and
# the provided weights, where W has one row per class.  Determine the max
# softmax value for each row and make that its class number.  Create a confusion
# matrix, and return it.
def classifySamples(Y, D, W):
    # Compute the softmax probabilities
    exp_scores = np.exp(D @ W.T)  # Softmax numerators per row per class
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)  # Normalize

    # Get the predicted class for each sample
    predicted_classes = np.argmax(probs, axis=1)

    # Create a confusion matrix
    confusion_matrix = np.zeros((W.shape[0], W.shape[0]), dtype=int)
    for i in range(Y.shape[0]):
        confusion_matrix[Y[i], predicted_classes[i]] += 1

    return confusion_matrix

# Parse command line arguments: <TestFile> <WeightsFile>
# TestFile contains rows comprising an integer class number and 5 attribute 
# coefficients each.  WeightsFile contains a matrix of weights, one row per class,
# with the first column being the bias term.  Read both files and call classifySamples
# to classify the test data. Output the resultant confusion matrix to the console.
def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python TestMVLog.py <TestFile> <WeightsFile>")
        sys.exit(1)

    # Read command line arguments
    test_file = sys.argv[1]
    weights_file = sys.argv[2]

    # Read the test data and weights
    Y, D = read_data(test_file)
    W = np.loadtxt(weights_file, delimiter=' ')
    
    # Check if the number of classes in weights matches the test data
    if W.shape[0] != np.max(Y) + 1:
        print(f"Error: Number of classes in weights does not match test data ({np.max(Y) + 1}).")
        sys.exit(1)

    # Classify the samples and get the confusion matrix
    confusion_matrix = classifySamples(Y, D, W)

    # Print the confusion matrix
    print("Confusion Matrix:")
    print(confusion_matrix)
    
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()