# Week 4 Itemset and Association Rule evaluation

## Readings
Zaki
  * Chapter 12 through page 322

## Exercises

### Zaki
 
1. The Fisher test is usually described as a computation of the likelihood of 
the value in upperleft cell "a" on the assumption that the two columns 
(e.g. "men" and "women") have the same distribution.  But, it can also be
viewed as the probability of value "a" assuming the two *rows* have the same
distribution.  Prove this by the following steps:

 * Start with the standard left-column based hypergeometric distribution.  Do some algebra to merge the three choose functions into to a *single* fraction with multiple factorials in both the numerator and denominator.
 * Write the top-row based hypergeometric distribution that results from a "rows have the same distribution" interpretation, and resolve it similarly to a single fraction.
 * Show that the two fractions are the same.

2. Assume a rule X -> Y, where X is a one-member antecedent, and a support of just 1 for that rule.  Design a *minimal* set of transactions for which this rule would be considered productive under a Fisher test standard with p of .01.  Does it make intuitive sense for the rule to be considered productive under that set?  Why or why not?

3. (You may want to confirm your #2 answer with me first, here).  For your transaction set in #2, What would be the confidence, lift, leverage, conviction, odds-ratio and Jaccard of the X->Y rule?  For the entire itemset XY what is its lift value?  Its $lift_2$ value?  Is the entire itemset productive according to the text definition of itemset productivity?

4. Redo exercise 2 assuming a support of 2 for the X->Y rule.

5. (You may want to confirm your #4 answer with me here.)  Redo exercise 3, for the rule and transactions from exercise 4.