import numpy as np
import numpy.random as rnd

pts = np.array([
 [  7.23828336,   3.09333045],
 [ -3.75895141, -10.87525812],
 [-14.58810855,   2.38893346],
 [  2.93480208,   3.74077959],
 [ -3.08733115, -11.03265158],
 [-20.63817606,  -2.88388447]]);

numCls = 3
numPts = len(pts)
dim = pts.shape[1]

# Find min and max values in dimensions, shape (dim,)
maxVals = pts.max(axis=0) # 1-D array of max vals per dimension
minVals = pts.min(axis=0) # 1-D array of min vals per dimension

# Set initial values for cluster configuration
means = rnd.uniform(minVals, maxVals, (numCls, dim))

# Create a (numPts, numCls, dim) array of point differences
ptDiffs = np.repeat(np.reshape(pts, (numPts, 1, dim)), numCls, axis=1
 ) -  means  # subtract mean values from each cluster column

print(f"Min/Max: {minVals} {maxVals}\n\nMeans: {means}\n\nPtDiffs: {ptDiffs}")