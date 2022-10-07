# Week 4 Itemset and Association Rule evaluation

## Readings
Zaki
  * Chapter 12 through page 322

## Exercises

### Zaki
 
1. The Fisher test is usually described as a computation of the likelihood of the value in upperleft cell "a" on the assumption that the two columns 
(e.g. "men" and "women") have the same distribution.  But, it can also be
viewed as the probability of value "a" assuming the two *rows* have the same
distribution.  Prove this by the following steps:

 * Start with the standard left-column based hypergeometric distribution.  Do some algebra to merge the three choose functions into to a *single* fraction with multiple factorials in both the numerator and denominator.
 * Write the top-row based hypergeometric distribution that results from a "rows have the same distribution" interpretation, and resolve it similarly to a single fraction.
 * Show that the two fractions are the same.

**Pretty straightforward math easy to check**

2. Assume a rule X -> Y, where X is a one-member antecedent, and a support of just 1 for that rule.  Design a *minimal* set of transactions for which this rule would be considered productive under a Fisher test standard with p of .01.  Does it make intuitive sense for the rule to be considered productive under that set?  Why or why not?

**A = 1, B = 0, C = 0, D = 99 will do it.  This gives $\frac{1! 99! 1! 99!}
{1! 0! 0! 99! 100!} = .01$  And even though the positive form of the rule appears only once, Y appears only with X, and appears not at all in 99 other cases**

3. (You may want to confirm your #2 answer with me first, here).  For your transaction set in #2, What would be the confidence, lift, leverage, conviction, odds-ratio and Jaccard of the X->Y rule?  For the entire itemset XY what is its lift value?  Its $lift_2$ value?  Is the entire itemset productive according to the text definition of itemset productivity?

**1 transaction with XY and 99 with neither X or Y.  Arbitrary other properties.**  
 * **Confidence is 1.0.  X only appears once**
 * **Lift = .01 / .01 * .01 = 100**
 * **Leverage = .0099**
 * **Conviction = infinite**
 * **Jaccard = 1**
 * **odds-ratio = infinite**

4. Redo exercise 2 assuming a support of 2 for the X->Y rule.

**A = 2, B = 0, C = 0, D = 13 will do it.  This gives $\frac{2! 13! 2! 13!}
{2! 0! 0! 13! 15!} = .0095$  Even though the positive form of the rule appears only twice, Y appears only with X, and appears not at all in 13 other cases, though interestingly it takes a lot fewer negative cases to make the X productive**


5. (You may want to confirm your #4 answer with me here.)  Redo exercise 3, for the rule and transactions from exercise 4.

**2 transactions with XY and 13 with !X!Y.  Arbitrary other properties.**
 * **Confidence remains 1.0**
 * **Lift = 15/2 = 7.5**
 * **Leverage = 2/15 - 4/225 = 26/225 = .116**
 * **Conviction = still infinite**
 * **Jaccard = 1**
 * **odds-ratio = infinite**