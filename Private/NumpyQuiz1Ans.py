import math
import numpy as np
import numpy.linalg as la

pts = np.array([[1,2], [1,4], [5,6], [1,8]])
pts2 = np.array([[9,10], [10,12]])

allPts = np.concatenate((pts, pts2))                    # 3pts
colsOfPts = np.repeat(pts.reshape(4, 1, 2), 3, axis=1)  # 5pts
print(f"All Points:\n{allPts}\n3 cols:\n{colsOfPts}")

bigVec = la.eigh(pts2)[1][-1]                 # 7pts
vecAngle = math.acos(bigVec[0])               # 5pts
print(f"Big EV: {bigVec}\nAngle: {vecAngle}")