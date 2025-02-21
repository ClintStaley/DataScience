# Python Analysis of Normal Distributions
## Readings
 * Zaki Ch 8

## Questions

1. Zaki Ch8 Q2\
Draw a diagram of the tree, or for text format, list each level giving itemset|tidset for each node left to right, e.g. AB|123.  Within a level, parenthesize sibling groups of nodes.
Along with diagram, list frequent itemsets in order of addition to $\mathcal{F}$



2. Zaki Ch 8 Q4\
Give each rule in form X->X, along with its confidence, in descending order of confidence.


### Questions 3 through 6 pertain to Aprior code in Zaki Algorithm 8.2

3. On line 18, might $|X_{ab}| \neq k+1$? If so, is this a problem? If not, why not, since it's a union of two different sets each with size k and thus might have size up to 2k?


4. What would bad thing would happen if we omitted the  $b > a$ qualfier on line 17? 

5. In what way, if any, does the algorithm fail if we omit the line 19 check and simply execute line 20 unconditionally?

6. Removal of all ancestors of $X_a$ on line 22 seems like an error because it makes those (well-supported) higher subsets unavailable for other subsets to use in checking on line 19, perhaps making them look as though they have an infrequent subset when they don't. Is this a problem? Why or why not?


### Questions 7 through 11 pertain to Eclat code in Zaki Algorithm 8.3 and the deClat code in Algorithm 8.4

7. What is the smallest and largest calls that might be made on line 9, by a given subcall of EClat?  Express your answer in terms of $|P|$, and be exact.


8. On that same line 9, might $|P_a| == |P|$, and thus result in an endless recursion?  Why or why not?



9. On line 6 of dEclat, could $d(X_{ab})$ be larger than $d(X_a)$? How about larger than $d(X_b)$? Why? 



10. In the discussion of the dEclat algorithm, the text suggests starting with tidsets a la' Eclat, and converting to diffsets partway through. This would require computing $d(X_{ab}))$ from $t(X_a)$ and $t(X_b)$ on line 6 of the dEclat algorithm. If we know only $t(X_a)$  and $t(X_b)$ , give a set-algebra equation for $d(X_{ab})$.


11. Consider line 7 in dEclat, where we compute $sup(X_{ab})$. If we're trying to subtract the transactions lost from $X_a$ by adding item b, why don't we subtract $|d(X_b)|$, since that's the set of supporting transactions lost by adding item b?



### Questions 12 through 16 pertain to the FPGrowth code in Zaki Algorithm 8.5

12. Why is ordering the items correctly when building a prefix-tree such a big deal? Build a database with at most 5 transactions and 5 items for which the original ordering of the items within the transactions produces a prefix tree with 3 times as many nodes than does the prefix tree derived from an optimal item ordering.  Draw the trees.

13. Does the order of the transactions (as opposed to that of the items) affect the form of the final prefix tree? Why or why not?

14. In line 11 of FPGrowth, we clearly add a frequent itemset, but I thought we did this only when the tree was degenerate, so we could systematically find all itemsets without dealing with branches.  What is line 11 adding, and why?

15. Does line 3 in FPGrowth include the empty set as a subset of R?  If so, what value is used for the min operation on line 5? 

16. Provide a D with at least three items and three transactions, for which the if statement on line 2 of FPGrowth will never be true.  Show the resultant initial tree, and explain why line 2 will never be run.


