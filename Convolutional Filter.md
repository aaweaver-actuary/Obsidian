[[Convolutional Neural Networks]]

$$
\begin{align}
\text{Input Image} =& \left[
\begin{array}{ccc}
a & b&c\\
d&e&f\\
g&h&i\\
j&k&l
\end{array}
\right] \\

\text{ }\\

\text{Convolution Filter} =& \left[
\begin{array}{cc}
\alpha & \beta \\
\gamma & \delta
\end{array}
\right]\\

\text{ }\\

\text{Convolved Image} =& \left[
\begin{array}{cc}
a\alpha + b\beta + d\gamma + e\delta & b\alpha + c\beta + e\gamma + f\delta \\
d\alpha + e\beta +g\gamma + h\delta & e\alpha + f\beta + h\gamma + i\delta\\
g\alpha+h\beta+j\gamma+k\delta & h\alpha+i\beta+k\gamma+l\delta
\end{array}
\right]

\end{align}
$$

- the convolutional filter itself is an image
    - represents a small shape, edge, etc[^1]
    - it is small -- here 2x2
- we slide the filter around the input image, scoring for matches
    - the scoring is done via the #dot-product, as shown above
- if the sub-image of the input image is similar to the filter, the score is high, otherwise it is low
- the convolutional filter is learned during training
- the idea of a #convolution with a [[Convolutional Filter|convolutional filter]] is to find common patterns that occur in different parts of the image
- since images have three color channels (red, green, blue), the convolutional filter does as well
    - one convolutional filter per channel, and the #dot-product's are summed
- the #weight's in the [[Convolutional Filter|convolutional filter]] are learned by the [[Neural Networks|neural network]]

[^1]: [[How Convolutional Neural Networks Work]]
