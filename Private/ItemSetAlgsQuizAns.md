# ItemSet Algorithms Quiz
<div style="text-align: right">Name __________________________________________</div>


**1. 12pts** In DeClat, if $d(X_{ab}) = \emptyset$ on line 6, what conclusion
can we reach regarding the respective closures of $X_a$ and $X_{ab}$?  Of
$X_b$ and $X_{ab}$? Justify your conclusion.

**Addition of $X_b$ to $X_a$ loses no support, so $X_a$ and $X_{ab} have the
same support and the same closure.  However $X_b might have had more support
than $X_a$, so its closure is a superset of $X_ab$**

**2. 20pts** In FPGrowth, assume $|R| = 5$ in the loop on line 3.

a. 5pts How many times will the loop execute? 

**31, since the emptyset doesn't count**

b. 5pts Does $|X| = |P| + |Y|$ on line 4?  If not, how small might $|X|$ be? 
If so, why, since set union doesn't guarantee this?

**Yes, because P and R are disjoint since P is a prefix and R and thus Y 
comprise only items not in P**

c. 10pts If the loop executes for $Y = \emptyset$, as would be implied by the $\subseteq$ operation, how is $sup(X)$ on line 5 determined?  If not, then how is P added to $\mathcal{F}$?

**$\emptyset$ is not included.  P is added prior to the current recursive call,
on line 11**



