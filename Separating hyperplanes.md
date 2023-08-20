#statistical-learning #svm 

If

$$
f(X)= \beta_0 + \beta_1X_1 + \cdots + \beta_pX_p
$$

then $f(X)>0$ for points on one side of the #hyperplane and $f(X) < 0$ for points on the other side

![[Pasted image 20230818042537.png]]

If we code the colored points as $Y_i=+1$ for blue, say, and $Y_i=-1$ for red, then if

$$
\begin{align}
Y_i\cdot f(X_i) > 0 \space \text{ for all } i
\end{align}
$$

then $f(X)=0$ defines a #separating-hyperplane
