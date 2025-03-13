# Hierarchical Clustering

## Readings
Zaki
  * Chapter 14

### Exercises

1. Zaki Ch 14 Q2 But just show the merges e.g.(`ab, ckg -> abckg`) , not the full matrix each time.  And do this for both single and full linking, commenting on the difference. Which method works better in this case do you think?  If we define a set's "diameter" as the largest distance between any two points in the set, which method results in smaller diameter groups?**

**Single:\
c,k -> ck\
ck,g -> ckg\
d,e -> de\
de, i -> dei\
a,b -> ab\
ab, ckg -> abckg\
\
Full\
c,k -> ck\
d,e -> de\
a,b -> ab\
ck, g-> ckg\
de, i -> dei\
f, ckg-> cfkg\
h,j->hj\
\
Quite similar outcomes, but full does a better job by getting hj together rather than the larger-diameter abckgf group.  In general, we expect smaller diameters from the full match**

2. Zaki Ch 14 Q4a

**Ans: $\frac{n_i}{n_i + n_j}\frac{\sum_{x \in C_i}\sum_{y \in C_r} ||x-y||}{n_i n_r} +
\frac{n_j}{n_j + n_j}\frac{\sum_{x \in C_j}\sum_{y \in C_r} ||x-y||}{n_i n_r}$\
= $\frac{\sum_{x \in C_i}\sum_{y \in C_r} ||x-y||}{(n_i+n_j) n_r} +
\frac{\sum_{x \in C_j}\sum_{y \in C_r} ||x-y||}{(n_i+n_j) n_r}$\
= $\frac{\sum_{x \in C_i\cup C_j}\sum_{y \in C_r} ||x-y||}{(n_i+n_j) n_r}$**

3. Zaki provides a complexity analysis for clustering.  Answer these questions regarding it:

a. Explain exactly the $O(n^2log(n))$ he arrives at.  What causes each n, and the log(n)? **n overall steps; for each n updates of nearest distance, updates in heap take log(n)**

b. He cites $O(log(n))$ as heap update/add cost, but there are $n^2$ items in the heap.  Why isn't that $O(log(n^2))$? **Ans: $O(log(n^2) = O(2*log(n)) = O(log(n)$))**

c. He cites initial heap construction as $O(n^2)$ but this is incorrect.  How, and does it affect the final result? **Each insert is $Olog(n)$ so init should be $O(n^2log(n))$ but this is same as merging complexity, so no change**

d. He does not take into account dimension d, which for some cases may be large.  How does this affect the complexity?  Roughly speaking, what value of d would begin to matter?  **Adds d to initialization, but nowhere else, given Lance-Williams.  So, complexity changes to $O(n^2d + n^2log(n))$ Roughly, $d > log(n)$ begins to make d of interest.**


### Numpy
A project analyzing these hierarchical measures may involve use of numpy, so here are a couple more numpy exercises.

4. Assume you have a numpy array vals of 10 3-D data points.  Vals has shape (10, 3).   *With a single numpy assignment and no Python loops*, create a numpy array relativeVals of shape (10, 5, 3) comprising 5 columns of points, each a copy of vals. Actually write the code and confirm it works via printing relativeVals.shape and relativeVals.  Submit the code and a run.

**weights = np.repeat(np.reshape(pts, (10, 1, 3)), 5, axis=1)**

5. Now also assume a numpy array "means" of 3-D means of 5 clusters, of shape (5, 3).  Modify your one assignment to relativeVals so each column now represents the difference between the points and the mean point of one of the clusters.

**add " - means"**

