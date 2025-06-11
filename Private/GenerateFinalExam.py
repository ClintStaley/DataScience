# Accept as commandline arguments, the number of points in a set, the normal
# vector (4 coefficients) and the origin-offset of a hyperplane in
# 4-D space, and a standard deviation.  Generate as output a set of 4-D points
# that are normally distributed about the hyperplane, with the standard deviation
# specified.

import numpy as np
import numpy.random as rnd
import sys

dimension = 4

# Arguments: number of points, 5-D weight and offset of hyperplane, standard 
# deviation.  Set coefficients of each point to random values in range [-10,10],
# Compute the Y value of each point as y = offset * weight*P. Add a 
# a gaussian random amount to each Y, using the stdev supplied. Return the points, the 
# Y values and the noised Y values.
def makePts(num_points, normal, offs, stdDev):
    pts = rnd.uniform(-10, 10, (num_points, dimension))
    y = np.dot(pts, normal) + offs
    noisedY = y + rnd.normal(0, stdDev, num_points)
    
    return pts, y, noisedY

# Parse command line arguments, generate two sets of points, and save them to files
def main():
    if len(sys.argv) != 5 + dimension:
        print("Usage: python MakeRegressionSep.py <num_points> <normal_vector> <offset> <std_dev> <output_file>")
        return

    num_points = int(sys.argv[1])
    normal = np.array([float(i) for i in sys.argv[2:2+dimension]])
    offs = float(sys.argv[2+dimension])
    std_dev = float(sys.argv[3+dimension])

    pts, y, noisedY = makePts(num_points, normal, offs, std_dev)

    # Save the noised Y values (first column) and the points (next 5 columns) 
    # to file <output_file>.tsv
    np.savetxt(sys.argv[4+dimension], np.column_stack((pts, noisedY)), fmt='%.4f')
    
    # Do the same for the original Y values
    np.savetxt(f"True{sys.argv[4+dimension]}", np.column_stack((pts, y)), fmt='%.4f')
    
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()