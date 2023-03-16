import numpy as np
import numpy.linalg as la

def main():
   d = np.array([[8, -20], [0, -1], [10, -19], [10, -20], [2, 0]])
   numPts = len(d)
   mean = d.mean(axis=0)
   dBar = d - mean
   sigmas = np.matmul(dBar.reshape(numPts, 2, 1), dBar.reshape(numPts, 1, 2))
   sigma = sigmas.sum(axis=0) / numPts
   eVals, eVecs = np.linalg.eigh(sigma)
   print(f"Mean:\n{mean}\nSigma:\n{sigma}\nEigs:\n{list(zip(eVals, eVecs))}\n")

main()