[[Unsupervised Learning]] [[Matrix Completion]]

- It is often the case that data matrices $\mathbf{X}$ have missing entries, often represented as `NA` or `NaN` 
- This is a nuisance since many of our modeling procedures require complete data
- Sometimes #imputation is the prediction problem[^1]
- One approach: #mean-imputation[^2]
- This ignores the [[Correlation|correlations]] among variables[^3]
- We present an approach based on [[Principal Components|principal components]]

[[Matrix Approximation via Principal Components]]
[[Iterative Algorithm for Matrix Completion]]



[^1]: eg as in [[Recommender Systems]]
[^2]: [[Mean Imputation - Replace missing values for a variable by the mean of the non-missing entries]] 
[^3]: [[Mean Imputation - Replace missing values for a variable by the mean of the non-missing entries#Main problem|Problem with mean imputation]]
