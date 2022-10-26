import sys, json, math
import numpy as np
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
numPts = len(pts)
dim = pts.shape[1]
tau2halfDim = math.pow(math.tau, dim / 2)

maxVals = pts.max(axis=0) # 1-D array of max vals per dimension
minVals = pts.min(axis=0) # 1-D array of min vals per dimension

# Set initial values for cluster configuration
means = rnd.uniform(minVals, maxVals, (numCls, dim))
sigmas = np.full((numCls, dim, dim), np.identity(dim))
prbs = np.full((numCls), 1.0/numCls)

if (adjust > eps):
    print(f"Means:\n{means[:2]}\nSigmas: {sigmas[:2]}\nPrbs: {prbs[:2]}\n")

    # Repeat points in numCls columns, arriving at (numPts, numCls, dim) array
    ptDiffs = np.repeat(np.reshape(pts, (numPts, 1, dim)), numCls, axis=1) -
     means  # subtract mean values from each cluster column
    
    expScales = np.reciprocal(np.sqrt(np.linalg.det(sigmas)) * tau2halfDim)
    print(f"Diffs: {ptDiffs[:2]}\nExpScales: {expScales[:2]}\n")
   
    weights = np.ndarray((numPts, numCls))
    for clsIdx in range (0..numCls):
        col = initWeights[:,clsIdx,:]
        col = (col * (sigmas[clsIdx].dot(col.T)).T).sum(axis=1)
         * expScales[clsIdx]
        weights = np.concatenate((weights, col), axis = 1);

    print(f"Final weights: {weights[:2][:2]}")

    #  compute sum fijP(ca) across all k


if verbose:
    print("Analyzing ", pts[:10], "...", pts[-10:0], " with range ", minVals,
     " to ", maxVals);
    plt.figure()
    colors = ('r', 'g', 'b', 'c')
    plt.axis('equal')
    ax = plt.gca()

    if verbose:
        color = colors[idx % len(colors)]
        plt.plot(clsData.T[0], clsData.T[1], color+'.')
        transform = np.array(cluster['sigma'])
        eVals, eVecs = np.linalg.eigh(transform)
        print(eVals, eVecs)
        ax.add_patch(Ellipse(xy=cluster['mean'], width = 2*eVals[1],
         height = 2*eVals[0], facecolor='None', edgecolor='k', linewidth=2,
         angle = 360*math.acos(eVecs[1][0])/math.tau))
