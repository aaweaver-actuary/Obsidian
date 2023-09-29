[[Unsupervised Learning]] [[Principal Components Analysis (PCA)]]

- if the variables are different units, [[Data Standardization|standardize]] each to have [[Standard Deviation|standard deviation]] 1 is recommended
- if they are the same units, you may or may not [[Data Standardization|standardize]] 
	- probably best to default to [[Data Standardization|standardize]] always
- this is because [[Principal Components Analysis (PCA)|principal components analysis]] tries to find the variables with the highest [[Variance|variance]] 
	- if the scales are different, [[Variance|variance]] may be very different as well, even if [[Coefficient of Variation|coefficient of variation]] is not all that different
