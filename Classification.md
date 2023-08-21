#classification 

- qualitative variables take values in an unordered set $\mathcal{C}$, e.g. $\mathcal{C} = \{\text{red}, \text{green}, \text{blue}\}$
- given a feature vector $X$ and a qualitative response $Y$ taking values in $\mathcal{C}$, we want to learn a function $C(X)$ that predicts $Y \in \mathcal{C}$ from $X$
- often we are more interested in the #probability that $Y$ belongs to a particular class $c \in \mathcal{C}$, i.e. $P(Y = c | X = x)$
  - for example, it is more valuable to have an estimate of the probability that an insurance claim is fraudulent than to simply predict whether or not it is fraudulent

[[We cannot use linear regression for binary classification]]


### Multiclass Classification

- Now suppose we have a response variable $Y$ that can take on $3$ different values: \* a patient presents at the emergency room, and we must classify them according to their symptoms:

  $$
  Y = \left\{ \begin{array}{ll}
  1 & \text{if } \text{stroke} \\
  2 & \text{if } \text{drug overdose} \\
  3 & \text{if } \text{epileptic seizure}
  \end{array} \right.
  $$

- The coding suggests an ordering of the classes
  - and in fact implies that the difference between `stroke` and `drug overdose` is the same as the difference between `drug overdose` and `epileptic seizure`
- Linear regression is **not** appropriate here
  - it is a linear function of $X$, and hence will take on values outside of the range $[1,3]$
  - it will also imply that the difference between `stroke` and `drug overdose` is twice as large as the difference between `drug overdose` and `epileptic seizure`
  - **Discriminant analysis** or **Multiclass logistic regression** are better alternatives

## Logistic Regression

- Write $p(X) = P(Y=1|X)$ for short and call this the _probability of success_
- Consider using credit card `balance` to predict `default`
- Logistic regression uses the form
  $$
  p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}}
  $$
- It is easy to show that no matter what values $\beta_0$ and $\beta_1$ take, $p(X)$ will always be between 0 and 1
- You can rearrange the equation to get
  $$
  \log \left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X
  $$
- The left-hand side is called the _log-odds_ or _logit_ transformation of $p(X)$
  - it is also a _monotonic_ transformation of $p(X)$, so the two are equivalent for classification purposes

## Maximum Likelihood

- We use maximum likelihood to estimate $\beta_0$ and $\beta_1$
- The likelihood function is
  $$
  \ell(\beta_0, \beta_1) = \prod_{i:y_i=1} p(x_i) \prod_{i':y_{i'}=0} (1 - p(x_{i'}))
  $$
- This likelihood function gives the probability of the observed data as a function of $\beta_0$ and $\beta_1$
- We choose $\beta_0$ and $\beta_1$ to maximize this likelihood function

## Logistic Regression for $p > 2$

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

- When you look at `student` on its own, it is _confounded_ by `balance`
- The strong effects of `balance` make it look like `student`'s are worse credit risks
  - But once you condition on `balance`, you see that `student`'s are actually _better_ credit risks

## Case-control sampling and logistic regression

- In SA heart disease data, we have 160 cases and 302 controls, so $\tilde{\pi} = 0.346$, but the true $\pi$ is 0.5.
- With case-control sampling, we can estimate the regression coefficients $\beta_j$ accurately, but the intercept $\beta_0$ is biased.
  - Note that this depends on our having defined the model correctly.
- we can correct the estimated intercept by adding $\log(\tilde{\pi}/(1-\tilde{\pi}))$ to the estimated intercept:
  $$
  \hat{\beta}_0^* = \hat{\beta}_0
  $$


$$
\begin{align}
\log & \frac{\tilde{\pi}}{1-\tilde{\pi}}=\\
\log &\frac{\pi}{1-\pi}
\end{align}
$$


- often cases are rare, so $\tilde{\pi}$ is small, and the #bias is large.
  - up to 5 times larger than the #standard-error of the intercept estimate.
  - **THIS MEANS** that you will get similar results studying a 5:1 ratio of controls to cases as you would studying a 1:1 ratio of controls to cases?

## Discriminant analysis

- Here the approach is to model the distribution of $X$ in each of the response classes separately, and then use Bayes' theorem to flip these around into estimates for $Pr(Y=k|X=x)$.
- When we use normal/Gaussian distributions for each class, we get linear discriminant analysis (LDA) or quadratic discriminant analysis (QDA).
- This approach is quite general, and can be used with any distributional assumptions for $X$, though we will focus on the Gaussian case.

### Bayes theorem for classification

- standard Bayes theorem:
  $$
  Pr(Y=k|X=x) = \frac{Pr(X=x|Y=k) \cdot Pr(Y=k)}{Pr(X=x)}
  $$
- we write this slightly differently for discriminant analysis:
  $$
  Pr(Y=k|X=x) = \frac{\pi_k \cdot f_k(x)}{\sum_{l=1}^K \pi_l \cdot f_l(x)}
  $$
- $f_k(x)$ is the density function for $X$ in class $k$.
  - here we use normal distributions, so $f_k(x) = \frac{1}{\sqrt{2\pi}\sigma_k} \exp\left(-\frac{1}{2\sigma_k^2}(x-\mu_k)^2\right)$
- $\pi_k$ is the marginal or prior probability for class $k$.
  - this is the proportion of the training observations that belong to class $k$.

### Why discriminant analysis?

- When the classes are well-separated, the parameter estimates for the logistic regression model are surprisingly unstable.
  - LDA does not suffer from this problem.
- If $n$ is small and the distribution of the predictors $X$ is approximately normal in each of the classes, the LDA model is again more stable than the logistic regression model.
- LDA is popular when we have more than two response classes.
  - there is no straightforward generalization of the logistic regression model to the case of multiple response classes.
  - LDA provides low-dimensional views of the data.
- Under the assumption that the normal distribution is the correct one, Bayes is the absolute best we can do.
  - LDA is asymptotically equivalent to the Bayes classifier.
  - QDA is not.
  - QDA is more flexible, but can overfit.
  - This is probably rarely the case in practice, but it is a nice property to have.

## Linear discriminant analysis when $p=1$

- The Gaussian density function is

$$
f_k(x) = \frac{1}{\sqrt{2\pi}\sigma_k} \exp\left(-\frac{1}{2\sigma_k^2}(x-\mu_k)^2\right)
$$

- $\mu_k$ and $\sigma_k^2$ are the mean and variance for $X$ in class $k$.
- we assume that all classes have the same variance, $\sigma_1^2 = \sigma_2^2 = \cdots = \sigma_K^2 = \sigma^2$.

### Discriminant functions

- To classify at the value $x$, we compute the discriminant function for each class, and then pick the class with the largest value.
- We need to see which of the $p_k(x)$ is largest.
- If you take logs and drop terms that don't depend on $k$, you get that the largest $p_k(x)$ corresponds to the largest $\delta_k(x)$, where
  $$
  \delta_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \log \pi_k
  $$
- note here that $\delta_k(x)$ is linear in $x$.
- $\pi_k$ is the prior probability for class $k$.
  - this is the proportion of the training observations that belong to class $k$.
- $\mu_k$ is the mean of $X$ for observations in class $k$.
  - this is the average of $X$ for the training observations in class $k$.
- If there are $k=2$ classes and we assume equal priors, eg $\pi_1 = \pi_2 = 0.5$, then we can simplify the discriminant function further \* the decision boundary is at
  $$
  x = \frac{\mu_1 + \mu_2}{2}
  $$
- if $x$ is less than this, we predict class 1, otherwise we predict class 2.
- this is the same as the logistic regression decision boundary.

### Estimating the parameters

- We need to estimate $\pi_k$, $\mu_k$, and $\sigma^2$.
- $\pi_k$ is just the proportion of the training observations that belong to class $k$.
- $\mu_k$ is the average of $X$ for the training observations in class $k$.
- $\sigma^2$ is the average of the sample variances for each of the $K$ classes.

$$
\begin{align}
\hat{\pi}_k &= \frac{n_k}{n} \\
\hat{\mu}_k &= \frac{1}{n_k} \sum_{i:y_i=k} x_i \\
\hat{\sigma}^2 &= \frac{1}{n-K} \sum_{k=1}^K \sum_{i:y_i=k} (x_i-\hat{\mu}_k)^2 \\
&= \sum_{k=1}^K \frac{n_k-1}{n-K} \cdot \hat{\sigma}_k^2
\end{align}
$$

- $\hat{\sigma}_k^2$ is the sample variance for the observations in the $k$th class.
- $n_k$ is the number of observations in the $k$th class.
- $n$ is the total number of observations.
- $K$ is the number of classes.
- $\hat{\sigma}^2$ is a weighted average of the sample variances for each of the $K$ classes.
  - the weights are the proportions of observations in each class.
  - this is the pooled estimate of variance.
- the pooled estimate of variance is a weighted average of the sample variances for each of the $K$ classes.
  - the weights are the proportions of observations in each class.

## Linear discriminant analysis when $p>1$

- The Gaussian density function is

$$
f_k(x) = \frac{1}{(2\pi)^{p/2} |\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu_k)^T \Sigma^{-1} (x-\mu_k)\right)
$$

- discriminant function:

$$
\delta_k(x) = x^T \Sigma^{-1} \mu_k - \frac{1}{2} \mu_k^T \Sigma^{-1} \mu_k + \log \pi_k
$$

- note that again this is a linear function of $x$.

* this ( #iris-dataset ) was the data/analysis Fisher used to develop his linear discriminant function
* when there are $K$ classes, linear discriminant analysis can be viewed exactly in a $K-1$ dimensional plot
  - the dimensions represent discriminant variables $1, 2, \dots, K-1$
  - each discriminant variable is a linear combination of the original variables
  - the discriminant variables are chosen to maximize the separation between the classes
  - LDA is in a sense measuring the distance between the means of the classes
    - there is a subspace of dimension $K-1$ that contains the means of all $K$ of the classes
    - eg if there are three classes, the means of the first two classes are in a line,
      - while the third class is off the line, it defines a plane with the first two classes

### From $\delta_k(x)$ to $p_k(x)$

- once we have estimates of the discriminant functions $\delta_k(x)$, we can turn these into estimates of the posterior probabilities $p_k(x)$

  $$
  \hat{p}_k(x) = \frac{e^{ \hat{\delta}_k(x) }}{\sum_{l=1}^K e^{ \hat{\delta}_l(x) }}
  $$

- thus classifying to the largest $\hat{\delta}_k(x)$ is equivalent to classifying to the largest $\hat{p}_k(x)$

### False positive / false negative rates

- here do LDA on the Default data

## Generalized Linear Models

- linear regression is used for quantitative response
- linear logistic regression is the counterpart for binary response
  - models the logit of the probability of class membership as a linear function of the features
- other response types exist:
  - count data -> Poisson regression
  - non-negative data -> Tweedie regression
  - skewed distributions -> Gamma regression
- all these models are special cases of the **generalized linear model**
  - the response $Y$ is assumed to follow some distribution in the exponential family
  - the mean of $Y$ is related to the linear predictor via a link function
  - the linear predictor is a linear combination of the features

### Poisson Regression Model

- Poisson distribution is useful for modeling count data:

$$
\begin{align}
p(y|\lambda) &= \frac{e^{-\lambda}\lambda^y}{y!} \\
\lambda &= E(Y) = Var(Y)
\end{align}
$$

- the mean and variance of the Poisson distribution are equal
- with covariates $X$, the Poisson regression model is:

$$
\begin{align}
\log \left[ \lambda(X_1, \dots, X_p )\right] =& \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \\
\lambda(X_1, \dots, X_p ) =& e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}

\end{align}
$$

### Generalized Linear Models

- so far have covered three GLMs:
  - linear regression
  - logistic regression
  - Poisson regression
- each of these has a characteristic _link_ function: \* a link function is the transformation of the mean that is represented by the linear model
  $$
  \begin{align}
  \eta \left( E[Y | X_1, \dots, X_p] \right) &= \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p
  \end{align}
  $$
- **linear regression:** identity
  - $\eta(\mu) = \mu$
- **logistic regression:** logit
  - $\eta(\mu) = \log \left( \frac{\mu}{1-\mu} \right)$
- **Poisson regression:** log

  - $\eta(\mu) = \log(\mu)$

- each also has a characteristic _variance_ function
- the models are fit by maximum likelihood
- other GLMs include:
  - Gamma regression
  - Tweedie regression
  - Negative Binomial regression
  - Inverse Gaussian regression
  - more

## Other forms of discriminant analysis

$$
Pr(Y=k|X=x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^K \pi_l f_l(x)}
$$

- when $f_k(x)$ is the Gaussian density function for the $k$th class
  - **and** each class has the same covariance matrix $\Sigma$
  - we have **linear discriminant analysis**
- by altering the forms for the $f_k(x)$, we get different classifiers:
  - **quadratic discriminant analysis**
    - each class is still Gaussian, but has its own covariance matrix $\Sigma_k$
  - **naive Bayes**
    - with $f_k(x) = \prod_{j=1}^p f_{jk}(x_j)$ (conditional independence model) in each class
    - for Gaussian this means the $\Sigma_k$ are diagonal matrices
    - this assumes that the features are conditionally independent given the class, which is a very strong assumption and rarely true in practice
    - this will bias the variance estimates and in turn the class probabilities
    - but in terms of classification, all you need to know is the class with the highest probability, so it can tolerate some bias in the probabilities while still achieving good results
  - many other forms, by proposing different forms for $f_k(x)$ (including nonparametric approaches)

### Quadratic Discriminant Analysis

$$
\delta_k(x) = -\frac{1}{2} (x-\mu_k)^T \Sigma_k^{-1} (x-\mu_k) - \frac{1}{2} \log |\Sigma_k| + \log \pi_k
$$

- the decision boundary is quadratic in $x$
- because the $\Sigma_k$ are different for each class, the decision boundary is nonlinear/the quadratic terms matter in a way they don't for LDA

### Naive Bayes

- assume that the features are conditionally independent given the class
- useful when there are many features ($p$ is large), and so multivariate approaches are infeasible
- the conditional independence assumption means that the covariance matrices $\Sigma_k$ are diagonal
- Gaussian naive Bayes assumes that each $\Sigma_k$ is diagonal:

$$
\begin{align}
\delta_k(x) \propto& \log \left[ \pi_k \prod_{j=1}^p f_{jk}(x_j) \right] \\
=& -\frac{1}{2} \sum_{j=1}^p \left( \frac{x_j - \mu_{jk}}{\sigma_{jk}} + \log \sigma_{kj}^2 \right)^2 + \log \pi_k
\end{align}
$$

- can use for **mixed** feature vectors
  - some continuous, some discrete, some qualitative, some quantitative
  - if $X_j$ is qualitative, replace $f_{jk}(x_j)$ with $P(X_j = x_j | Y = k)$ over the discrete values of $X_j$
- despite really strong assumptions, naive Bayes often produces surprisingly good results
  - it is often used as a benchmark for classification methods
  - it is very fast and can be used on very large datasets
  - it is often surprisingly hard to beat

### Logisitc regression vs LDA

- for a two-class problem, one can show that for LDA

  $$
  \begin{align}
  \log \left( \frac{p_1(x)}{1-p_1(x)} \right) =& \log \left( \frac{p_1(x)}{p_2(x)} \right) \\
  =& c_0 + c_1 x_1 + \dots + c_p x_p
  \end{align}
  $$

- so LDA has the same form as logistic regression
- the difference is how the parameters are estimated
  - logistic regression uses the conditional likelihood based on $p(y|x)$
    - known as **discriminative** learning in a machine learning context
  - LDA estimates the parameters by maximizing the full likelihood of the parameters given the data
    - known as **generative** learning in a machine learning context
  - in practice results are often very similar
- LDA is more stable when $n$ is small and the classes are well-separated
  - logistic regression can be unstable in this case
- LDA is more popular when $p$ is large and/or $n$ is small
  - logistic regression can easily overfit
- _footnote:_ logistic regression can also fit quadratic decision boundaries by explicitly including quadratic terms in the model

## Summary

- logistic regression is very popular for classification, especially for binary classification
- LDA is useful when $n$ is small and the classes are well-separated and Gaussian assumptions are reasonable
  - also useful when $K > 2$
- naive Bayes is useful when $p$ is large and/or $n$ is small
- logistic regression and LDA are more popular than naive Bayes
  - but naive Bayes is often surprisingly hard to beat
- see section 4.5 for some comparisons of these methods on real data
