# Naive Bayes Classification
<div style="text-align: right">Name __________________________________________</div>

1. 30pts\
The following table of data for Titanic survivors gives age and gender for 5 people,
along with a Y/N value for survival.  Based on this, build a naive Bayesian model
that predicts survival based on age and gender.  (Note this means a pseudocount for M and F
values in both classes and thus denominators of 5 and 4 in the categorical probabilities.)
Compute the likelihood of survival and nonsurvival for a 30 year old male under your model.


age|gender|survived
---|---|---
25|M|N
35|F|Y
5|F|Y
50|M|N
5|M|Y

## Survive = Y (8 pts)
### Age
$\mu = \frac{35+5+5}{3}=15$
$\sigma = \sqrt{\frac{20^2+10^2+10^2}{3}}=14.14$

### Gender
P(M|Y) = 2/5
P(F|Y) = 3/5

## Survive = N (8 pts)
### Age
$\mu = \frac{25+50}{2}=37.5$
$\sigma = \sqrt{\frac{12.5^2+12.5^2}{2}}=12.5$

### Gender
P(M|N) = 3/4
P(F|N) = 1/4

## Overall (2 pts)
P(Y) = 3/5, P(N) = 2/5

## P(Y|M, age=30)  (10pts)

P(Y|M, age=30)
= $\frac{(P(30|Y)*P(M|Y)*P(Y)}{P(30|Y)*P(M|Y)*P(Y)+(P(30|N)*P(M|N)*P(N)}$
= $\frac{f_y(30)(.4)(.6)}{f_y(30)(.4)(.6)+f_n(30)(.75)(.4)}$
= $\frac{(.0161)(.4)(.6)}{(.0161))(.4)(.6)+(.0267)(.75)(.4)}$
= $\frac{.00387}{.00387+.00802} = .326$