[[Unsupervised Learning]]

- If we use [[Principal Components|principal components]] as a summary of our data, how many components are sufficient?
	- No simple answer here, because [[k-fold Cross Validation|cross validation]] is not available for this purpose
		- no target variable $Y$ 
	- When could we use [[k-fold Cross Validation|cross validation]] to select the number of [[Principal Components|principal components]]?
		- if using [[Principal Components Analysis (PCA)|principal components analysis]] to select the most important variables for a [[Regression|regression]] problem, do have a target variable trying to predict
- We can use the #scree-plot as a guide: look for an elbow
- 