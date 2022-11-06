import sys, math
import numpy as np
import numpy.linalg as la

# Array-based outer product test
# Q = np.array([[.98, -.2], [.2, .98]])
# L = np.array([[.5, 0],[0, 9]])
#print(Q.dot(L.dot(Q.T)));

#print(f"TD: {np.tensordot(Q, L, 1)}\nDot: {Q.dot(L)}")

pts = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
pts2 = np.array([[2,3,4],[2, 1, 3], [5, 6, 6], [9, 8, 7]])
#print(f"Prod: {pts[0].T * pts[1]} Transpose: {pts[0].T}")
#right = pts.reshape(4,1,3)
#left = pts.reshape(4,3,1)
#print(f"Right: {right}\nLeft: {left}\n")
#sigmas = np.matmul(left, right);
#weights = np.array([.2, .4, .3, .1])
# print(f"Test: {np.multiply(weights.reshape(4,1,1), sigmas)}")
#print(f"Weights: {weights}\nSigmas: {sigmas}\nWeighted: {weights.dot(sigmas)}")

def makeGrid(minVals, maxVals, numCls, dims):
     rtn = np.ndarray((numCls, dim))
     jumps = maxVals - minVals;
     repeats = numCls

     for dim in range(dims):
         steps = math.ceil(math.pow(repeats, 1/dim))
         repeats /= steps
         ranges[dim] /= steps
         for clsIdx in range(numCls):
             rtn[clsIdx][dim] = minVals[dim] + ranges[dim] 

ptsDiff = pts - pts2
delta = (ptsDiff*ptsDiff).sum();
print(f"diff {ptsDiff}\nprd: {ptsDiff*ptsDiff}\ndelta: {delta}")