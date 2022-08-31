# Day 2
## Prelim test

 * t({C, D}) =?
 * i({2,4}) = ?
 * t(0) = ?
 * How many yotta-atoms in a mole?  ($6 * 10^{23}$)

## Example 8.3

 * Possible for item in $F^(3)$ to not be prefix of some item in $F^(2)$?

## Association Rules

 * Compute $sup(AB \rightarrow D)$  **Answer: 3**
 * Compute $conf(AB \rightarrow D)$  **Answer: 3/4 = .75**
 * Can conf(X->Y) be greater than 1.0?  Why or why not?

## Brute Force Algorithm
 * Walk through and expalin each step
 * Consider complexity
 * How to improve?  What order would you explore the itemsets?  Why?  Can we trim?
   * This is how you should do reading: question and anticipate
 * Look at lattice
   * How does sup change as you move down?

## Apriori
 * Walk through ComputeSupport for sample itemsets
   * Why is this better?
 * Walk through 
   * Reframe line 19 a bit.  "if for all $X_j \subset X_{ab}...$"
   * What is sup value for eleements of $C^{(k)}$ at start of call?
 * Pick a homework problem or two to analyze

## Python Lab
 * Get Pandas and Numpy installed
 * Pull down zip file
 * Do a Pandas read-in of Orders100.csv and try out a bit of Pandas

## Eclat
 * Look at C version of database.  How do we compute, say, t({B}, t{BC}, t(BCD)..
 * Walk through Eclat
 