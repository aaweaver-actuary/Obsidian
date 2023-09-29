- qualitative variables take values in an unordered set $\mathcal{C}$, e.g. $\mathcal{C} = \{\text{red}, \text{green}, \text{blue}\}$
- given a feature vector $X$ and a qualitative response $Y$ taking values in $\mathcal{C}$, we want to learn a function $C(X)$ that predicts $Y \in \mathcal{C}$ from $X$
- often we are more interested in the probability that $Y$ belongs to a particular class $c \in \mathcal{C}$, i.e. $P(Y = c | X = x)$
    - for example, it is more valuable to have an estimate of the probability that an insurance claim is fraudulent than to simply predict whether or not it is fraudulent

[[We cannot use linear regression for binary classification]]

[[Multiclass classification cannot use linear regression either]]

[[Logistic regression is linear regression on the log-odds]]

[[Maximum likelihood is used to fit linear regression parameters]]

[[Logistic regression for multiclass classification]]

[[Case control sampling and logistic regression]]

[[Discriminant analysis for classification]]

[[Generalized linear models generalize linear regression to work on different types of responses]]

[[Other forms of discriminant analysis]]

[[Logistic Regression vs Discriminant Analysis]]

## Summary

- [[Logistic Regression|Logistic regression]] is very popular for [[Classification|classification]], especially for binary target
- [[Linear Discriminant Analysis|Linear discriminant analysis]] is useful when $n$ is small and the classes are well separated and [[Gaussian]] assumptions are reasonable
    - also useful when $K > 2$
- [[Naive Bayes]] is useful when $p$ is large and/or $n$ is small
- [[Logistic Regression|Logistic regression]] and [[Linear Discriminant Analysis|linear discriminant analysis]] are more popular than [[Naive Bayes]]
    - but [[Naive Bayes]] is often surprisingly hard to beat
- see section 4.5 for some comparisons of these methods on real data
