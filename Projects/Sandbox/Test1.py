import numpy as np

#print(bigArr)
#print(bigArr + smallArr)
#print(np.repeat(np.reshape(smallArr, (2, 1, 2)), 3, axis=1))
# print(smallArr.dot(bigArr[:,1,1]))

Q = np.array([[.866, -.5], [.5, .866]])
S = np.array([[10, 0],[0, 5]])

xform = Q.dot(S.dot(Q.T))
print(xform, np.linalg.eigh(xform))
print(xform.dot([1.732, 1]))

print(np.linalg.inv([[5.16, .16], [.16, .96]]))
print(xform, np.linalg.eigh(np.array([[5.16, .16], [.16, .96]])))
