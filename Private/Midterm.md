# Data Science Midterm
<div style="text-align: right">Name ________________________________________</div>

**1. 36 pts** Give terms to match the following definitions.   No credit is given for incorrect spelling.

Three alliterative terms describing how "big data" differs from ordinary data\
**volume, variety, velocity**

Prefix meaning $10^{24}$\
**yotta**

Itemset for which the removal of any item will result in a reduction of support\
**minimal generator**

Type of matrix that describes a orthogonally rotated scaling\
**positive definite**

Ratio of the joint likelihood of two events to the product of their independent likelihoods\
**lift**

Ratio of likelihood of $X\rightarrow Y$ to likelihood of X alone\
**confidence**

Ratio of intersection to union\
**Jaccard**

A common name for L-1 norm\
**Manhattan distance**

Optimization method that mimics a ball rolling down hill on a cost surface.\
**gradient descent**

Statistical test that builds on a hypergeometric distribution\
**Fisher test**

Itemset that cannot be made larger without losing support\
**closed**

Itemset that cannot be made larger without its support dropping below the threshold\
**maximal**

Kind of attribute that "favorite color" would be\
**nominal categorical**

Kind of attribute that "grade level" would be\
**ordinal categorical**

An association rule for which removal of any antecedent item results in loss of confidence\
**productive**

A tree structure that improves on a trie by labelling branches by strings, not just characters\
**radix tree or compressed trie, or (this course only)suffix tree/trie**


**2. 46pts Data Science math**

**a. 8pts** The angle in radians between vectors [2, 4, 1, 2] and [4, 2, 2, 1]\
**.643**

**b. 4pts** The L-1 norm distance between those same two vectors\
**6**

**c. 8pts** Adjust the projection formula $\frac{b^Ta}{a^Ta}$ so it gives the projection of b along a in simple length. (E.g. so a value of of 2 means b's projection onto a is 2 units long)\
**Replace denominator with $||a||$**

**d. 14pts** Write a matrix representing a $\frac{\pi}{4}$ or $45\degree$ clockwise rotation around the X axis (Z and Y axis both move toward you)\
$\begin{bmatrix}1&&0&&0\\0&&.707&&-.707\\0&&.707&&.707\end{bmatrix}$

**e. 12pts** Three models of cars are shown below, each with a popularity and a likelihood of being in the shop for repairs.  If a car is in the shop, what is the chance it's a model X?

|Model|Popularity|Repair frequency|
|---|---|---|
|X|50%|2%|
|Y|30%|4%|
|Z|20%|5%|

$\frac{.02(.5)}{(.02(.5)+.04(.3)+..05(.2)} = \frac{.01}{.01+.012+.01} = \frac{.01}{.032} = .3125$



**3. 22pts Itemset and Rule Evaluation**
I have a database D with just four transactions. Two of them have both items a and b; the other two have neither.  I wonder if $a\rightarrow b$ is a good rule...

**a. 5pts** What is the lift of $a\rightarrow b$?\
**2**

**b. 5pts** What is the confidence of $a\rightarrow b$\
**1**

**c. 12pts** For what p-value does $a\rightarrow b$ pass a Fisher test of productivity?\

$\frac{2!^4}{2!^2n!} = \frac{2!^2}{4!}=\frac{4}{24}=.1666$

Charm thing

Ukonnen thing

EMCluster thing

genEMClusters exercise

```
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
```

