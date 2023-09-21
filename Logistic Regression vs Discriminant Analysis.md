### [[Logistic Regression|Logistic regression]] vs [[Linear Discriminant Analysis]]

- for a two-class problem, one can show that for [[Linear Discriminant Analysis]][^1] [^2] $$
    \begin{align}
    \log \left( \frac{p_1(x)}{1-p_1(x)} \right) =& \log \left( \frac{p_1(x)}{p_2(x)} \right) \\
    =& c_0 + c_1 x_1 + \dots + c_p x_p
    \end{align}
    $$
- so [[Linear Discriminant Analysis]] has the same form as [[Logistic Regression|Logistic regression]][^3]
- the difference is how the parameters are estimated
    - [[Logistic Regression|Logistic regression]] uses the [[Likelihood|conditional likelihood]] based on $p(y|x)$
        - known as #discriminative-learning in a machine learning context
    - [[Linear Discriminant Analysis|Linear discriminant analysis]] estimates the parameters by [[Maximum likelihood is used to fit linear regression parameters|maximizing the full likelihood]] of the parameters given the data
        - known as #generative-learning in a machine learning context
    - in practice results are often very similar
- [[Linear Discriminant Analysis|linear discriminant analysis]] is more stable when $n$ is small and the classes are #well-separated
    - [[Logistic Regression|Logistic regression]] can be unstable in this case
- [[Linear Discriminant Analysis|linear discriminant analysis]] is more popular when $p$ is large and/or $n$ is small
    - [[Logistic Regression|Logistic regression]] can easily [[Overfitting|overfit]]
- _footnote:_ [[Logistic Regression|Logistic regression]] can also fit quadratic [[Decision Boundary|decision boundary]] by explicitly including quadratic terms in the model

[^1]: [[Linear discriminant analysis when p=1]]
[^2]: [[Linear discriminant analysis when p is bigger than 1]]
[^3]: [[Logistic regression is linear regression on the log-odds]]
