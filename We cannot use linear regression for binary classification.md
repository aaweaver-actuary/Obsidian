#linear-model #classification 

- Suppose we code

  $$
  Y = \left\{ \begin{array}{ll}
  1 & \text{if } \text{red} \\
  0 & \text{if } \text{not red}
  \end{array} \right.
  $$

- Can we simply perform #linear-regression on $Y$ using $X$ as the predictor, and classify a new observation as red if the predicted value $\hat{Y}$ is greater than 0.5?
  - In the case of a #binary #target, #linear-regression does a good job as a classifier, and is equivalent to #linear-discriminant-analysis (LDA)
  - Since in the population $E[Y|X=x] = P(Y=1|X=x)$, we might think that #regression is perfect for this task
  - However, #linear-regression can produce values outside the range $[0,1]$, so this is not a good idea
  - #logistic-regression is a better alternative