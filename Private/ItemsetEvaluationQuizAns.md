# Itemset Evaluation Quiz #

<div style="text-align: right">Name ________________________________________</div>

You may use our text for referenc.  No calculator as the computations in question are quite simple.

1. 12pts Given an association rule $xy \rightarrow Z$  with an two-item antecedent, find a minimally-sized set of transactions for which you can prove, with p-value $\le$ .05, that y is productive via the Fisher test.  You may confirm your result with me before proceeding with the next steps.  You should need less than 8 transactions.

**6 transactions, three with xyZ and three with x$\neg$Z will do this.  Table 
is below, with probability $\frac{3! 3!}{6!} = .05.**

```
x       Z  not Z
y       3     0
not y   0     3
```

2. 8pts Given your transaction set from question 1, what would be the confidence, lift, leverage, conviction, odds-ratio and Jaccard of the $xy \rightarrow Z$ rule?

 * **Confidence is 1.0.  xy always appears with Z, never without**
 * **Lift = .5 / .5 * .5 = 2**
 * **Leverage = .25**
 * **Conviction = infinite**
 * **Jaccard = 1**
 * **odds-ratio = infinite**

3. 10pts Extra credit
Develop a minimal transaction set for which you can prove that the entire $xy\rightarrowZ$ association rule is productive per Fisher test at p = .05.

**Need an extra three transactions wity y$\negZ$.  Each table, with x and then y under test, leaving the other antecedent assumed, thus includes only 6 transactions, and looks just like the one above.**
