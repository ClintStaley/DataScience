import sys, json, math
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

inFile, outFile = sys.argv[1:3]
options = sys.argv[3].split(',') if len(sys.argv) > 3 else []
verbose = "verbose" in options

inFile = open(inFile);
config = json.load(inFile)
inFile.close()

if verbose:
    print("Generating ", config)
    plt.figure()
    ax = plt.gca()

colors = ('r', 'g', 'b', 'c')
plt.axis('equal')
dim = config['dim']

pts = np.ndarray((0, dim))
for idx, cluster in enumerate(config['clusters']):
    clsData = rnd.multivariate_normal(
      cluster['mean'], cluster['sigma'], cluster['numPts'])
    pts = np.concatenate((pts, clsData))
    if verbose:
        color = colors[idx % len(colors)]
        plt.plot(clsData.T[0], clsData.T[1], color+'.')
        transform = np.array(cluster['sigma'])
        eVals, eVecs = np.linalg.eigh(transform)
        ax.add_patch(Ellipse(xy=cluster['mean'], width = 2*eVals[1],
         height = 2*eVals[0], facecolor='None', edgecolor='k', linewidth=2,
         angle = 360*math.acos(eVecs[1][0])/math.tau))

rnd.shuffle(pts)
pts.dump(outFile)

if verbose:
    print(np.load(outFile, allow_pickle=True)[:10])
    plt.show()