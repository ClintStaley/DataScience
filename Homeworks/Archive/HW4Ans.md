# Storing Itemsets

## Readings
 * Zaki Ch 9

## Exercises


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


