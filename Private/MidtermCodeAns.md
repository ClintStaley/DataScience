# Midterm (Coding Section)
<div style="text-align: right">Name __________________________________________</div>

1. 60pts\
Below is an implementation of Charm.  It has 4 bugs and 4 blank spots to fill in.  Fix the bugs and fill in the blanks, without adding new lines of code, and without fixing anything that isn't broken. 

```
import sys, pickle
import pandas as pd
import collections as cll;

# items: hierarchichal list, tids: simple set, sup: integer
ITGroup = cll.namedtuple('ITGroup', 'items, tids, sup')
ItemSet = cll.namedtuple('ItemSet', 'items, tids')

def flatten(itemList):
    rtn = set()
    for item in itemList:
        rtn = rtn | (flatten(item) if ________________________________
         Ans: (type(item) is list) 8pts  else {item}) 8pts 
    return rtn

def charm(itGroups, minSup, cSets):
   for idx1, grp1 in enumerate(itGroups):
      subGroups = []
      idx2 = idx1              Ans  + 1 6pts
      while (idx2 < len(itGroups)):
         grp2 = itGroups[idx2]
         jointTids = grp1.tids | grp2.tids    Ans: | => & 8pts
         sup = len(jointTids)
         if sup >= minSup:
            if grp1.tids == grp2.tids:        
               grp1.items.append(grp2.items)
               del itGroups[idx2]
               _____________________________  Ans: idx2 -= 1 8pts
            else:
               if grp1.tids > grp2.tids:      Ans: > => <  6pts
                  grp1.items.append(grp2.items)
               else:           
                  subGroups.append(ITGroup([grp1.items, grp2.items],
                   jointTids, sup))
         idx2 += 1

      if len(subGroups):
         charm(subGroups, minSup, cSets)

      newSet = ________________________ Ans: flatten(grp1.items) 8pts
      for existingSet in cSets:
         if (newSet == existingSet.items and existingSet.tids == grp1.tids):
         Ans: == => <= 8pts
            newSet = None
            break;
      if newSet != None:
         cSets.append(ItemSet(newSet, grp1.tids))

def main():
   supSets = pd.read_pickle(sys.argv[1])
   minSup = int(sys.argv[3])

   cSets = [];

   itmSets = list(map(lambda v: ITGroup([v[0]], v[1], len(v[1])),
    enumerate(map(set, filter(lambda s: len(s) >= minSup, supSets["userIds"])))))

   itmSets.sort(key=_________________)   Ans: lambda x: len(x.tids)  8pts

   charm(itmSets, minSup, cSets)
   
   pickle.dump(cSets, open(sys.argv[2], "wb"))
   checkRead = pickle.load(open(sys.argv[2], "rb"))
   print(f"Read/write check\n{checkRead[:10]}\n{checkRead[-10:]}\n")

main()
```

2. 86 pts\
Below is an implementation of EMClusters, without the diagonal or verbose optoins.  It has with 3 bugs and 8 blank spots to fill in (including the three comments).  Fix the bugs and fill in the blanks, without adding new lines of code, and without fixing anything that isn't broken.  Note the comment above the main while loop indicating that all code above that point is correct.

```
import sys, json, math
import numpy as np
import numpy.linalg as la
import numpy.random as rnd
import matplotlib.pyplot as plt

colors = ('r', 'g', 'b', 'c', 'm', 'y')
eps = 1e-4

def main():
    inFile, outFile, numCls = sys.argv[1:4]
    numCls = int(numCls)
    options = sys.argv[4].split(',') if len(sys.argv) > 4 else []

    meansDelta = math.inf

    # Get points, numPts, and their dimension and value range
    pts = np.load(inFile, allow_pickle=True)
    numPts, dim = pts.shape
    tau2halfDim = math.pow(math.tau, dim / 2)

    maxVals = pts.max(axis=0) # array of max vals per dimension
    minVals = pts.min(axis=0) # array of min vals per dimension

    # Set initial values for cluster configuration
    means = rnd.uniform(minVals, maxVals, (numCls, dim))
    sigmas = np.full((numCls, dim, dim), np.identity(dim))
    prbs = np.full((numCls), 1.0/numCls)

    # All code above here is correct.  Shapes are:
    # means.shape =  _____________     Ans: (numCls, dim) 2pts
    # sigmas.shape = _______________   Ans: (numCls, dim, dim) 2pts
    # prbs.shape = _______________     Ans: (numCls) 2pts

    while meansDelta > eps: 
        # Repeat points in numCls column to get (numPts, numCls, dim) array

        ptDiffs = np.repeat(np.reshape(pts, _________________), numCls, axis=1)        
        # Ans: (numPts, 1, dim) 8pts

        ptDiffs = _______________________________________
        # Ans: ptDiffs - mean 8pts

        dets = np.linalg.det(sigmas)
        expScales = np.reciprocal(np.sqrt(dets) * tau2halfDim)
    
        weights = np.ndarray((numPts, 0))  # Will be (numPts, numCls) when done
        for clsIdx in range(0, numCls):
            col = ptDiffs[:, clsIdx]                   # (numpts, dim)
            invSigma = la.inv(sigmas[clsIdx]) * -.5    # - Sigma^-1 / 2
            exponents = (col * invSigma.dot(col.T).T).sum(axis=1)

            col = np.exp(exponents) * expScales[clsIdx] * prbs[clsIdx]
            weights = np.concatenate((weights, col.reshape((numPts, 1))))
             
            Ans: need axis = 1  12pts

        # Normalize for Bayesian
        weights = weights / __________________________
        
        # Ans: weights.sum(axis=1, keepdims=True) sum 8pts, axis 8pts keep 8pts

        # Redo means
        denoms = weights.T.sum(axis=1)      
        priorMeans = means
        means = weights.T.dot(pts)/denoms________________________
         
        # Ans .reshape((numCls, 1)) 8pts

        # Redo sigmas
        sigmas = np.ndarray((0, dim, dim))

        for clsIdx in range(0, numCls):
            col = ptDiffs[:, clsIdx]                    # (numpts, dim)
            sigCol = np.matmul(col.reshape(numPts, dim, 1), 
             col.reshape(numPts, 1, dim))               # (numPts, dim, dim)
            sigCol = np.multiply(weights.T[clsIdx].reshape(numPts, 1, 1),
             sigCol)
            sigma = sigCol.sum(axis=0) / denoms
            
            # Ans: add [clsIdx]  8pts
            sigmas = np.append(sigmas, sigma.reshape((1,dim,dim)), axis=0)

        # Redo Prbs
        prbs = denoms;             Ans add  / numPts  12pts
            
        meansDelta = ((means - priorMeans)*(means - priorMeans)).sum()

    json.dump(makeDict(means, sigmas, prbs, numPts),
     open(outFile, "w"), indent = 3)

def makeDict(means, sigmas, prbs, numPts):
    clusters = []
    for mean, sigma, prb in zip(means, sigmas, prbs):
        clusters.append({
            "mean": mean.round(3).tolist(),
            "sigma": sigma.round(3).tolist(),
            "numPts": int(round(numPts*prb))})
        
    return {
        "dim": ___________________   #Ans: means.shape[1] or equiv,  8pts
        "clusters" : clusters
    }

main()
```
