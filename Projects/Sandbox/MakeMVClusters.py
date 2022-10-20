import sys, json
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

inFile, outFile, options = sys.argv[1:]

options = options.split(',')
verbose = "verbose" in options

inFile = open(inFile);
config = json.load(inFile)
inFile.close()

markers = ('r.', 'g.', 'b.', 'c.')
plt.axis('equal')
dim = config['dim']


pts = np.ndarray((0, dim))
print(pts.shape)
for idx, cluster in enumerate(config['clusters']):
    clsData = rnd.multivariate_normal(
        cluster['mean'], cluster['sigma'], cluster['numPts'])
    pts = np.concatenate((pts, clsData))
    if verbose:
        print(pts.shape)
        plt.plot(clsData.T[0], clsData.T[1], markers[idx % len(markers)])

pts.dump(outFile)

if verbose:
    print(config)
    print(np.load(outFile)[:10])
    plt.show()