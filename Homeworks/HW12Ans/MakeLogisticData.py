import numpy as np
import numpy.random as rnd
import sys

## Generate random points in 5-D space, with range [-10, 10] and assign them 
# to classes based on the closest centroid.  Write the class index and point 
# coordinates to a file.
def generate_and_write_points(file_path, centroids, num_points):
    with open(file_path, 'w') as f:
        for _ in range(num_points):
            # Generate a random point in 5-D space
            point = rnd.uniform(-10, 10, 5)
            # Calculate distances from the point to each centroid
            distances = np.linalg.norm(point - centroids, axis=1)
            # Find the index of the closest centroid
            closest_class = np.argmin(distances)
            # Write the class index and point to the file
            f.write(f"{closest_class} {' '.join(map(str, point))}\n")

# Parse command line arguments: <number of classes "C"> <number of pts "P"> <trainFile> <testFile>  
# Generate C random 5-D centroid points in range [-10, 10], and P random 5-D
# points in that same range.  For each point, compute a vector of distances
# to each centroid.  Assign the point to the class of the closest centroid.
# Output the class index and point coefficients for each point, one point per line
# in the trainFile.  Repeat this for the testFile, using the same centroids.
# The testFile will be used to test the classifier.  
# The trainFile will be used to train the classifier.
def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python MakeLogisticData.py <number of classes> <number of points> <trainFile> <testFile>")
        sys.exit(1)

    # Read command line arguments
    num_classes = int(sys.argv[1])
    num_points = int(sys.argv[2])

    # Generate random centroids for each class
    centroids = rnd.uniform(-10, 10, (num_classes, 5))
    print("Centroids:", centroids)

    # Call the function for both trainFile and testFile
    train_file = sys.argv[3]
    test_file = sys.argv[4]
    generate_and_write_points(train_file, centroids, num_points)
    generate_and_write_points(test_file, centroids, num_points)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()