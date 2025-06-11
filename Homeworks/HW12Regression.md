# Linear and Logistic Regression

## Readings
Zaki Chapter 23.1 - 23.3 (but not 23.3.1), Ch 24

## Problems

1. Zaki Ch 23 Ex 1

2. Zaki Ch 24 Q2

3. Zaki Ch 24 Q3

4. Devise 2 4-input sets of values for the softmax function that will cause it to output .5, .25, .125, and .125.  One must be all positive, and the other all negative.  Generalize to a functional form, where you provide an function for each of the four values, with a single parameter X shared across all four equations, that will result in the given output distribution.  *Don't do this by cut and try.  You can arrive at a solution with one natural log computation, and a bunch of additions otherwise.*

5. At the bottom of p 589, Zaki states that $\omega$ is the normal to the hyperplane in $R^{d+1}$ formed by  $f(X)$, but $\omega$ hasn't got the right dimension to be such a normal.  What is the dimension of $\omega$ and what is *actually* the normal to the hyperplane specified. (Assume the dimension supplied by f(X) is the final dimension.)

6. In Figure 23.5, the projections from points onto the plane do not appear to be orthogonal, yet the prior discussion follows an orthogonal projection operation, like the one for bivariate regression in Figure 23.4.  Is this inconsistent?  What are the dimensions of the two spaces shown in those two figures?

7. Write a program that inputs a data file of rows, each with a real Y value followed by a 5-D vector of real attributes.  The program performs a multivariate linear regression on that data, and prints the 6 coefficients (y and 5 attribute factors) that result. Then, write a second program that takes a similar file, and outputs the predicted Y values for the rows of that file, computing a MSE error
between the preducted Y values and the actual ones from the file.  Output the predicted Y values, and the MSE.

```
Example Runs:
python TrainMVRegress.py TrainRegress.tsv
Regression plane offset and coeffs: 99.9938 0.9984 2.0008 3.0000 3.9998 4.9961
python TestMVRegress.py 99.9938 0.9984 2.0008 3.0000 3.9998 4.9961 TestRegress.tsv
Estimated Y values: 
78.21452649999999
107.22397814000001
111.13996585999998
170.70482622
.....
97.42695315
82.77196253
MSE: .01363
```

8. Do the same as problem 7 but for files of rows with the first column indicating
a class to which the point on that row belongs, with classes numbered from 0 to
C-1.  (Determine C from the file)  Write a file of C rows, each giving a 6-D 
w vector for the relevant class.  Importantly, do this by true gradient descent,
meaning one gradient step per epoch, not per data point like the text. And,
do this with just one loop that repeats the gradient steps (essentially the repeat
loop in Zaki Algorithm 24.2), with all gradient computation and application done
by Numpy calls alone.  Your program accepts commandline arguments giving the
training data, the output file for the weights, and the learning rate $\eta$, the max
iterations, and the $\epsilon$ target difference between successive weight values.
Report the error as it changes per epoch
Experiment with different learning rates, and report what you learn.  

Write a second program that takes a second file with the same 
structure as the first, and the weight file from the first, and uses the 
w values to perform a
multiclass logistic regression, comparing the class resulting from the logistic
regression to the class given in the file, which is the correct value.  
Output a CxC dimension confusion matrix, which must have at least 87.5% correct
values.

Example runs:
```
python TrainMVLog.py TrainMVLog.tsv MVWeights.tsv .0005 400 1e-6
Computing weights...
Epoch 0: MSE = 0.001693
Epoch 1: MSE = 0.000627
Epoch 2: MSE = 0.000306
Epoch 3: MSE = 0.000184
Epoch 4: MSE = 0.000125
Epoch 5: MSE = 0.000091
.....
Epoch 312: MSE = 0.000001
Epoch 313: MSE = 0.000001
Epoch 314: MSE = 0.000001
Epoch 315: MSE = 0.000001
Epoch 316: MSE = 0.000001
Epoch 317: MSE = 0.000001
Epoch 318: MSE = 0.000001
Epoch 319: MSE = 0.000001
Epoch 320: MSE = 0.000001
Converged after 320 iterations.

cat MVWeights.tsv
0 2.3 4.3.2.1.-9.1 3.2
5 2.4 -9.0 12.0 0.1 -.2
....

python TestMVLog.py MVWeights.tsv
Confusion Matrix:
[[17  0  0  1  0  0  0  0]
 [ 1  4  1  0  0  0  0  0]
 [ 1  1 63  0  1  2  0  1]
 [ 0  0  0 21  2  0  1  0]
 [ 0  0  0  0 31  0  1  1]
 [ 0  0  1  0  0 13  0  0]
 [ 1  0  0  3  0  0 17  0]
 [ 2  0  1  0  0  0  0 12]]

```

9. Under multiclass logistic regression, what is $\tilde{w}_K^t$ for all values of t?  Why? What if we specifically set $\tilde{w}_K^t = (1,....1)$ instead?  (Just that specific value, on line 6, changing no others)  What effect would this have on the final values of $\tilde{w}_j after training is complete.  Reason from your understanding of how the weight vectors relate under the algorithm.  What effect would this have on the classifications done by the algorithm after training?

10. Just after Eq 24.17, Zaki says "When K = 2, this formulation yields exactly the same model as in binary logistic regression.  Show that this is so.  In particular, if we interpret Eq as a form of Eq 24.17, what will $w_0$ and $w_1$ be?  Show that with these w values, Eq 24.4 for Y=0 and Y=1 resolves to Eq 24.17 for $\pi_0$ and $\pi_1$

