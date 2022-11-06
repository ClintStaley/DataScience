# Data Science Midterm
<div style="text-align: right">Name ________________________________________</div>

**1. 36 pts Vocabulary**\
Give correctly-spelled terms to match the following definitions.

Three alliterative terms describing how "big data" differs from ordinary data

Prefix meaning $10^{24}$

Itemset for which the removal of any item will result in increase of support

Type of matrix that describes a orthogonally rotated scaling

Metric using ratio of the joint likelihood of two events to the product of their independent likelihoods

Metric using ratio of likelihood of $X\rightarrow Y$ to likelihood of X alone

Metric using ratio of intersection to union

A common name for L-1 norm

Optimization method that mimics a ball rolling down hill on a cost surface.

Statistical test that builds on a hypergeometric distribution

Itemset that cannot be made larger without losing support

Itemset that cannot be made larger without its support dropping below the threshold

Kind of attribute that "favorite color" would be

Kind of attribute that "grade level" would be

An association rule for which removal of any antecedent item results in loss of confidence

A tree structure that improves on a trie by labelling branches by strings, not just characters

**2. 10pts Data Science Practice**\
Comment on this statement, with at most 30 words: "Most of the algorithms used in big data analysis are available as libraries, so practical data science involves little coding.  The relevant data is just fed to the library algorithms and we analyze the patterns that result"
```




```

**3. 72 pts Data Science Math**

**a. 8pts** The angle in radians between vectors [2, 4, 1, 2] and [4, 2, 2, 1]


**b. 4pts** The L-1 norm distance between those same two vectors\


**c. 10pts** Adjust the projection formula below so it gives the projection of b along a in simple length. (E.g. so a value of of 2 means b's projection onto a is 2 units long)

$\frac{b^Ta}{a^Ta}$


**d. 16pts** Write a matrix representing a $\frac{\pi}{4}$ or $45\degree$ clockwise rotation around the X axis (Z and Y axis both move toward you)
```



```

**e. 18pts** Three models of cars are shown below, each with a popularity and a likelihood of being in the shop for repairs.  If a car is in the shop, what is the chance it's a model X?  Show work.

|Model|Popularity|Repair frequency|
|---|---|---|
|X|50%|2%|
|Y|30%|4%|
|Z|20%|5%|
```





```
**f 8pts** Describe the shape of the points at exactly 2 standard deviation distance from the center of a multivariate normal with $\Sigma = \begin{bmatrix}9&&0&&0\\0&&9&&0\\0&&0&&9\end{bmatrix}$ and $\mu = \begin{bmatrix}0&&6&&0\end{bmatrix}$  Is the origin one of the points in this shape? Why or why not?
```


```

**g 8pts** Assume a probability distribution with 4 possible events, all with probability of at least .01.  What distribution will have the lowest entropy?  What entropy will that be, exactly?  (You may give base-10 entropy if you like; it's easier to do on a typical calculator.)
```






```
**4. 28 pts Itemset and Rule Evaluation**\
Consider a database D with just four transactions. Two of them have both items a and b; the other two have neither a nor b.  Evaluate rule $a\rightarrow b$

**a. 6pts** What is the lift of $a\rightarrow b$?\


**b. 6pts** What is the confidence of $a\rightarrow b$\

**c. 16pts** For what p-value does $a\rightarrow b$ pass a Fisher test of productivity (Show your work on this one)?
```








```
**5. 50 pts Charm Algorithm**\
Below is a snapshot of Charm from the text.  Construct a 5 transaction database, with as few items as possible, that generates 5 separate closed itemsets assuming a minsup of 0, *and for which the recursive call on line 16 is not executed*.  Show the database, the final contents of $C$, and explain how many times lines 9, 13, and 15 will be executed during the Charm run.

![Charm Algorith](Charm.png)

```












```

**6. 56 pts Ukkonen's Algorithm**\
Below is a snapshot of Ukkonen's algorithm from the text.  Answer the following questions, tying the visual steps of the algorithm as displayed in our favorite simulation to the lines of the code.

![Ukkonen algorith](Ukkonen.png)

**a. 8pts** How many nodes in the suffix tree, and which ones, might be modified by line 6?
```



```
**b. 8pts** If your answer to a is not a fixed or limited number, then given that line 6 is inside an O(n) loop, this suggests the algorithm has complexity worse than O(n).  How do you reconcile this with the know O(n) complexity of Ukkonen's?
```



```
**c. 8pts** Which line performs the "move the pipe forward" step that we see in the Ukkonen's simulation?
```



```
**d. 8pts** The algorithm describes where suffix links are used, but not where they're added.  On what line would we add a suffix link?  Why?
```



```
**e. 8pts** The simulation tracks a "remainder" variable.  Write an expression, using the variables of the algorithm pseudocode, that is equivalent to "remainder".
```

```
**f. 8pts** Line 8 looks like a bit of a hunt in the tree.  How does the depth of the tree affect the amount of time line 8 will take?  Why?
```




```
**g. 8pts** If n = 100, what is the maximum number of times line 10 might execute?  Lines 12-13?  Why?
```



```
**7. 60 pts EMClusters Algorithm**\
Below is a snapshot of the EM algorithm from the text.  Answer the following questions regarding it.

![EMClusters Algorithm](EmClusterAlg.png)

**a. 18pts** What range of possible values might these two summations have? Explain your answer for each.

$\sum_{i=1}^{i=k}w_{ij}$  (for various values of j)\
```



``````
$\sum_{j=1}^{j=n}w_{ij}$  (for various values of i)
```



```
**b. 6pts** Give an intuitive description of the second summation's meaning in the algorithm.
```

```
**c. 8pts** On line 11, what is the dimension of $\Sigma$?  Use variables from the algorithm if possible, or if you make up new ones explain their meaning in terms of variables in the algorithm.
```

```
**d. 10pts** How is the $\Sigma$ dimension you gave in part c obtained from what appears to be a summation of dot products?  And, how can we be sure $\Sigma$ is positive definite, or at least symmetrical?
```


```
**e. 10pts** What is the order of complexity of *one* iteration of the repeat loop?  You may create one new variable for this, but otherwise use only variables in the code.  Explain your answer.

```



```
**f. 8pts** For this algorithm, how do you think worst-case, average-case, and best-case complexities for one loop-iteration relate? Why?
```



```
