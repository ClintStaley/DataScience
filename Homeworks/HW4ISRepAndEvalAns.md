# Itemset Representation and Evaluation

## Readings
Zaki
  * Chapter 9.1 - 9.3
  * Chapter 12 through page 317 (minus Odds Ratio)

## Exercises

1. Zaki Ch 9 Q1

**a. False. Can't provide exact support\
b. True\
c. True.  Maximal is closed since can't add any element w/o losing support.\
d. False.  Could e.g. have A as maximal and BCD maximal, but BC nonmaximal**

2. Zaki Ch 9 Q2
For 2b, specify Frequent, closed, and maximal in the order they appear in
the tree, level by level, left to right, with a pipe symbol between each level.  You should have 20 frequent, 12 closed, and 4 maximal sets.

```
a. C(AE) = ABCE, so AE is not closed

b. See diagram on paper.  Note support groups are:

356 AB ABC
1356 A AC
23456 B
35 AE ABE ACE ABCE
123456 C
2356 AC
146 D
46 BD
2345 E BE
16 AD CD 
235 CE BCE


Frequent: A, B, C, D, E | AB, AC, AD, AE, BC, BD, BE, CD, CE | ABC, ABE, ACD, ACE, BCE | ABCE

Closed (by root level): B, C, D | AC, BC, BD, BE, CD | ABC, ACD, BCE | ABCE

Maximal: BD | ACD | ABCE
```


3. Zaki Ch 9 Q3

**(see attached photo)
A, B, C, D, AB, AC, AD, BC, CD, ABC, ACD**

4. For a rule X -> Y, describe a situation that would give a confidence of 1, but only a lift of 1.  What is the leverage in this case?

**Regardless of X, Y occurs in all itemsets.  Leverage would be 0**

5. For a rule X -> Y with confidence .5, what are the largest possible values for rsup(X) and rsup(Y)?  What are lift and conviction in this case?

**rsup(X) can be 1.0; rsup(Y) would be at most .5.  Lift and conviction are both 1.0**

6. For a rule X->Y, what does a confidence of 1.0, with a lift of 100, but a leverage of less than .01 signify?  Give rsup values that would result in this case:

**Strong correlation but light support.  rsup(X) = rsup(Y) = .01 would do this if X and Y are exactly correlated.**

7. Describe the support structure and partition for an itemset ABCD minLift is 1 but maxLift is 4.  Is such an itemset productive?  Why or why not?

**Half have AB; half don't.  Ditto CD, and AB and CD are uncorrelated.  rsup(ABCD) is thus .25.  Lift of, say, AC -> BD is 4, while lift of AB->CD = 1.  Not productive as at least one partition has lift of just 1.**
