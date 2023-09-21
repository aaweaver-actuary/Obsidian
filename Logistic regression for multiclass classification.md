## [[Logistic Regression]] for $p > 2$

$$
\begin{align}
\log \left(  \frac{p(X)}{1 - p(X)} \right) =& \beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p \\
p(X) =& \frac{e^{\beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p}}
\end{align}
$$

Students tend to have:

1. higher balances than non students
2. higher marginal default rates than non students

But, for any given balance, students are less likely to default than non students

#### Big idea here:

- When you look at `student` on its own, it is [[Confounding Variable|confounded by]] `balance`
- The strong effects of `balance` make it look like `student`'s are worse credit risks
  - But #conditional on `balance`, you see that `student`'s are actually _better_ credit risks