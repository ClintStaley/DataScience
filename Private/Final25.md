# Data Science Final
<div style="text-align: right">Name ________________________________________</div>

## 1. 42 pts Vocabulary
Give correctly-spelled terms to match the following definitions.

Itemset for which the addition of any item will result in decrease of support 

Itemset for which the addition of any item will result in insufficient support 

vector defining a dividing hyperplane between classes of data 

Fraction of correct predictions made by a classifier, on average 

Measure of average number of "symbols" needed to transmit a result from a probability distribution 

Measure of the decrease in entropy resulting from dividing categorized points into two groups 

If-then rule derived from a supported itemset


proportion of transactions supporting an itemset 

itemset algorithm that is more efficient when that proportion is generally > .5


graph topology describing a partial order with clear sinks and sources 

For X->Y, the likelihood that Y will be in the itemset if X is 

For itemsets X and Y, the ratio of the likelihood X and Y will appear in an itemset togther, beyond just random chance given their supports.

Same as the prior, but expressed as a *difference* between likelihoods, not a ratio 

Name of quantity maximized by the optimal linear discriminant 

Bayesian estimation that presumes relevant properties of a sample are independently distributed 

Itemset for which the two prior terms indicate more than just average likelihood, for all partitions of the itemset 

Equation for logistic function, two forms, one with and one without negative exponents: 

Additional value added in a categorical naive-Bayes calculation to compensate for missing class/category samples. 

Classification system that considers nearby points when establishing class means 

Bayesian equivalent of the same 

## 2. 62 pts Data Science Math
### a. 23 pts
A college has these statistics.  What is the chance that a random CSCI major, who we know is not a senior, is a freshman?

|Class | % of all students | % that are CSCI majors |
|--------------|-----------|------------|
| Freshman     | 30    | 4       |
| Sophomore   | 25  | 8       |
| Junior    | 20  | 9       |
| Senior     | 25  | 7       |

```





```

### b. 15pts 
Provide a 3x3 rotational matrix that rotates the X-axis onto the line (0,1,-1) in the Y-Z plane, and the Y-axis onto the line (0, 1, 1) in that same plane.  (Z axis is deducible from this info).
```




```
### c. 12pts
Three different test scores have normal distributions of ,$\mathcal{N}(80, 10)$,
$\mathcal{N}(70, 20)$ and $\mathcal{N}(90, 5)$.  What is the distribution of the
product of their score frequencies? 

### d. 12pts
A rule X->Y has lift of 10, but leverage of just .09.  What is the smallest number of transactions for which is this possible?  Briefly describe them.  
```


```
## 3 42pts FPGrowth

### a. 12pts
With reference to Zaki Algorithm 8.5, line 13:  PATH_FROM_ROOT(i) only looks at nodes
in the FPTree from root to the i, not those below i.  But clearly nodes both
above and below i will contribute to itemsets containing i.  Why is this OK, and what
other line in that Algorithm ensures this?  

### b. 14pts
The algorithm sorts items by decreasing order of support, both within itemsets before building the original FP-Tree, and also at line 8.  What if two items have the same support?  Can they go in either order in those two lines?  And, could they go in one order when building the FP-Tree, but in the other on line 8, as long as they're addressed in increasing order of support?  Explain your answer carefully.  
```



```
### c. 16pts
Design a database, with at most 4 transactions, that will cause the initial FP-Tree to have 3 levels, and 7 nodes, but which will result in no calls of line 3 of the FPGrowth algorithm throughout the entire recursion.  How many total calls of FPGrowth will result?  Show the database and the initial tree with frequency counts.  

```


```

## 4 35 pts Ukkonen's algorithm

### a. 23pts
Show a string of 5 characters (including final $) that will cause Ukkonen's algorithm to produce a suffix tree with 5 levels, and for which each edge has only one character. Show the resultant tree, including any suffix links.

```



```

### b. 12pts
Show a string, including $, that results in 8 branches from the root, but no suffix links. 


## 5. 36pts EM Clustering
All questions with reference to Zaki Algorithm 13.3 and associated material

### a. 10pts
Can $P(C_i)$ be zero for any cluster?  Describe how if so, or explain why this isn't possible. 

### b. 16pts
What if n < k? What would you expect $\mu_i$ values to converge to after many steps? Why?
```


```
And what about $P(C_i)$ values? Again, explain. 
```

```
And, what would $w_{ij}$ values look like?  Why? 
```


```
### c. 10pts
Draw a scenario, with distinct 2-D points and n=8, k=2, where all $w_{ij}$ values are equal.  Show the $\mu$ locations, and the point locations.  Is this a stable situation?
```







```

## 6. 59 pts Linear Discriminant Analysis
### a. 12pts
Set up a pair of clusters of 2-D points, such that the mean-difference and optimal linear discriminant are almost 90 degrees opposed, and 1/3 of points are misclassified by the former.

For simplicity in grading, and to save you error and time, present to me your solution, and I'll approve it, and give you an alternate one to analyze instead. 

### b. 35pts
Compute the optimal linear discriminant, normalized, showing your work.  Recall that if $ M = \begin{bmatrix}a&&b\\c&&d\end{bmatrix}$, then $M^{-1} = \frac{\begin{bmatrix}d&&-b\\-c&&a\end{bmatrix}}{det(M)}$


$\mu_1= $\
$\mu_2= $\
$\bar{D}_1 = $\
$\bar{D}_2= $\
$S_1 + S_2 = $\
$(S_1+S_2)^{-1} =$

normalized w =

### c. 12pts
Draw the points, and the normalized W, and give a threshold value for which the optimal linear discriminant correctly divides the classes.
```







```
## 7. 70 pts Linear Regression

### a. 20pts 
In Zaki Figure 23.5, the projections from points onto the plane do not appear to be orthogonal, yet the prior discussion follows an orthogonal projection operation, like the one for bivariate regression in Figure 23.4.  Is this inconsistent?  What are the dimensions of the two spaces shown in those two figures?
```




```
### b. 50pts
Given the data provided as a text file on Canvas, perform a linear regression analysis and predict the missing value for the last 10 points in that text file.  You may use Python, and any code you wrote previously for homeworks.  Copy the missing 10 numbers, to two decimals of accuracy, here.  (Verification hint, the first two should be between 19 and 22 and the final 3 are negative.)

```


```

## 8. 50pts Naive Bayes Estimation
Given the following categorical data for several classes of car, what is the likelihood
that a red, lo-cost, med-capacity car is a Sedan?  Use categorical naive Bayes classification, with pseudo-counts as necessary.

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
```



```
### b. 20pts
Perform naive-bayes combination of the above, per class (3 values)
```


```
### c. 10pts
Perform the Bayes estimation using these data (one value, but show work)