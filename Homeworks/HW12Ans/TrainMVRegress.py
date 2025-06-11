import numpy as np
import numpy.random as rnd
import sys

# Parse command line arguments: <TrainFile>
# TrainFile contains rows comprising 1 Y value and 5 attribute coefficients each.
# Read the file, creating a 1-D vector Y from the first column and a 2-d tensor D from
# the remaining columns.  Augment D with a column of 1's to account for the bias term.
def read_data(file_path):
    data = np.loadtxt(file_path, delimiter=' ')
    Y = data[:, 0]  # First column is Y
    D = data[:, 1:]  # Remaining columns are attributes
    D = np.hstack((np.ones((D.shape[0], 1)), D))  # Add bias term
    return Y, D

# Accept Y and D as arguments, and compute the weights using the normal equation:
# w = ((D.T)(D))^-1(D.T)(Y)
def compute_weights(Y, D):
    # Compute the weights using the normal equation
    D_transpose = np.transpose(D)
    w = np.linalg.inv(D_transpose @ D) @ D_transpose @ Y
    return w

# Check commandline args, read data, compute weights, and print them to stdout.
def main():
    if len(sys.argv) != 2:
        print("Usage: python TrainMVRegress.py <TrainFile>")
        sys.exit(1)

    train_file = sys.argv[1]

    # Read the training data
    Y, D = read_data(train_file)

    # Compute the weights
    w = compute_weights(Y, D)

    # Print the weights to stdout
    print("Regression plane offset and coeffs: ")
    print(" ".join(f"{coef:.4f}" for coef in w))
    
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()