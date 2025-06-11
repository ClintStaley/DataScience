# Accept as commandline arguments, the number of points in a set, the normal
# vector (5 coefficients) and the origin-offset of a hyperplane in
# 5-D space, and a standard deviation.  Generate as output a set of 5-D points
# that are normally distributed about the hyperplane, with the standard deviation
# specified.

import numpy as np
import numpy.random as rnd
import sys

# Arguments: number of points, 5-D weight and offset of hyperplane, standard 
# deviation.  Set coefficients of each point to random values in range [-10,10],
# Compute the Y value of each point as y = offset * weight*P. Add a 
# a gaussian random amount to each Y, using the stdev supplied. Return the points, the 
# Y values and the noised Y values.
def makePts(num_points, normal, offs, stdDev):
    pts = rnd.uniform(-10, 10, (num_points, 5))
    y = np.dot(pts, normal) + offs
    noisedY = y + rnd.normal(0, stdDev, num_points)
    
    return pts, y, noisedY

# Parse command line arguments, generate two sets of points, and save them to files
def main():
    if len(sys.argv) != 10:
        print("Usage: python MakeRegressionSep.py <num_points> <5-D normal_vector> <offset> <std_dev> <output_file>")
        return

    num_points = int(sys.argv[1])
    normal = np.array([float(i) for i in sys.argv[2:7]])
    offs = float(sys.argv[7])
    std_dev = float(sys.argv[8])

    pts, y, noisedY = makePts(num_points, normal, offs, std_dev)

    # Save the noised Y values (first column) and the points (next 5 columns) 
    # to file <output_file>.tsv
    np.savetxt(sys.argv[9], np.column_stack((noisedY, pts)), fmt='%.4f')
    
    # Do the same for the original Y values
    np.savetxt(f"True{sys.argv[9]}", np.column_stack((y, pts)), fmt='%.4f')
    
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()