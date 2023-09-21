[[Unsupervised Learning]] [[Matrix Completion]]

## Idea:
- start with #mean-imputation to get a first guess
- iterate: replace missing values at each iteration with [[Principal Components|principal components]]
- eventually get a better estimate/imputed data

## 1. Initialize

- Create a complete data matrix $\mathbf{\tilde{X}}$ by filling in the missing values using #mean-imputation[^1]

## 2. Iterate

Repeat steps (1) - (3) until the objective in (3) fails to decrease:

1. $$
   \text{minimize}_{\mathbf{A} \in \mathbb{R}^{n \times M}, \mathbf{B}\in\mathbb{R}^{p\times M}} \left\{ \sum_{j=1}^p \sum_{i=1}^n \left(\hat{x}_{ij} - \sum_{m=1}^M a_{im}b_{jm} \right)^2\right\}
   $$by computing the [[Principal Components|principal components]] of $\mathbf{\tilde{X}}$
2. For each missing entry $(i,j) \notin \mathcal{O}$, set $\tilde{x}_{ij} \leftarrow \sum_{m=1}^M \hat{a}_{im} \hat{b}_{jm}$
3. Compute the objective$$
   \sum_{(i,j) \in \mathcal{O}} \left( x_{ij} -\sum_{m=1}^M\hat{a}_{im} \hat{b}_{jm}\right)^2
   $$
## 3. Return the estimated missing entries $\tilde{x}_{ij}$, $(i,j)\notin\mathcal{O}$

[[Selecting a good value for M in the iterative algorithm for matrix completion]]



[^1]: [[Mean Imputation - Replace missing values for a variable by the mean of the non-missing entries]]