[[Support Vector Machines (SVMs)]]

- we now extend the [[Maximal margin classifier - the separating hyperplane that makes the biggest gap between the two classes|maximum margin classifier]] to deal with situations where you cannot separate the data well

## Non-separable data
- if $n$ is large relative to the number of dimensions, you often cannot put a linear boundary between two groups:

![[Pasted image 20230819060344.png]]

- [[When the number of sample points is less than the number of predictors, you can always separate the data with a hyperplane]]

## Noisy data
- what if we need to add one more blue point
	- eg we go from the left to the right below
	- causes the [[Hyperplane|hyperplane]] to rotate pretty dramatically to still get a [[Separating hyperplanes|separating hyperplane]]
	- this can lead to a poor solution for the [[Maximal margin classifier - the separating hyperplane that makes the biggest gap between the two classes|maximal margin classifier]]
	- this behavior is not robust to the addition of one extra point

![[Pasted image 20230819060718.png]]

- [[The support vector classifier maximizes a soft margin]]
