import sys, json, math
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

inFile, outFile = sys.argv[1:3]
# Check for third option and set "verbose" if it's part of the third option

inFile = open(inFile);
config = json.load(inFile)
inFile.close()

dim = config['dim']

if verbose:
    print("Generating ", config)
    plt.figure()
    ax = plt.gca()
    colors = ('r', 'g', 'b', 'c')
    plt.axis('equal')

pts = np.ndarray((0, dim))  # Start the points array with no rows

for idx, cluster in enumerate(config['clusters']):
    clsData = rnd.multivariate_normal(
    cluster['mean'], cluster['sigma'], cluster['numPts'])
    
    # Tack new set of points onto pts

    if verbose:
        color = colors[idx % len(colors)]
        plt.plot(clsData.T[0], clsData.T[1], color+'.')
        # Analyze sigma transform to find eigenvalues and eigenvectors. 
        # Find angle that will swing the x axis onto the direction of the 
        # eigenvector with largest eigenvalue.  Use this information to
        # create a black ellipse two std deviations from the center.
        ax.add_patch(Ellipse(xy=cluster['mean'], facecolor='None',
            edgecolor='k', linewidth=2,

# Shuffle points randomly

pts.dump(outFile)

if verbose:
    plt.show()
    print(np.load(outFile, allow_pickle=True)) # Print just the first 10 pts