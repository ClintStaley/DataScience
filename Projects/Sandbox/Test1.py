import numpy as np

bigArr = np.ones((10, 2, 2))
smallArr = np.array([[1,2], [2,3]])
column = np.array([ [[1,2]] , [[2,3]], [[3,4]] ])

#print(bigArr)
#print(bigArr + smallArr)
#print(np.repeat(np.reshape(smallArr, (2, 1, 2)), 3, axis=1))
print(smallArr.dot(bigArr[:,1,1]))