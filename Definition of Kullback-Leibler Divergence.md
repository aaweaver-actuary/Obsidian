
- The [[Kullback–Leibler Divergence]] is denoted $D_{KL}(P||Q)$

For two probability distributions $P$ and $Q$, 
$$
\begin{align}
D_{KL}(P||Q) =& \sum_{x\in \mathcal{X}} P(x) \log \left( \frac{P(x)}{Q(x)} \right), \space \text{ discrete case}\\
=& \int_{-\infty}^{\infty} P(x)\log\left(\frac{P(x)}{Q(x)} \right) \space dx,\space \text{ continuous case}
\end{align}
$$