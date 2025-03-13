# 1. Take three integer commandline arguements dim, range, and numSamples.
# 2. Generate a random, dimxdim symmetric matrix cov with entries in the 
# range [-range, range].  Generate also a dimx1 vector mu with entries in
# the range [-range, range].
# 3. Generate a numSamples x dim vector samples with rows resulting from a
# multivariate normal distribution with mean mu and covariance matrix cov.
# 4. Compute the correlation matrix corr of samples.
# 5. Print cov, mu, and corr.
# 6. Output samples as a text file  Samples.txt.

import numpy as np
import sys

def main():
	if len(sys.argv) != 4:
		print("Usage: python GenCorrelation.py <dim> <range> <numSamples>")
		sys.exit(1)

	dim = int(sys.argv[1])
	rangeVal = int(sys.argv[2])
	numSamples = int(sys.argv[3])

	# Generate random symmetric matrix cov
	A = np.random.uniform(-rangeVal, rangeVal, (dim, dim))
	cov = np.dot(A, A.T)

	# Generate random vector mu
	mu = np.random.uniform(-rangeVal, rangeVal, dim)

	# Generate samples
	samples = np.random.multivariate_normal(mu, cov, numSamples)

	# Compute covariance matrix
	testCov = np.cov(samples, rowvar=False)
	
	# Compute correlation matrix
	corr = np.corrcoef(samples, rowvar=False)

	# Set print options to display 5 decimal digits without scientific notation
	np.set_printoptions(precision=5, suppress=True)

	# Print cov, mu, and corr
	print("Covariance matrix (cov):\n", cov)
	print("Covariance matrix (testCov):\n", testCov)
	print("Mean vector (mu):\n", mu)
	print("Correlation matrix (corr):\n", corr)

	# Output samples to a text file
	np.savetxt("Samples.txt", samples, fmt='%.5f')

if __name__ == "__main__":
	main()
