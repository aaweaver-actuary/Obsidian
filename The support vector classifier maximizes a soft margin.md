[[Support Vector Machines (SVMs)]] [[Classification]]

## soft margin that is maximized:

$$
\begin{align}
\max_{\beta_i, \epsilon_i} \space M\\
\text{subject to } \sum_{j=1}^p\beta_j^2 =1\\
y_i(\beta_0 + \beta_1x_{i1} + \beta_2x_{i2} + \cdots + \beta_px_{ip} ) \ge M(1-\epsilon_i)\\
\epsilon_i \ge 0\\
\sum_{i=1}^n \epsilon_i \le C
\end{align}
$$

[[Making the soft margin wider or smaller in an SVC has an effect similar to that of regularization]]

## [[Maximal margin classifier - the separating hyperplane that makes the biggest gap between the two classes|Maximal Margin Classifier]] vs Soft Margin Classifier

- [[The difference between a maximal margin and a soft margin is the epsilon discount factor]]

- on 4th line, $C$ refers to our budget allowed for the total amount of slack

- This is again a #convex-optimization problem
- $C$ is a #hyperparameter
    - as we change $C$ the #soft-margin will get wider or smaller
    - and a [[Regularization|regularization]] parameter
- [[Support Vector Machines (SVMs)|A support vector machine]] treats all the variables as equal in terms of distance
    - [[Standardize data before using it in a support vector machine]]
-
