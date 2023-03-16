# EMClustering Coding Project
This project will produce a Numpy implementation of EMClustering, along with a data generation tool to support testing the EMClustering implementation.  Learning to use Numpy and PyPlot is a principal goal of this assignment.

## Phase 1 Write a dataset generator
Use the supplied MakeMVClusters.py scaffold, and fill in missing steps to produce a program that generates a pickle file containing a single numpy array of d-dimensional points.  MakeMVClusters reads a JSON formatted file like the
supplied MV1.in, which gives a dimension value, and the mean, sigma, and point 
count for one or more clusters.  You run it thus:

python MakeMVClusters.py <configFile> <pickleOutputFile> [comma-separated options]

If the word "verbose" is one of the options, MakeMVClusters also prints the configuration, a sample of the first 10 points from the pickle file, and a picture of the generated cluster data, using PyPlot.  This comprises colored point clouds for each cluster, and also an
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

### Hints
1. matplotlib.patches offers an Ellipse class that I found useful for drawing those ellipses.
2. Other useful methods include `rnd.multivariate`, `rnd.shuffle`, and np.linalg.eigh

### Submission
Submit by first demoing a style-correct version for me, and then submitting MakeMVClusters.py to the Canvas assignment.
s
## Phase 2-4 EMClusters.py
In these phases you take the output from MakeMVClusters.py and perform the EMClustering algorithm on it.  

Create a program EMClusters.py that performs iterations of the EMCluster algorithm, per Algorithm 13.3 in our text, stopping when the total mean-change is less than .0001.  

Run EMClusters.py thus:
```
python EMClusters.py inFile outFile numClusters <options>
```
where `infile` is an output file from MakeMVClusters, and `<options>` is an optional
comma-delimited string with "just5", "verbose" and "diagonal" as options.

Once you've arrived at a clustering, write it out to `outFile` as a text formatted JSON string that is readable by MakeMVClusters.

EMClusters performs iterations of the EMCluster algorithm, per Algorithm 13.3 in 
our text, stopping when the total mean-change is less than .0001.  

### Verbose option
Under the verbose option, EMClusters prints the point set that was read in, and,
at the start of each iteration of the repeat loop, it prints the 0-based loop 
number, the point-diffs, and the $\mu$, $\Sigma$ and P values for all clusters, 
along with the resultant computed weights for all cluster/point combinations 
as a 2-D array.

And, if dimensions = 2, it displays a diagram like this:

![EMClusterPlot](EMClusterPlot.png)

It's similar to the one for MakeMVClusters.  The points are colored according to the cluster they are closest to, and the centers and ellipses are also colored.  Pop up a new diagram for each iteration of the loop, so you can watch the cluster configurations converge.  In this image, for instance, the blue cluster is competing with the green for points.  Further iterations will show it gradually winning those points neares to it and the green cluster gradually concentrating instead on the point cloud to the right.

### Just5 option
Printing all of the weights and point differences is pretty cumbersome with hundreds of points.  The "just5" option limits outputs to just the first 5 points.  I found this useful for checking the math on the steps of the algorithm without being inundated with data.

### Diagonal option
The "diagonal" option limits $\Sigma$ values to diagonal arrays.  *Importantly*, this means you do not even represent the $\Sigma$ values as 2-D arrays, bur as 1-D vectors of just the diagonal values, adjusting the relevant Numpy calls accordingly.  This is necessary in order to gain the speed expected from the diagonal assumption.

### Dropping Unpopular Clusters
A curiosity of the algorithm, not mentioned in the text, is that it's common for one or more clusters to become highly "unpopular", with P values dropping to near zero, and very few points considering the cluster their highest probability.  This can result in Nan values for probability division operations, and also cause nonsingular matrices when only a couple of points are determining the correlation matrix.  Fix this by detecting when the popularity of a cluster drops to a mean point-count under 3 points.  Adjust all cluster-dependent data (means, sigmas, prbs, number of clusters) to eliminate such unpopular clusters.

Note that this feature also makes the algorithm less dependent on accurate estimation of the number of clusters to find, since you can overestimate when you run the program, and let the unpopular-clusters trimming reduce the number of clusters if needed.

### Use of Numpy and Limits on Loops
Your program must run quickly by using Numpy.  You may start with more Python loops to get an accurate implementation, but ultimately you may have at most four computational loops in the entire program, including the main while-loop driving the iterations.  You may also have two more loops for constructing the "verbose" pyplot diagrams.

### Hints
1. Numpy methods you may find useful include argmax, full, repeat, reshape, reciprocal, sqrt, det, inv, sum, concatenate, dot, matmul, multiply, subtract, ones, where, count_nonzero.  Rnd.uniform is also useful.

2. For dropping unpopular clusters, you may find `count_nonzero` and `where` useful to generate a vector of clusters to keep.  (E.g. [0, 2, 3] if I'm dropping cluster 1 due to unpopularity).  Note that such an array may be used to index a Numpy array, selecting only the indicated indices.  Once made, it can filter all the relevant arrays, e.g. means, sigmas, etc.

3. I did not find Numpy.outer useful for computing arrays of outer products, but you might be able to get it to do that; lemme know if you do.

4. I was not able to write this without considerable side-testing of Numpy methods via a short Test.py that I altered over and over to be sure I understooed what each method did.  You should do the same.

5. Be painfully conscious of tensor shapes as you build weights, $\mu, \Sigma$, etc.
Drop comments to the side next to each tensor you create to remind you of its
dimensions.

6. The Numpy behavior called "broadcasting" is quite important to understand.  See the Numpy docs on this.

### Submission
This is clearly a sophisticated project, and by the end of it you should be well-familiar with Numpy and the EM Clustering algorithm.  Complete it in the following phases.  For each, submit by first demoing a style-correct version for me, and then submitting EMClusters.py to the relevant Canvas assignment.

## Phase 2 -- Basic Functionality
Set up initial values for means, sigmas and probabilities, and compute the weight matrix from them.  Write the EM loop, but execute it just three times so you can display the results and check your work.  Don't bother with coloring the points in your verbose display; just show the means and ellipses.  Feel free to use more loops than allowed in this phase.

## Phase 3 -- Full Numpy Use
Add point coloring, and termination of the main loop when error is small instead of running a fixed number of iterations.  Reduce the number of loops to the required limit.

## Phase 4 -- Output, Diagonal Option, Trim Clusters
Finish all features, including writing the JSON output file, implementing the diagonal feature and automated dropping of unpopular clusters.