import numpy as np

# Return d, projected onto first principal component
def doPCA(d):
   numPts = len(d)
   mean = d.mean(axis=0)
   dBar = d - mean
   sigmas = np.matmul(dBar.reshape(numPts, 2, 1), dBar.reshape(numPts, 1, 2))
   sigma = sigmas.sum(axis=0) / numPts
   eVals, eVecs = np.linalg.eigh(sigma)
   totalVar = sigma.trace()

   print(f"Dbar: {dBar}\nSigma:\n{sigma}\nEVals: {eVals}\nEVecs:\n{eVecs}\n")
   print(f"Reducing variance by {eVals[-1]} from {totalVar}")

   return np.dot(dBar, eVecs[-1]).reshape(numPts, 1)*eVecs[-1] + mean

def main():
   prjD = doPCA(np.array([[8, -20], [0, -1], [10, -19], [10, -20], [2, 0]]))
   print(f"Projected: {prjD}")

main()
