#cnn #pooling-layers 
$$
\text{Max pool } \left[
\begin{array}{cccc}
1 & 2 & 5 & 3 \\
3 & 0 & 1 & 2 \\
2 & 1 & 3 & 4 \\
1 & 1 & 2 & 0
\end{array} 
\right]
\rightarrow
\left[

\begin{array}{cc}
3 & 5 \\
2 & 4
\end{array}
\right] \hspace{18em}
$$
- this is called #max-pooling
- each non-overlapping 2x2 block is replaced by its maximum
- this sharpens the feature identification
- allows for #locational-invariance
- reduces the dimension by a factor of 4
	- eg a factor of 2 in each dimension