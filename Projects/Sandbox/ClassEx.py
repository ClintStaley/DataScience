import numpy as np

S = np.array([[5, 0], [0,10]])
Q = np.array([[.866,-.5],[.5,.866]])
print(Q.T)
xform = Q.dot(S.dot(Q.T))
print(xform)
print(np.linalg.eigh(xform))
# print xform*[1.732, 1]