#statistical-learning #featurization #bag-of-words-model

we are using the [[IMDB Movie Reviews Corpus]] to do #sentiment #classification [^1]

movie reviews are considered #document's
- #document's:
	- have different lengths
	- consist of sequences of words
- question: how to create #feature's $X$ to characterize a #document

1. from a dictionary, ID the $10K$ most frequently occurring words
2. create a #binary #feature of length $p=10K$ for each document
	1. score 1 in every position the corresponding word occurred
3. with $n$ documents, we now have a $n\times p$ #sparse feature matrix $\mathbf{X}$
4. we compare a #lasso #logistic-regression model to a 2-hidden-layer #neural-network 
	1. note: no #convolution-layer here

- bags of words are #unigrams 
	- can instead use #2-grams or in general #n-grams

[^1]: [[Classification]]