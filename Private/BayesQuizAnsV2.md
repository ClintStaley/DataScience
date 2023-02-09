# Naive Bayes Classification
<div style="text-align: right">Name __________________________________________</div>

1. 30pts\
The following table of data for Titanic survivors gives age and gender for 5 people,
along with a Y/N value for survival.  Based on this, build a naive Bayesian model
that predicts survival based on age and gender.  (Note this means a pseudocount for M and F
values in one (though not both) classes and thus denominators of 3 and 4 in the categorical probabilities.)
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
P(M|Y) = 1/3
P(F|Y) = 2/3

## Survive = N (8 pts)
### Age
$\mu = \frac{30+50}{2}=40$
$\sigma = \sqrt{\frac{10^2+10^2}{2}}=10$

### Gender
P(M|Y) = 3/4
P(F|Y) = 1/4

## Overall (2 pts)
P(Y) = 3/5, P(N) = 2/5

## P(Y|M, age=30)  (10pts)

P(Y|M, age=30)
= $\frac{f_y(30)(.333)(.6)}{f_y(30)(.333)(.6)+f_n(30)(.75)(.4)}$
= $\frac{(.0161)(.333)(.6)}{(.0161))(.333)(.6)+(.0242)(.75)(.4)}$
= $\frac{.00322}{.00322+.00726} = .307$