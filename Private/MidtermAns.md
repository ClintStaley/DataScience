# Data Science Midterm
<div style="text-align: right">Name ________________________________________</div>

**1. 36 pts Vocabulary**\
Give correctly-spelled terms to match the following definitions.

Three alliterative terms describing how "big data" differs from ordinary data\
**volume, variety, velocity**

Prefix meaning $10^{24}$\
**yotta**

Itemset for which the removal of any item will result in increase of support\
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

**2. 10pts Data Science Practice**\
Comment on this statement, with at most 30 words: "Most of the algorithms used in big data analysis are available as libraries, so practical data science involves little coding.  The relevant data is just fed to the library algorithms and we analyze the patterns that result"

**The big coding work is usually data cleaning and organization**

**3. 54pts Data Science math**

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

**f 8pts** Describe the shape of the points at exactly 2 standard deviation distance from the center of a multivariate normal with $\Sigma = \begin{bmatrix}9&&0&&0\\0&&9&&0\\0&&0&&9\end{bmatrix}$ and $\mu = \begin{bmatrix}0&&6&&0\end{bmatrix}$  Is the origin one of the points in this shape? Why or why not?

**Sphere centered at y=6, with radius 6.  Origin is 6 distance from that center, so it's in the shape**


**g 8pts** Assume a probability distribution with 4 possible events, all with probability of at least .01.  What distribution will have the lowest entropy?  What entropy will that be, exactly?  (You may give base-10 entropy if you like; it's easier to do on a typical calculator.)

**(.97, .01, .01, .01) with base-10 entropy of .0728 and base-2 entropy of .242**

**3. 22pts Itemset and Rule Evaluation**
I have a database D with just four transactions. Two of them have both items a and b; the other two have neither.  I wonder if $a\rightarrow b$ is a good rule...

**a. 5pts** What is the lift of $a\rightarrow b$?\
**2**

**b. 5pts** What is the confidence of $a\rightarrow b$\
**1**

**c. 12pts** For what p-value does $a\rightarrow b$ pass a Fisher test of productivity?\

$\frac{2!^4}{2!^2n!} = \frac{2!^2}{4!}=\frac{4}{24}=.1666$

**5. 40pts Charm Algorithm**
Below is a snapshot of Charm from the text.  Construct a 5 transaction database, with as few items as possible, that generates 5 separate closed itemsets assuming a minsup of 0, *and for which the recursive call on line 16 is not executed*.  Show the database, the final contents of $C$, and explain how many times lines 9, 13, and 15 will be executed during the Charm run.

![Charm Algorith](Charm.png)

```









```

**6. 56pts Ukkonen's Algorithm**
Below is a snapshot of Ukkonen's algorithm from the text.  Answer the following questions, tying the visual steps of the algorithm as displayed in our favorite simulation to the lines of the code.

![Ukkonen algorith](Ukkonen.png)

**a. 8pts** How many nodes in the suffix tree, and which ones, might be modified by line 6?

**Leaves will be modified, and this may be up to n.**

**b. 8pts** If your answer to a is not a fixed or limited number, then given that line 6 is inside an O(n) loop, this suggests the algorithm has complexity worse than O(n).  How do you reconcile this with the know O(n) complexity of Ukkonen's?

**"Modification" means adjusting the e value that all leaves use; no actual change to individual leaves is needed**

**c. 8pts** Which line performs the "move the pipe forward" step that we see in the Ukkonen's simulation?

**Line 10 (or line 9/10) does this, by skipping 12-13 and going to the next i value in the outer loop**

**d. 8pts** On what line would we add a suffix link?

**This would occur on line 8, where we will find a new immediate suffix and add a suffix link**

**e. 8pts** The simulation tracks a "remainder" variable.  Write an expression, using the variables of the algorithm pseudocode, that is equivalent to "remainder".

**i-l, and accept off-by-one**

**f. 8pts** Line 8 looks like a bit of a hunt in the tree.  How does the depth of the tree affect the amount of time line 8 will take?  Why?

**No effect since line 8 will not traverse from the root but from an immediate suffix node provided by suffix link**

**g. 8pts** If n = 100, what is the maximum number of times line 10 might execute?  Lines 12-13?  Why?

**Line 10 might run 100 times, but the pipe can only make 100 forward steps in all.  Line 12-13 might run 101 times, but we advance l only 100 times at most.**

**7. EMClusters**\
Below is a snapshot of the EM algorithm from the text.  Answer the following questions regarding it.

![EMClusters Algorithm](EmClusterAlg.png)

**a. 16pts** What range of possible values might these two summations have? Explain your answer for each.

$\sum_{i=1}^{i=k}w_{ij}$  (for various values of j)\

**Always 1, since each point contributes a probability-distrubution resulting from line 8**


$\sum_{j=1}^{j=n}w_{ij}$  (for various values of i)


**Anywhere from nearly zero to n, depending on how much the points like the cluster**

**b. 8pts** Give an intuitive description of the second summation's meaning in the algorithm.

**How "popular" cluster i is**

**c. 8pts** On line 11, what is the dimension of $\Sigma$?  Use variables from the algorithm if possible, or if you make up new ones explain their meaning in terms of variables in the algorithm.

**d x d, with d the dimension of each point in D**

**d. 8pts** How is the $\Sigma$ dimension you gave in part c obtained from what appears to be a summation of dot products?  And, how can we be sure $\Sigma$ is positive definite, or at least symmetrical?

**It's an outer product, and since its the same vector left and right, then** $\Sigma_{ij} = \Sigma_{ji}$

**e. 8pts** What is the order of complexity of *one* iteration of the repeat loop?  You may create one new variable for this, but otherwise use only variables in the code.  Explain your answer.

**Big pole is line 11, which requires k iterations, each summing n outer products, each of which require d*d operations (the vector dimension).  So, O(knd^2)**

**f. 8pts** For this algorithm, how do you think worst-case, average-case, and best-case complexities for one loop-iteration relate? Why?

**Loops are all fixed-range with no options for shortening them.  The three complexities are identical**
