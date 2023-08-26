## #linear-discriminant-analysis when $p>1$

- The #Gaussian #density-function is

$$
f_k(x) = \frac{1}{(2\pi)^{p/2} |\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu_k)^T \Sigma^{-1} (x-\mu_k)\right)
$$

- #discriminant-function[^1]:
$$
\delta_k(x) = x^T \Sigma^{-1} \mu_k - \frac{1}{2} \mu_k^T \Sigma^{-1} \mu_k + \log \pi_k
$$
- note that again this is a #linear-function of $x$.

* this ( #iris-dataset ) was the data/analysis Fisher used to develop his #linear #discriminant-function
* when there are $K$ classes, #linear-discriminant-analysis can be viewed exactly in a $K-1$ dimensional plot
  - the dimensions represent #discriminant-function variables $1, 2, \dots, K-1$
  - each #discriminant-function variable is a #linear-combination of the original variables
  - the #discriminant-function variables are chosen to maximize the separation between the classes
  - #linear-discriminant-analysis is in a sense measuring the distance between the #mean's of the classes
    - there is a #subspace of dimension $K-1$ that contains the #mean's of all $K$ of the classes
    - eg if there are three classes, the #mean's of the first two classes are in a line,
      - while the third class is off the line, it defines a plane with the first two classes

### From $\delta_k(x)$ to $p_k(x)$

- once we have estimates of the #discriminant-function $\delta_k(x)$, we can turn these into estimates of the #posterior-distribution probabilities $p_k(x)$

  $$
  \hat{p}_k(x) = \frac{e^{ \hat{\delta}_k(x) }}{\sum_{l=1}^K e^{ \hat{\delta}_l(x) }}
  $$

- thus classifying to the largest $\hat{\delta}_k(x)$ is equivalent to classifying to the largest $\hat{p}_k(x)$


[^1]: [[The Discriminant Function]]