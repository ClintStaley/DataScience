# Generate two 100-point sets of 5-D points drawn from two 5-D Gaussian distributions,
# The means of the distributions are two randomly chosen 5-D locations that 
# are at least 10 units apart.  The covariance matrices for the two 
# distributions are diagonal, with the diagonal elements randomly chosen 
# between .5 and 2.  Output the two sets to files Set1.txt and Set2.txt

import numpy as np
import numpy.random as rnd

# Function to generate a random 5-D point
def generate_random_point():
    return rnd.uniform(-10, 10, 5)

# Ensure the two means are at least 10 units apart
# Function to generate means that are at least 10 units apart
def generate_means():
    while True:
        mean1 = generate_random_point()
        mean2 = generate_random_point()
        if np.linalg.norm(mean1 - mean2) >= 10:
            return mean1, mean2

# Function to generate a random diagonal covariance matrix
def generate_covariance():
    return np.diag(rnd.uniform(0.5, 2, 5))

# Function to generate the datasets
def generate_datasets():
    mean1, mean2 = generate_means()
    cov1 = generate_covariance()
    cov2 = generate_covariance()
    print("Mean1:", mean1)
    print("Mean2:", mean2)
    set1 = rnd.multivariate_normal(mean1, cov1, 100)
    set2 = rnd.multivariate_normal(mean2, cov2, 100)
    return set1, set2

def makeTestSet(set1, set2, numTests):
    testSet = np.zeros((numTests, 6))
    for i in range(numTests):
        if rnd.uniform() < 0.5:
            testSet[i] = np.append(set1[rnd.randint(0, 100)], 1)
        else:
            testSet[i] = np.append(set2[rnd.randint(0, 100)], 2)
    return testSet

# Main function
if __name__ == "__main__":
    set1, set2 = generate_datasets()
    testSet = makeTestSet(set1, set2, 100)
    
    set1, set2 = generate_datasets()
    testSet = makeTestSet(set1, set2, 100)
    
    np.savetxt("Set1.tsv", set1, fmt='%.4f')
    np.savetxt("Set2.tsv", set2, fmt='%.4f')
    np.savetxt("TestSet.tsv", testSet[:,:5], fmt='%.4f')
    np.savetxt("TestSetLabels.tsv", testSet, fmt='%.4f')
