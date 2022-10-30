import sys, math
import numpy as np
import numpy.linalg as la

# vecs = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,10], [11,12]]])
vecs = np.array([[[1,2], [1,4]], [[5,6], [1,8]], [[9,10], [1,12]]])
print(np.reciprocal(np.sqrt(la.det(vecs))))

# print((vecs * (xform.dot(vecs.T)).T).sum(axis=1))

Q = np.array([[.98, -.2], [.2, .98]])
L = np.array([[.5, 0],[0, 9]])
#print(Q.dot(L.dot(Q.T)));

#print(f"TD: {np.tensordot(Q, L, 1)}\nDot: {Q.dot(L)}")

#sumVecs = vecs.sum(axis=(1,2))
#print(sumVecs.shape, sumVecs, vecs / sumVecs.reshape(3, 1, 1))

pts = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Prod: {pts[0].T * pts[1]} Transpose: {pts[0].T}")
right = pts.reshape(3,1,3)
left = pts.reshape(3,3,1)
sigmas = np.matmul(left, right);
weights = np.array([.2, .5, .3])
print(sigmas.shape, weights.shape)
print(f"Test: {np.multiply(weights.reshape(3,1,1), sigmas)}")
print(f"Weights: {weights}\nSigmas: {sigmas}\nWeighted: {weights.dot(sigmas)}")
