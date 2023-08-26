# [[Statistical Learning Lectures]]

* Random forests provide an improvement over [[Bagging|bagged]] trees by way of a small tweak that decorrelates the trees.
    * This [[6. Linear Model Selection and Regularization|reduces the variance]] when we average the trees.
* As in [[Bagging|bagging]], we build a number of [[8. Tree-Based Methods#8.1.2 The Basics of Decision Trees|decision trees]] on [[Resampling Methods#5.8 The bootstrap|bootstrapped]] training samples
* But when building these decision trees, each time a split in a tree is considered, **a random selection of** $m$ **predictors** is chosen as split candidates from the full set of $p$ predictors.
	* The split is allowed to use only one of those $m$ predictors
* A fresh selection of $m$ predictors is taken at each split
	* typically we choose $m\approx \sqrt{p}$
	* that is, the number of predictors considered at each split is approximately equal to the square root of the total number of predictors
		* eg 4/13 are chosen for the `Heart` dataset
* So you throw out most of your possible predictors for each iteration
## Example: gene expression data
- They applied random forests to a high-dimensional biological data set consisting of expression measurements of 4,718 genes measured on tissue samples from 349 patients
	- There are around 20,000 genes in humans, and individual genes have different levels of activity (or expression)
		- In particular, cells, tissues, and biological conditions
- Each of the patient samples has a qualitative label with 15 different levels:
	- Either normal or 1 of 14 different types of cancer
- Use random forests to predict cancer type based on the 500 genes that have the largest variance in the training set
	- This is not the same as the [[Resampling Methods#the wrong way|error in cross-validation]]
		- That error came about because the predictiveness of the set of variables was used to eliminate possible variables
		- Here, we are just looking at the _variance of the predictors in the training data set_
			- Think of this as **supervised** variable selection (WRT the target variable) vs **unsupervised** variable selection (WRT the variables themselves, not WRT the target variable)
- They randomly divided the observations into a training and a test set, and applied random forests to the training set for three different values of the number of splitting variables $m$

#### Nice thing about random forest/[[Bagging|bagging]]:
- you really can't overfit by adding too many trees
- each tree is a relatively weak learner
- at some point the variance will stop *decreasing*, but it also won't hurt you
- so you look at the out-of-bag errors to figure out when you have gone far enough