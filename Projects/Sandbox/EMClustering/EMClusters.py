import sys, json, math
import numpy as np
import numpy.linalg as la
import numpy.random as rnd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

colors = ('r', 'g', 'b', 'c', 'm', 'y')
eps = 1e-4

def main():
    inFile, outFile, numCls = sys.argv[1:4]
    numCls = int(numCls)
    options = sys.argv[4].split(',') if len(sys.argv) > 4 else []
    verbose = "verbose" in options
    diagonal = "diagonal" in options

    meansDelta = math.inf

    # Get points, numPts, and their dimension and value range
    pts = np.load(inFile, allow_pickle=True)
    numPts, dim = pts.shape
    tau2halfDim = math.pow(math.tau, dim / 2)
    dbgPts = 5 if "just5" in options else numPts

    maxVals = pts.max(axis=0) # 1-D array of max vals per dimension
    minVals = pts.min(axis=0) # 1-D array of min vals per dimension

    # Set initial values for cluster configuration
    means = rnd.uniform(minVals, maxVals, (numCls, dim))
    sigmas = np.ones((numCls, dim)) if diagonal else np.full(
     (numCls, dim, dim), np.identity(dim))
    prbs = np.full((numCls), 1.0/numCls)

    if verbose:
        print(f"Points: {pts[:dbgPts]}")
        plt.figure()
        plt.axis('equal')

    while meansDelta > eps:     # while (adjust > eps):
        # Repeat points in numCls columns, to get (numPts, numCls, dim) array
        ptDiffs = np.repeat(np.reshape(pts, (numPts, 1, dim)), numCls, axis=1
         ) -  means  # subtract mean values from each cluster column
        
        dets = sigmas.prod(axis=1) if diagonal else np.linalg.det(sigmas)
        expScales = np.reciprocal(np.sqrt(dets) * tau2halfDim)
    
        weights = np.ndarray((numPts, 0))
        for clsIdx in range(0, numCls):
            col = ptDiffs[:, clsIdx]                 # (numpts, dim)
            if diagonal:
                invSigma = np.reciprocal(sigmas[clsIdx]) * -.5  # - Sigma^-1 / 2
                exponents = (invSigma.reshape((1, dim)) * col * col).sum(axis=1)
            else: 
                invSigma = la.inv(sigmas[clsIdx]) * -.5         # - Sigma^-1 / 2
                exponents = (col * invSigma.dot(col.T).T).sum(axis=1)

            col = np.exp(exponents) * expScales[clsIdx] * prbs[clsIdx]
            weights = np.concatenate((weights, col.reshape((numPts, 1))),
             axis = 1)

        # Normalize for Bayesian
        weights = weights / weights.sum(axis=1, keepdims=True) # (numPts, numCls)

        # Redo means
        denoms = weights.T.sum(axis=1)                         # (numCls,)
        priorMeans = means
        means = weights.T.dot(pts)/denoms.reshape((numCls, 1)) # (numCls, dim)

        # Redo sigmas
        if diagonal:
            sigmas = np.ndarray((0, dim))
        else:
            sigmas = np.ndarray((0, dim, dim))
        for clsIdx in range(0, numCls):
            col = ptDiffs[:, clsIdx]                        # (numpts, dim)
            if diagonal:
                sigCol = np.multiply(weights.T[clsIdx].reshape(numPts, 1), 
                 (col * col))                               # (numPts, dim)
                sigma = sigCol.sum(axis=0) / denoms[clsIdx]
                sigmas = np.append(sigmas, sigma.reshape((1,dim)), axis=0)
            else:
                sigCol = np.matmul(col.reshape(numPts, dim, 1), 
                 col.reshape(numPts, 1, dim))               # (numPts, dim, dim)
                sigCol = np.multiply(weights.T[clsIdx].reshape(numPts, 1, 1),
                 sigCol)
                sigma = sigCol.sum(axis=0) / denoms[clsIdx]
                sigmas = np.append(sigmas, sigma.reshape((1,dim,dim)), axis=0)

        # Redo Prbs
        prbs = denoms / numPts
            
        meansDelta = ((means - priorMeans)*(means - priorMeans)).sum()

        if verbose:
            report(pts, ptDiffs, weights, means, sigmas, prbs, meansDelta,
             dbgPts, diagonal)

        keepSize = np.count_nonzero(denoms > 5)
        if (keepSize < len(means)):
            toKeep = np.where(denoms > 5)
            print(f"Dropping to {keepSize} clusters counts: {denoms} toKeep:{toKeep}")
            means = means[toKeep]
            sigmas = sigmas[toKeep]
            prbs = prbs[toKeep]
            numCls = keepSize

    json.dump(makeDict(means, sigmas, prbs, numPts),
     open(outFile, "w"), indent = 3)

def report(pts, ptDiffs, weights, means, sigmas, prbs, meansDelta, dbgPts, diag):
    numCls = means.shape[0]

    print(f"Diffs: {ptDiffs[:dbgPts]}\n")
    print(f"Weights: {weights[:dbgPts][:]}") # (numPts, numCls)
    print(f"Means: {means}")                 # (numCls, dim)
    print(f"Sigmas: {sigmas}")               # (numCls, dim, dim)
    print(f"Prbs: {prbs}")                   # (numCls)
    print(f"Delta: {meansDelta}")

    # Plot points per color of most-liked cluster
    clsPerPt = np.argmax(weights, axis=1)    # (numPts)
    for cls in range(numCls):
        clrPts = pts[clsPerPt == cls].T
        print(len(clrPts.T))
        plt.plot(clrPts[0], clrPts[1], colors[cls % len(colors)]+'.')

    # Plot means and sigmas
    for mIdx, mean in enumerate(means):
        color = colors[mIdx % len(colors)]
        plt.plot(mean.T[0], mean.T[1], color+'o')
        if (diag):
           angle = 0
           (width, height) = 2*sigmas[mIdx]
        else:
           eVals, eVecs = np.linalg.eigh(sigmas[mIdx])
           angle = 360*math.atan(eVecs[1][1]/eVecs[1][0])/math.tau
           (height, width) = 2*eVals[:2]

        plt.gca().add_patch(Ellipse(xy=mean, width=width, height=height,
         facecolor='None', edgecolor=color, linewidth=2, angle=angle));

    plt.show()

def makeDict(means, sigmas, prbs, numPts):
    clusters = []
    for mean, sigma, prb in zip(means, sigmas, prbs):
        clusters.append({
            "mean": mean.round(3).tolist(),
            "sigma": sigma.round(3).tolist(),
            "numPts": int(round(numPts*prb))})
        
    return {
        "dim": means.shape[1],
        "clusters" : clusters
    }

main()