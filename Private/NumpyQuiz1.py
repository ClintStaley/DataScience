import math
import numpy as np
import numpy.linalg as la

pts = np.array([[1,2], [1,4], [5,6], [1,8]])
pts2 = np.array([[9,10], [10,12]])

allPts = ___________________________ # Tack pts2 onto end of pts
colsOfPts = ________________________ # Make a (4, 3, 2) array by repeating pts
print(f"All Points: {allPts}\n3 cols: {colsOfPts}")

bigVec = __________________________  # Biggest eigenvector of pts2
vecAngle = ________________________  # CCW radians between X+ axis and bigVec
print(f"Big EV: {bigVec}\nAngle: {vecAngle}")