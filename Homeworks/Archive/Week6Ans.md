# Week 6

## Readings
Zaki
  * Chapter 14, 15 and 17

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

3. Assuming n points, of dimension d, and an $L_2$ norm, what is the complexity of computing a hierarchical categorization?   Is this complexity different per cluster distance measure?  What part of the algorithm takes the most time?  Explain your reasoning.

* For simplicity, assume we reduce the entire set to 1 category eventually. 
* Assume that as part of the data structure, we maintain, for each current cluster, a pointer to its closest cluster.
* Assume use of Lance-Williams.

**We must first compute interpoint distances and near-cluster pointers.  This is $O(dn^2)$ regardless.** 

**Then we must, n times, merge two clusters.  A merge requires an O(n) min operation, then an O(1) merge of two clusters, followed by an O(n) update of closest cluster for all other clusters viz-a-viz the new one.  Given Lance-Williams, dimension d has no effect.  So $O(n^2)$.  Overall complexity is thus determined by the initialization step of $O(dn^2)$, which is the most expensive**



3. Ch 15 Q1

**a. Core: b, c, d, e, f, g, h, i, j, k, n, o, p, q, r, s, t, v, w  (all but a, l, m, u)**

**b. Yes**

**c. Yes: i, e, c, f, j, n**

**d. No, since y may not be core**

**e. Yes.  l - t - w - x**

**f Yes, since reachability from central point goes both ways**

**g. {p, q, v, r, s, t, w, x, k, h, d, a, l}, {m, i, e, b, c, f, g, j, n, o, u}**

### Information Entropy

X. Assume you have a non-uniform probability distribution, with event probabilities ranging from .25 down to .01.  You divide one of the existing events into two equally-likely events, e.g. dividing an event E with 20% probability into E1 and E2 each with 10% probability.  Assuming $log_2$, what is the largest possible increase in entropy resulting from such a division?  The smallest?

**Dividing a .25 event will result in increase of .25 entropy.  Dividing a .01 event results in .01 entropy increase.**

X. Entropy is a common means of measuring password strength.  A very good password will have, for instance, 40 bits of entropy.  Describe a password choosing system that would result in that much entropy.

**A random 40-bit number will suffice, though it's hard to remember.  A 10-digit hex value will also work, as would a 13-digit number (though not a 12-digit)**.  

X. A very good means of choosing high-strength password is to randomly build a phrase by drawing words from a dictionary of say 4096 possibilities.  A four-word such phrase might be "red dog true red".  Assumingly uniformly random choices from a 4096 word dictionary, what is the information entropy of such a pass phrase?  Why? Is it as random, for instance, as a safe password of 7 2-digit numbers, e.g. 01-00-20-98-43-28-42?  Why or why not?

**48 bits of entropy, since it represents $2^{12^4} = 2^{48}$ uniformly distributed outcomes.  14 digits represents only $10^{14}$ outcomes, for entropy of 46.5**

### Numpy

X. Assume you have a numpy array vals of 10 3-D data points.  Vals has shape (10, 3).   *With a single numpy assignment and no Python loops*, create a numpy array relativeVals of shape (10, 5, 3) comprising 5 columns of points, each a copy of vals. Actually write the code and confirm it works via printing relativeVals.shape and relativeVals.  Submit the code and a run.

**weights = np.repeat(np.reshape(pts, (10, 1, 3)), 5, axis=1)**

X. Now also assume a numpy array "means" of 3-D means of 5 clusters, of shape (5, 3).  Modify your one assignment to relativeVals so each column now represents the difference between the points and the mean point of one of the clusters.

**add " - means"**

