#maximal-margin-classifier 
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
- In #R, the function `svm()` in the `e1071` package solves this problem efficiently
- In #python, the function `SVC()` in the `sklearn.svm` package solves this problem efficiently
