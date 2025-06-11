import numpy as np
import numpy.random as rnd
import sys


# TestFile contains rows comprising 1 Y value and 5 attribute coefficients each.
# Read the file, creating a 1-D vector Y from the first column and a 2-d tensor D from
# the remaining columns.  Augment D with a column of 1's to account for the bias term.
def read_data(file_path):
    data = np.loadtxt(file_path, delimiter=' ')
    Y = data[:, 0]  # First column is Y
    D = data[:, 1:]  # Remaining columns are attributes
    D = np.hstack((np.ones((D.shape[0], 1)), D))  # Add bias term
    return Y, D

# Read the test data, and compute a yHat value for each row using the regression plane.
# Print the yHat values to stdout, followed by a MSE value between yHat and Y.
def test_regression_plane(offset, coords, test_file):
    # Read the test data
    Y, D = read_data(test_file)

    # add offset as the first value of coords
    coords = np.insert(coords, 0, offset)
    
    # Compute the regression plane values from D and coords
    yHat = np.dot(D, coords)
    
    # Compute the Mean Squared Error (MSE)
    mse = np.mean((Y - yHat) ** 2)

    # Print the yHat values and MSE
    print("yHat values:")
    for value in yHat:
        print(value)
    print("Mean Squared Error (MSE):", mse)
    
# # Parse command line arguments: <offset> <coords> <TestFile>
# where <offset> is the offset for the regression plane, <coords> are the 
# 5 coordinates of the plane, and <TestFile> is the file containing test data.
# 
def main():
    if len(sys.argv) != 8:
        print("Usage: python TestMVRegress.py <offset> <coord1> <coord2> <coord3> <coord4> <coord5> <TestFile>")
        sys.exit(1)

    # Read command line arguments
    offset = float(sys.argv[1])
    coords = np.array([float(coord) for coord in sys.argv[2:7]])
    test_file = sys.argv[7]

    # Test the regression plane with the provided parameters
    test_regression_plane(offset, coords, test_file)
    
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()