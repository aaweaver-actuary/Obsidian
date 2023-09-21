[[Neural Networks]] [[Deep Learning]]

[[Motivation for recurrent neural networks]]

[[Recurrent Neural Network Architecture]]

- the [[Hidden Layers In a Neural Network|hidden layer]] is a sequence of vectors $A_t$, receiving as input $X_{\ell}$ as well as $A_{\ell - 1}$
    - $A_{\ell}$ produces an output $O_{\ell}$
- the same #weight's $\mathbf{W}$, $\mathbf{U}$, and $\mathbf{B}$ are used at each step in the sequence
    - hence the term recurrent
- the $A_{\ell}$ sequence represents an evolving model for the response that is updated as each element $X_{\ell}$ is processed

[[Recurrent Neural Network in More Detail]]

[[Recurrent Neural Network on IMDB Reviews]]

[[Time series forecasting with RNNs]]

[[Summary of Recurrent Neural Networks]]
