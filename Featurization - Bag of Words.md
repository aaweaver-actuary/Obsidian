
we are using the [[IMDB Movie Reviews Corpus]] to do #sentiment [[Classification|classification]]

movie reviews are considered document's
- documents:
	- have different lengths
	- consist of sequences of words
- question: how to create features $X$ to characterize a#document

1. from a dictionary, ID the $10K$ most frequently occurring words
2. create a binary feature of length $p=10K$ for each document
	1. score 1 in every position the corresponding word occurred
3. with $n$ documents, we now have a $n\times p$ sparse feature matrix $\mathbf{X}$
4. we compare a [[The Lasso for regularization|lasso]] [[Logistic Regression|logistic regression]] model to a 2-hidden-layer [[Neural Networks|neural network]] 
	1. note: no [[Architecture of a Convolutional Neural Network|convolution layer]] here

- bags of words are #unigram's 
	- can instead use #2-gram's or in general #n-gram's