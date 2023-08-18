#bart #statistical-learning 

A collection of prediction models:
$$
\hat{f}^b(x) = \sum_{k=1}^K \hat{f}_k^b (x), \space \text{ for } b=1, 2, \dots, B
$$
To obtain a single prediction, we simply take the average after some $L$ *burn-in iterations* ([[BART notation]])
$$
\hat{f}(x) = \frac{1}{B-L}\sum_{b=L+1}^B \hat{f}^b(x)
$$
We can also compute other quantities such as the percentiles of $f^{L+1}(x), \dots, f^B(x)$ provide a measure of uncertainty