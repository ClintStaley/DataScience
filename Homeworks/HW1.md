# Homework 1 Review and Basics

## Readings
Zaki:
Ch 1, 2, 3.1

## Exercises
1. Provide a 3x3 matrix that rotates $\tau/8$ about the z-axis, folllowed by $-\tau/4$ about the y axis.

2. Prove Zaki Eq 2.18, by starting with the right side, and evolving it into the left.  You should need at least 6 steps.\

3. Assume a set of 11 test scores, all between 0 and 100

   a. If the average score is above 90, what is the lowest possible median score? 

   b. If the average score is under 50, what is the highest possible median score? 

   c. If the median is 50, what is the lowest possible mode? 

4. I have an unreliable network provider, and they're down on 10% of days.  In the course of a 365-day year, how likely is it they will be out on exactly 36 of the days?  What number of outage days should I plan for, so that there is a 99.9% chance there won't be more days than that?  Show your work. 

5. Say a 3-D distribution is formed by multiplying independent univariate normal distributions $\mathcal{N}(x|\mu_x, \sigma_x^2)$, $\mathcal{N}(y|\mu_y, \sigma_y^2)$ and $\mathcal{N}(z|\mu_z, \sigma_z^2)$.  Give a single multivariate normal distribution that describes that 3-D distribution, in $\mathcal{N}(X|\Mu, \Sigma)$ form, with X representing $[x,y,z]^T$.  What are the values of $\Mu$ and $\Sigma$?

6. Prove algebraically that your answer for the prior question is correct.

7. Given a 3-dimensional multivariate normal distribution $\mathcal{N}(X|[1, 2, 3]^T, \begin{bmatrix}.417&&-.0589&&.0589
\\-.0589&&.708&&.292\\.0589&&.292&&.708\end{bmatrix})$, what is the conditional distribution taken along the x axis, with y=2 and z=3?  Provide a precise equation for this, using ($\tau$ not $\pi$, this time).

8. Three bags contain colored balls in the proportions below.  I choose from bag 1 10% of the time, from bag 2 40% of the time, and from bag 3 50% of the time.  I choose a ball via this rule, and it's red.  What is the chance it came from bag 2?
  * Bag 1: 10% red, no green, 90% blue
  * Bag 2: 50% red, 25% green, 25% blue
  * Bag 3: 90% red, 5% green, 5%% blue