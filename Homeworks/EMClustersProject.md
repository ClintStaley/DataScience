# EMClustering Coding Project
This project will produce a Numpy implementation of EMClustering, along with a data generation tool to support testing the EMClustering implementation.  Learning to use Numpy and PyPlot is a principal goal of this assignment.

## Phase 1 Write a dataset generator
Use the supplied MakeMVClusters.py scaffold, and fill in missing steps to produce a program that generates a pickle file containing a single numpy array of d-dimensional points.  MakeMVClusters reads a JSON formatted file like the
supplied MV1.in, which gives a dimension value, and the mean, sigma, and point 
count for one or more clusters.  You run it thus:

python MakeMVClusters.py <configFile> <pickleOutputFile> [comma-separated options]

If the word "verbose" is one of the options, MakeMVClusters also prints the configuration, a sample of the first 10 points from the pickle file, and a picture of the generated cluster data, using 
PyPlot.  This comprises colored point clouds for each cluster, and also an
ellipse at 2 standard deviation distance from the center point.

Here is a sample run of MakeMVClusters:

The pyplot display: 

![Clusters](ClusterDiagram.png)

And the command and text output (Your values may differ since they're random, but they must not all come from the same cluster):
```
$ python MakeMVClusters.py MV1.in MV1.out verbose
Generating  {'dim': 2, 'clusters': [{'mean': [3, 4], 'sigma': [[10, 0], [0, 3]], 'numPts': 100}, {'mean': [-15, 1], 'sigma': [[6.5, 3.5], [3.5, 6.5]], 'numPts': 200}, {'mean': [-3, -10], 'sigma': [[1, 2], [2, 8]], 'numPts': 400}]}
[[-14.44887245   0.80871476]
 [ -1.70872688  -7.6049518 ]
 [  4.1507679    6.41269918]
 [ -2.32286371 -10.61501481]
 [ -3.3545244  -12.41835679]
 [-12.97114612   6.75887577]
 [ -2.54195976   4.23352316]
 [ -3.38364657  -9.11110374]
 [ -2.27414744 -11.90995098]
 [-15.5385435    2.28277911]]
```

### Submission
Submit by first demoing a style-correct version for me, and then submitting MakeMVClusters.py to the Canvas assignment.

## Phase 2 Write EMClusters.py
In this phase you take the output from MakeMVClusters.py and perform the EMClustering algorithm on it.