# Data Science Final
<div style="text-align: right">Name ________________________________________</div>

## 1. 40 pts Vocabulary
Give correctly-spelled terms to match the following definitions.

Itemset for which the addition of any item will result in decrease of support **closure**

Itemset for which the addition of any item will result in insufficient support **maximal**

vector defining a dividing hyperplane between classes of data **linear discriminant**

Fraction of correct predictions made by a classifier, on average **accuracy, precision or purity**

Measure of average number of "symbols" needed to transmit a result from a probability distribution **entropy**

If-then rule derived from a supported itemset
**association rule**

proportion of transactions supporting an itemset **relative support**

itemset algorithm that is more efficient when that proportion is generally > .5
**dEclat**

graph topology describing a partial order with clear sinks and sources **lattice**

For X->Y, the likelihood that Y will be in the itemset if X is **confidence**

For itemsets X and Y, the ratio of the likelihood X and Y will appear in an itemset togther, beyond just random chance given their supports. **lift**

Same as the prior, but expressed as a *difference* between likelihoods, not a ratio **leverage**

Itemset for which the two prior terms indicate more than just average likelihood, for all partitions of the itemset **productive**

Name of quantity maximized by the optimal linear discriminant **Fisher LDA**

Bayesian estimation that presumes relevant properties of a sample are independently distributed **naive Bayes**

Equation for logistic function, two forms, one with and one without negative exponents: **$\frac{1}{1+e^{-1}}$, $\frac{e^x}{1+e^x}$**

Additional value added in a categorical naive-Bayes calculation to compensate for missing class/category samples. **pseudo-count**

Classification system that considers nearby points when establishing class means **K-NN**

Bayesian equivalent of the same **EM-clustering**

## 2. 62 pts Data Science Math
### a. 23 pts
A college has these statistics.  What is the chance that a random CSCI major, who we know is not a senior, is a freshman?

|Class | % of all students | % that are CSCI majors |
|--------------|-----------|------------|
| Freshman     | 30    | 4       |
| Sophomore   | 25  | 8       |
| Junior    | 20  | 9       |
| Senior     | 25  | 7       |

**Ans: $P(Fr|CSCI) = \frac{P(Fr \land CSCI)}{P(Fr \land CSCI)+P(So \land CSCI)+P(Jr \land CSCI)} = \frac{.3(.04)}{.3(.04)+.25(.08)+.2(.09)} = .24$**

### b. 15pts 
Provide a 3x3 rotational matrix that rotates the X-axis onto the line (0,1,-1) in the Y-Z plane, and the Y-axis onto the line (0, 1, 1) in that same plane.  (Z axis is deducible from this info).

**Answer: $\begin{bmatrix}0&&0&&-1\\.707&&.707&&0\\-.707&&.707&&0\end{bmatrix}$**

### c. 12pts
Three different test scores have normal distributions of ,$\mathcal{N}(80, 10)$,
$\mathcal{N}(70, 20)$ and $\mathcal{N}(90, 5)$.  What is the distribution of the
product of their score frequencies? Express your answer using $\mathcal{N}(...)$ notation.\
**$\mathcal{N}([80, 70, 90]^T, \begin{bmatrix}10&&0&&0\\0&&20&&0\\0&&0&&5\end{bmatrix})$**

### d. 12pts
A rule X->Y has lift of 10, but leverage of just .09.  What is the smallest number of transactions for which is this possible?  Briefly describe it.  **10 transactions of which 1 contains X and Y, an no others do**

## 3 42pts FPGrowth

### a. 12pts
With reference to Zaki Algorithm 8.5, line 13:  PATH_FROM_ROOT(i) only looks at nodes
in the FPTree from root to the i, not those below i.  But clearly nodes both
above and below i will contribute to itemsets containing i.  Why is this OK, and what
other line in that Algorithm ensures this?  **6pts Lower nodes will already have been considered and put into other subtrees.  6pts Line 8 visiting nodes in increase support order ensures this**

### b. 14pts
The algorithm sorts items by decreasing order of support, both within itemsets before building the original FP-Tree, and also at line 8.  What if two items have the same support?  Can they go in either order in those two lines?  And, could they go in one order when building the FP-Tree, but in the other on line 8, as long as they're addressed in increasing order of support?  Explain your answer carefully.  **4pts They may go in either order, but 4pts the *same* order must apply in both cases, so that the layering of the tree is maintained 6pts**

### c. 16pts
Design a database, with at most 4 transactions, that will cause the initial FP-Tree to have 3 levels, and 7 nodes, but which will result in no calls of line 3 of the FPGrowth algorithm throughout the entire recursion.  How many total calls of FPGrowth will result?  Show the database and the initial tree with frequency counts.  **ABD, ABE, ACD, ACE is an example 10pts.  7 calls will occur 6pts**

## 4 31pts Ukkonen's algorithm

### a. 23pts
Show a string of 5 characters (4 plus final \$) that will cause Ukkonen's algorithm to produce a suffix tree with 5 levels, and for which all but one edge has only one character. Show the resultant tree, including any suffix links. **aaaa$ or equivlent (6pts) results in degenerate tree of single-a and \$ branches (5pts) bottom most having a$ and $ branches (6pts), two suffix links backward in the middle (6pts)**

### b. 8pts
Show a string, including \$, that results in 8 branches from the root, but no suffix links. **abcdefg$ will do it**

## 5. 36pts EM Clustering
All questions with reference to Zaki Algorithm 13.3 and associated material

### a. 10pts
Can $P(C_i)$ be zero for any cluster?  Describe how if so, or explain why this isn't possible. **Not possible (1pt).  Every datapoint contributes some nonzero value to each $P(C_i)$ no matter how distant since the multivariate normal is everywhere > 0 (9pts)**

### b. 16pts
What if n < k? What would you expect $\mu_i$ values to converge to after many steps? Why?\
**8pts $\mu$ values would converge toward points, though not necessarily every point would get a $\mu$.**

And what about $P(C_i)$ values? Again, explain. **4pts $P(C_i)$ values would be proportional to number of congregated points, though always > 0**  

And, what would $w_{ij}$ values look like?  Why? **Nearly 1 or nearly 0 (4pts but only with "nearly")** 

### c. 10pts
Draw a scenario, with distinct 2-D points and n=8, k=2, where all $w_{ij}$ values are equal.  Show the $\mu$ locations, and the point locations.  Is this a stable situation? **Ring of equidistant 8 points around overlapping $\mu$ values (8pts).  Dynamically unstable (2pts)**   


## 6. 59 pts Linear Discriminant Analysis
### a. 12pts
Set up a pair of clusters of 2-D points, such that the mean-difference and optimal linear discriminant are almost 90 degrees opposed, and 1/3 of points are misclassified by the former.
**Any reasonable slanted set like the example I will provide, though *not* collinear!!**

For simplicity in grading, and to save you error and time, present to me your solution, and I'll approve it, and give you an alternate one to analyze instead.  **C1 = {(-6,1), (-2,0), (4,-1)} and c21 = {-4, 1), (2,0), (6,-1)}**

### b. 35pts
Compute the optimal linear discriminant, normalized, showing your work.  Recall that if $ M = \begin{bmatrix}a&&b\\c&&d\end{bmatrix}$, then $M^{-1} = \frac{\begin{bmatrix}d&&-b\\-c&&a\end{bmatrix}}{det(M)}$


**2pt $\mu_1 = [-4, 0]$\
2pt $\mu_2 = [4, 0]$\
4pts$\bar{D}_1 = \begin{bmatrix}-2&&1\\2&&0\\8&&-1\end{bmatrix}$\
4pts$\bar{D}_2 = \begin{bmatrix}2&&-1\\-2&&0\\-8&&1\end{bmatrix}$\
6pts$S_1 = S_2 = \begin{bmatrix}72&&-10\\-10&&2\end{bmatrix}$\
2pts$S_1 + S_2 = \begin{bmatrix}144&&-20\\-20&&4\end{bmatrix}$\
10pts$(S_1+S_2)^{-1} = \begin{bmatrix}.023&&.114\\.114&&.818\end{bmatrix}$\
5pts$w = [.023, .114], w_{norm} = [.198, .98]$**

### c. 12pts
Draw the points, and the normalized W, and give a threshold value for which the optimal linear discriminant correctly divides the classes. **4pts Reasonable drawing.  8pts Threshold of 0**


## 7. 70 pts Linear Regression

### a. 20pts 
In Zaki Figure 23.5, the projections from points onto the plane do not appear to be orthogonal, yet the prior discussion follows an orthogonal projection operation, like the one for bivariate regression in Figure 23.4.  Is this inconsistent?  What are the dimensions of the two spaces shown in those two figures?
**Not inconsistent.  Figure 23.4 is the n-dimensional space across all sample points.  Figure 23.5 is the d-dimensional space of the regression hyperplane.  The orthogonal projection is in the former, not the latter.**

### b. 50pts
Given the data provided as a text file on Canvas, perform a linear regression analysis and predict the missing value for the last 10 points in that text file.  You may use Python, and any code you wrote previously for homeworks.  Copy the missing 10 numbers, to two decimals of accuracy, here.  (Verification hint, the first two should be between 19 and 22 and the final 3 are negative.)

**All or nothing, given all the confirmatory hints\
-1.9708 2.0849 -0.5849 8.1987 19.5638\
3.6419 4.8835 0.3889 7.1235 21.1505\
2.6805 -3.1918 2.9862 6.5189 30.6487\
-7.8500 -6.5191 1.0820 -0.8496 2.1682\
6.2289 -8.1671 0.3267 -0.3835 17.9274\
-2.9571 -3.1570 1.2602 9.7836 30.5493\
8.1656 -5.5417 7.0732 7.9638 48.2268\
-2.7247 4.1660 -5.4911 -1.5461 -14.9927\
5.5008 4.2324 3.7334 -9.2410 -12.2339\
-2.4385 -1.2027 8.0252 -8.2373 -5.7912**


## 8. 50pts Naive Bayes Estimation
Given the following categorical data for several classes of car, what is the likelihood that a red, lo-cost, med-capacity car is a Sedan?  Use categorical naive Bayes classification, with pseudo-counts as necessary (should be four cases).  YUour final answer should be about .518.

|Class | color(red/black/other) | cost(hi/lo) | load capacity(lo/med/hi)
|--------------|-----------|------------|----|
| Sedan     | red    | hi  | hi |
| Sedan     | black  | lo  | med |
| Sedan     | other  | lo  | lo |
| Minivan   | other  | lo  | hi |
| Minivan   | black  | hi  | hi |
| Sports    | red    | hi  | med |
| Sports    | red    | hi  | lo |
| Sports    | other  | lo  | lo |

### a. 20pts
Compute forward probabilities for red, lo-cost, and med-capacity, per class (9 values)


**ANSWER:**
|class|red|lo-cost|med-cap|
|--|--|--|--|
|Sedan|.33|.67|.33|
|Mini|.2|.5|.2|
|Sports|.5|.333|.333|**

### b. 20pts
Perform naive-bayes combination of the above, per class, and determine prior likelihood of each class based on table samples (6 values)

**ANSWER:**
|class|NB|prior|
|--|--|--|
|Sedan|.0741|.375|
|Mini|.02|.25|
|Sports|.0556|.375|**

### c. 10pts
Perform the Bayes estimation using these data (one value, but show work)

**Answer: (8pts) $\frac{.0741(.375)}{.0741(.375)+.02(.25)+.0556(.375)} = \frac{.02778}{.0536} = .518$ (2pts)**