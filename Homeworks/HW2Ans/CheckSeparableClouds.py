# Accept commandline arugments for two input files and one test file
# From each input file, read in a numpy array of 5-D points.  For each array,
# find its 5-D mean, and a normalized vector between the means.  Find the 
# minimum and maximum projections of the points onto the direction vector, and
# use these to determine if the two sets are separable.  If they are not, print
# an error message and exit.  Otherwise, for each point in the test file
# determine if it is closer to the mean of set1 or set2, and output the test
# file with an additional 6th column of 1s and 2s to indicate the classification.

import numpy as np
import sys

# For the provided set of 5-D points pts and normalized vector dir, find the
# minimum and maximum projections of the points onto the direction vector, and
# return the two values.
def project_onto_direction(pts, dir):
    projections = np.dot(pts, dir)
    return np.min(projections), np.max(projections)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python CheckSeparableClouds.py Set1.tsv Set2.tsv Test.tsv")
        sys.exit(1)
        
    # Read the two point sets and compute the normalized direction vector between
    # their means.
    set1 = np.loadtxt(sys.argv[1])
    set2 = np.loadtxt(sys.argv[2])
    mean1 = np.mean(set1, axis=0)
    mean2 = np.mean(set2, axis=0)
    direction = mean2 - mean1
    direction /= np.linalg.norm(direction)
    
    # Project the two sets of points onto the direction vector.  If the min/max
    # ranges of the two sets overlap, the sets are not separable.  Report an 
    # error message and exit.  Otherwise, determine the average of the 
    # projections of the two means onto the direction vector.
    min1, max1 = project_onto_direction(set1, direction)
    min2, max2 = project_onto_direction(set2, direction)
    if min1 <= max2 and min2 <= max1:
        print("The two sets are not separable.")
        sys.exit(1)
    if min1 < min2:
        avg_projection = (max1 + min2) / 2
    else:
        avg_projection = (min1 + max2) / 2
    
    # Set print precision to 3 decimal places and print the data
    np.set_printoptions(precision=3)
    print(f"Mean1: {mean1}\nMean2: {mean2}")
    print(f"Min1: {min1} Max1: {max1}")
    print(f"Min2: {min2} Max2: {max2}")
    print(f"Direction: {direction}, Midpoint projection: {avg_projection}")
    
    # Read the third test file into a numpy array.  Add a 6th column with values
    # 1 or 2, depending on whether the dot product of the row and direction is
    # less than or greater than avg_projection.  (Which means the test point is
    # closer to the mean of set 1 or set 2.  Then output the resultant 6-column
    # array to <testFile>.labels. 
    
    testSet = np.loadtxt(sys.argv[3])
    testSet = np.hstack((testSet, np.zeros((testSet.shape[0], 1))))
    projections = np.dot(testSet[:,:5], direction)
    testSet[:,5] = np.where(projections < avg_projection, 1, 2)
    
    np.savetxt(sys.argv[3] + ".labels", testSet, fmt='%.4f')
