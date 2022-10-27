import sys, math
import numpy as np

vecs = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,10],[11,12]]])
xform = np.array([[3, 0], [0, 5]])
det = np.linalg.det(xform)
print(1 / det)

# print((vecs * (xform.dot(vecs.T)).T).sum(axis=1))

col = vecs[:,1,:]
print(col)
print(np.exp((col * (xform.dot(col.T)).T).sum(axis=1) * -0.5) / det)
print(math.pow(math.tau, 5/2))

Q = np.array([[.98, -.2], [.2, .98]])
L = np.array([[.5, 0],[0, 9]])
print(Q.dot(L.dot(Q.T)));

sumVecs = vecs.sum(axis=(1,2))
print(sumVecs.shape, sumVecs, vecs / sumVecs.reshape(3, 1, 1))