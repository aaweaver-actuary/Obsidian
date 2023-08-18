#svm #statistical-learning 

This is a direct way to approach the #binary-target problem:
	we try to find a plane that separates the classes in feature space

If we can't we get creative in two ways:
1. we soften what we mean by separates
2. we enrich and enlarge the feature space so that separation is possible

[[hyperplane|What is a hyperplane?]]

## Separating hyperplanes

If
$$
f(X)= \beta_0 + \beta_1X_1 + \cdots + \beta_pX_p
$$
then $f(X)>0$ for points on one side of the #hyperplane and $f(X) < 0$ for points on the other side

![[Pasted image 20230818042537.png]]

If we code the colored points as $Y_i=+1$ for blue, say, and $Y_i=-1$ for red, then if 
$$
\begin{align}
Y_i\cdot f(X_i) > 0 \space \text{ for all } i
\end{align}
$$
then $f(X)=0$ defines a #separating-hyperplane

## Maximal margin classifier

Among all #separating-hyperplane, find the one that makes the biggest gap or margin between the two classes

This is a #constrained-optimization-problem:
$$
\begin{align}
\max_{\beta_i}M\\
\text{subject to } \sum_{j=1}^p \beta_j^2 =1 \\
y_i(\beta_0 + \beta_1x_{i1}+\cdots+\beta_px_{ip}) \ge M\\
\text{for all } i =1, 2, \dots, N
\end{align}
$$
- This can be rephrased as a #convex-quadratic-program and solved efficiently
- In `R`, the function `svm()` in the `e1071` package solves this problem efficiently
- In `python`, the function `SVC()` in the `sklearn.svm` package solves this problem efficiently