#rnn #neural-network #imdb-reviews

- not going to use the #bag-of-words-model 
- the document feature is a sequence of words $\{ \mathcal{W}\}_1^L$
- we typically truncate or pad the documents to be the same number $L$ of words
	- here we use $L=500$
- each word $\mathcal{W}_{\ell}$ is represented as a #one-hot-encoded #binary #feature vector $X_{\ell}$ of length 10,000, with all zeros and a single 1 in the position for that word in the dictionary
	- eg #dummy-variable's 
- this results in an extremely #sparse feature representation, which would not work well

## INSTEAD
- use a #lower-dimensional pretrained word #embedding[^1] matrix $\mathbf{E}$ ($m\times 10K$)
- this reduces the #binary #feature vector of length $10K$ to a #continuous feature vector of dimension $m \ll 10K$ 
	- eg $m$ is in the low hundreds

## RESULTS
- vanilla #rnn didn't work well
- tried #lstm[^4] 
- got 87% accuracy
	- slightly less than the 88% achieved by `glmnet`[^2] [^3]

- #imdb-reviews have been used as a #benchmark for new #rnn #neural-network-architecture's 
	- best reported result (ca 2020) was around 95%



[^1]: [[Word embeddings encode one-hot-encoded words to floats in a lower-dimensional vector space]]
[^2]: [[IMDB Movie Reviews Corpus]]
[^3]: [[Document Classification]]
[^4]: [[Long and Short Term Memory Model]]