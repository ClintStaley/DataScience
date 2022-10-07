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
**Ch 8 Q2, Q4**

Q2 

Level 1 A|1356, B|23456, C|12356, E|2345

Level 2 (AB|356, AC|1356) (BC|2356, BE|2345), (CE|235)

Level 3 (ABC|356) (BCE|235)

Order of generation: A, AB, ABC, AC, B, BC, BCE BE, C CE, E

Q4

A->BE has confidence 2/4

AB->E has confidence 2/3

AE->B has confidence 2/2

BE->A has confidence 2/4

**Ch 9 Q1, Q2, Q3**

Q1

a. False. Can't provide exact support

b. True

c. True.  Maximal is closed since can't add any element w/o losing support.

d. False.  Could e.g. have A as maximal and BCD maximal, but BC nonmaximal

Q2

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


Frequent: A, B, C, D, E, AB, AC, AD AE, BC, BD, BE, CD, CE, ABC, ABE, ACE, BCE, ABCE

Closed (by root level): AC, B, C, D, BE | ABC, AD, ABCE, BC, BD, CD, BCE

Maximal: BD, AD, CD, ABCE

Q3 (see attached photo)

A, B, C, D, AB, AC, AD, BC, CD, ABC, ACD


### EMC
Ch 2 Ex 1-3

1. Data Prep phase is clearly cited as most time consuming, and text strongly
suggests Model Building is not too time consuming.

2. Reasonable answers are to try out deployment under low-risk situatoin.

3. 
a) Hadoop, Alpine Miner, OpenRefine, Data Wrangler
b) SAS Enterprise Miner, SPSS Modeler, Matlab, Alpine Miner, Statistica,
Mathematica