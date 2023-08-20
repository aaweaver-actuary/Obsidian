#svm #inner-products #kernels 

- define #inner-products between vectors:
$$
\langle x_i, x_{i;'} \rangle = \sum_{j=1}^p x_{ij}x_{i'j} \hspace{27em}
$$

- the #linear #support-vector-classifiers can be represented as
$$
f(x) = \beta_0 + \sum_{i=1}^n \alpha_i \langle x, x_i \rangle \hspace{26em}
$$
- to estimate the $n$ parameters $\alpha_1, \dots, \alpha_n$ and $\beta_0$, all we need are the $\binom{n}{2}$ #inner-products $\langle x_i, x_{i'} \rangle$ between all pairs of training observations

- it turns out that most of the $\hat{\alpha_i}$ can be zero:
$$
f(x)=\beta_0+\sum_{i\in \mathcal{S}} \hat{\alpha}_i \langle x, x_i \rangle \hspace{26em}
$$
- $\mathcal{S}$ is the #support-set of indices such that $\hat{\alpha_i} > 0$ 

### big idea:
- the only points that contribute to the solution are those inside or touching the margin boundary lines