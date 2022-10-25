import sys
import numpy as np

vecs = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,10],[11,12]]])
xform = np.array([[3, 0], [0, 5]])

# print((vecs * (xform.dot(vecs.T)).T).sum(axis=1))

col = vecs[:,1,:]
print(col)
print((col * (xform.dot(col.T)).T).sum(axis=1))
