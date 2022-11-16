import sys
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

vals = rnd.multivariate_normal([5, 10], [[1, 5], [5, 10]], 100, 'warn').T
plt.plot(vals[0], vals[1], "bo")
plt.axis("equal")
plt.show()