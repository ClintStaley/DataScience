# Numpy Quiz 1
<div style="text-align: right">Name ________________________________________</div>

1. 20pts 
Fill in the four missing lines in the provided NumpyQuiz1.py file to match
the comments, and the output shown.  (Do not simply use constant values, e.g.
for the vector angle -- compute these in a way that would work for any values of
pts and pts2, provided the latter is positive definite).  Do not add new lines, nor more than 50 chars for each space.  (Most need only half that many.) You may use an editor, Python interpreter, and Numpy docs.

Model output:

```
import math
import numpy as np
import numpy.linalg as la

pts = np.array([[1,2], [1,4], [5,6], [1,8]])
pts2 = np.array([[9,10], [10,12]])

allPts = np.concatenate((pts, pts2))                  # 3pts
colsOfPts = np.repeat(pts.reshape(4,1,2), 3, axis=1)  # 5pts
print(f"All Points:\n{allPts}\n3 cols:\n{colsOfPts}")

bigVec = la.eigh(pts2)[1][-1]                 # 7pts
vecAngle = math.acos(bigVec[0])               # 5pts
print(f"Big EV: {bigVec}\nAngle: {vecAngle}")
```