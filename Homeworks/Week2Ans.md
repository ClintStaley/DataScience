# Week 2 Itemsets Cont

## Readings
Zaki
  * Chapter 9.1-9.2 by classtime Wedn
  * Chapter 9.3, and 1.3.2-1.3.4 by classtime Friday
EMC 
  *Chapter 2 by classtime Monday

## Exercises
All due Monday 2:20p 9/12

### Zaki
Ch 8 Q2, Q4

Q2 
Level 1 A, B, C, D, E
Level 2 (AB|356, AC|1356) (BC|2356, BE|2345), (CE|235)
Level 3 (ABC|356) (BCE|235)

Order of generation: A, AB, AC, ABC, BC, BE, BCE, CE

Q4
A->BE has confidence 2/4
AB->E has confidence 2/3
AE->B has confidence 2/2
BE->A has confidence 2/4

Ch 9 Q1, Q2, Q3, Q4

Q1
a. False. Can't provide exact support
b. True
c. True.  Maximal is closed since can't add any element w/o losing support.
d. False.  Could e.g. have A as maximal and BCD maximal, but BC nonmaximal

Q2
a. C(AE) = ABCE, so AE is not closed
b. 
Frequent: A, B, C, D, AB, AC, AD, BC, BD, CD, ABD, ACD, BCD
Closed: A, C, D, BCD, ABD, AC, AD, ACD, CD
Maximal: ABD, ACD, CBD

Q3
A, B, C, D, AB, AC, AD, BD, CD, ACD, BCD, ABCD


### EMC
Ch 2 Ex 1-3

1. Data Prep phase is clearly cited as most time consuming, and text strongly
suggests Model Building is not too time consuming.

2. Reasonable answers are to try out deployment under low-risk situatoin.

3. 
a) Hadoop, Alpine Miner, OpenRefine, Data Wrangler
b) SAS Enterprise Miner, SPSS Modeler, Matlab, Alpine Miner, Statistica,
Mathematica