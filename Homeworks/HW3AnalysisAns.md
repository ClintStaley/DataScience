# Itemset Algorithm Analysis
These questions consider a case where $|\mathcal{I}| = 10,000$, $|\mathcal{D}| = 1,000,000,000$ and each item is 1% likely to appear in any given transaction, with uniform probability independent of any other item.

1. What is the average size of a transaction under this model?

**100**

2. Give an expression for the mean support for an itemset of size k?  What value is this specifically for k=4 and k=5?

**$\frac{1000000000}{100^k}$, so 10 for k=4 and .1 for k=5**

3. Dialing in on the k=4 case, how many possible 4-itemsets are there?

**${10000 \choose 4} = 4.1 x 10^{14}$ 4-itemsets**

4. Let's find a minsup that will filter for interesting 4-itemsets.  Considering the mean support for a 4-itemset you calculated above, and assuming that the relevant binomial distribution is large enough to be approximated by a normal distribution, what minsup would ensure at most 0.01% of 4-itemsets are frequent, if they truly are random?  Show your work.  Since you can only choose an integer, this value should in fact produce an even smaller likelihood.  What is that?

**$\sigma for Bern(.0001) = \sqrt{.9999(.0001)} = .01$\
$\sigma for B(1000000, .0001) = 1000(.01) = 10$\
Need z-sigma of 3.71 or 3.72, so 38 to ensure < .0001, thus **10 + 38 = 48**\
Actually 4 sigmas, so .00003**

5. Assuming k = 4 in ComputeSupport of Apriori, an average size of transaction, and a minsup of the value you just computed, how many itemset comparisons will occur per iteration of line 13?  (Note that the test $if X \in C^{(k)}$ implies an examination of all surviving 4-itemsets, and use the actual survival rate from the prior question)

**Answer: ${100 \choose 4} * 4.1 x 10^{14} * .00003 = 4.8 x 10^{16}$**

6. Reorganize lines 14-15 to first loop through $C^{(k)}$.  Show your code here:

```
foreach $X \in C^{(k)}$ do\
   if $X \subseteq t(i)$ then sup(X)++
```
7. Your reorganized code should include a line doing a subset operation.  How many subset operations per iteration of line 13 when k=4? And, roughly how much more expensive is a subset operation than a 4-set equality operation (which was the "fundamental step" of the prior organization?)  

**Answer: $4.1 x 10^{14} * .00003 = 1.23 x 10^{10}$\
25x as expensive assuming sorted order of items**

8. So, by roughly what factor would reorganizing these lines speed up the algorithm in the case described?

**Answer: $\frac{{100 \choose 4} }{25} = 6,468$**

9. For that same secnario, at what point, if any, would you shift to "difference mode" in eClat/DeClat algorithm case?  Why?

**Pretty much no case.  The number of dropped transactions at each level is 99x the number of undropped**

10. Consider the FPGrowth tree look like for this scenario.\
a) What would the first three or four levels look like?\
b) About how many levels would you expect overall?\
c) How wide could the widest level be at most?\
d) What would you expect, say, level 10 to look like? What support per node? How many children per node?

**a. Top 3-4 levels would have almost, but not quite, 10,000 branches\
b. Widest level would < 1,000,000,000.\
c. Up to around 150 levels, however.\
d. Level 10 would be close to a billion wide, almost all 1-support nodes, with just one child**

