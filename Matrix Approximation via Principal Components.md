[[Unsupervised Learning]] [[Matrix Completion]]

- In section 12.2.2[^1][^2] there was an interpretation of [[Principal Components|principal components]] in terms of #matrix-approximation:
  $$
  \text{minimize}_{A\in\mathbb{R}^{n\times m} , B\in\mathbb{R}^{p\times m}} \left\{ \sum_{j=1}^p\sum_{i=1}^n \left( x_{ij} - \sum_{m=1}^M a_{im}b_{jm}\right)^2 \right\} \hspace{4em}
  $$Where $\mathbf{A}$ is a $n \times M$[^3] matrix whose $(i,m)$ element is $a_{im}$, and $\mathbf{B}$ is a $p \times M$[^4] matrix whose $(j,m)$ element is $b_{jm}$

- It can be shown that for any value of $M$, the first $M$ [[Principal Components|principal components]] provide a solution to $\hat{a}_{im} = \phi_{jm}$ 
	- But what do we do if the matrix has missing elements?

## If there are missing elements

- Modified approximation criterion:
  $$
  \text{minimize}_{A\in\mathbb{R}^{n\times M}, B\in\mathbb{p\times M}} \left\{ \sum_{(i,j) \in \mathcal{O}} \left(x_{ij} - \sum_{m=1}^M a_{im}b_{jm}\right)^2\right\} \hspace{4em}
  $$
- where $\mathcal{O}$ is the set of all **observed** pairs of indices $(i,j)$
	- which is a subset of the possible $n\times p$ pairs

#### Once we solve this problem:

- We can estimate a missing observation $x_{ij}$ using $\hat{x}_{ij} = \sum_{m=1}^M \hat{a}_{im}\hat{b}_{jm}$
	- where $\hat{a}_{im}$ and $\hat{b}_{jm}$ are the $(i,m)$ and $(j,m)$ elements of the solution matrices $\mathbf{\hat{A}}$ and $\mathbf{\hat{B}}$  
- We can (approximately) recover the $M$ [[Principal Components|principal component]] scores and #loading's as if the data were complete

#### Improvement over #mean-imputation[^5]
- this method captures [[Correlation|correlations]] in the same way that [[Principal Components|principal components]] do
- Principal components exploit the correlations when finding [[Linear Combination|linear combinations]] that maximize variance
	- You do a [[Regression|regression]] of the non-missing values to predict the missing values

[^1]: [[Matrix Approximation via Principal Components]]
[^2]: Also from the book [[Introduction to Statistical Learning]], 12.2.2
[^3]: here $n$ is the number of rows
[^4]: here $p$ is the number of columns
[^5]: [[Mean Imputation - Replace missing values for a variable by the mean of the non-missing entries]] 