import sys, json, math
import numpy as np
import numpy.linalg as la
import numpy.random as rnd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

inFile, outFile, numCls = sys.argv[1:4]
numCls = int(numCls)
options = sys.argv[4].split(',') if len(sys.argv) > 4 else []
verbose = "verbose" in options

eps = 1e-6
adjust = math.inf

# Get points, numPts, and their dimension and value range
pts = np.load(inFile, allow_pickle=True)
numPts, dim = pts.shape
tau2halfDim = math.pow(math.tau, dim / 2)

maxVals = pts.max(axis=0) # 1-D array of max vals per dimension
minVals = pts.min(axis=0) # 1-D array of min vals per dimension

# Set initial values for cluster configuration
means = rnd.uniform(minVals, maxVals, (numCls, dim))
sigmas = np.full((numCls, dim, dim), np.identity(dim))
prbs = np.full((numCls), 1.0/numCls)

print(f"Points: {pts}, Min/max: {minVals}, {maxVals}\n\n")

if verbose:
     print(f"Points: {pts}")
     plt.figure()
     colors = ('r', 'g', 'b', 'c')
     plt.axis('equal')
     ax = plt.gca()

for step in range(0,1):     # while (adjust > eps):
    print(f"Step {step} -----------------------\n"
     f"Means:\n{means}\nSigmas: {sigmas}\nPrbs: {prbs}\n")

    # Repeat points in numCls columns, arriving at (numPts, numCls, dim) array
    ptDiffs = np.repeat(np.reshape(pts, (numPts, 1, dim)), numCls, axis=1
     ) -  means  # subtract mean values from each cluster column
    
    expScales = np.reciprocal(np.sqrt(np.linalg.det(sigmas)) * tau2halfDim)
    print(f"Diffs: {ptDiffs}\nExpScales: {expScales}\n")
   
    weights = np.ndarray((numPts, 0))
    for clsIdx in range(0, numCls):
        col = ptDiffs[:, clsIdx]  # (numpts, dim)
        invSigma = la.inv(sigmas[clsIdx]) * -.5  # - Sigma^-1 / 2
        col = (col.dot(invSigma.dot(col.T)).T).sum(axis=1) * expScales[clsIdx]
        weights = np.concatenate((weights, col.reshape((numPts, 1))), axis = 1)
    print(f"Weights: {weights}")                   # (numPts, numCls)

    denoms = weights.T.sum(axis=1)                          # (numCls,)
    means = weights.T.dot(pts)/denoms.reshape((numCls, 1))  # (numCls, dim)

    sigmas = np.ndarray((numCls, dim, dim))
    for clsIdx in range(0, numCls):
        col = ptDiffs[:, clsIdx]  # (numpts, dim)
        sigCol = np.matmul(col.reshape(numPts, dim, 1),  # (numPts, dim, dim)
         col.reshape(numPts, 1, dim))
        sigCol = np.multiply(weights.T[clsIdx].reshape(numPts, 1, 1), sigCol)
        print(sigCol.shape, sigCol)
        sigma = sigCol.sum(axis=0) / denoms[clsIdx]
        print(sigma.shape, sigma)
        sigmas = np.append(sigmas, sigma.reshape((1,2,2)), axis=0)
    prbs = denoms / numPts
        
    if verbose:
        print(f"Weights: {weights}")             # (numPts, numCls)
        print(f"Means: {means}")                 # (numCls, dim)
        print(f"Sigmas: {sigmas}")               # (numCls, dim, dim)
        print(f"Probs: {prbs}")                  # (numCls)
        plt.plot(pts.T[0], pts.T[1], 'k.')
        for mIdx, mean in enumerate(means):
            color = colors[mIdx % len(colors)]
            plt.plot(mean.T[0], mean.T[1], color+'o')
        #eVals, eVecs = np.linalg.eigh(transform)
        #print(eVals, eVecs)
        #ax.add_patch(Ellipse(xy=cluster['mean'], width = 2*eVals[1],
        # height = 2*eVals[0], facecolor='None', edgecolor='k', linewidth=2,
        # angle = 360*math.acos(eVecs[1][0])/math.tau))
        plt.show()
