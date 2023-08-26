#rnn #autocorrelation #statistical-learning 

The #rnn forecaster is similar in structure to a more traditional #autoregression procedure
$$
\mathbf{y} = \left[\begin{array}{c} 
v_{L+1} \\ v_{L+2} \\ \vdots \\ v_T
\end{array}\right] 
\hspace{3em}
\mathbf{M}=\left[\begin{array}{c c c c c}
1 & v_L & v_{L-1} & \cdots & v_1 \\
1 & v_{L+1} & v_{L} & \cdots & v_2 \\
1 & v_{L+2} & v_{L+1} & \cdots & v_3 \\
\vdots & \vdots & \vdots & \vdots &\vdots \\
1 & v_{T-1} & v_{T-2} & \cdots & v_{T-L} 
\end{array}\right] \hspace{9em}
$$
Fit an #OLS #regression of $\mathbf{y}$ on $\mathbf{M}$, giving
$$
\hat{v}_t = \hat{\beta}_0 + \hat{\beta}_1v_{t-1} + \hat{\beta}_2v_{t-2} + \cdots + \hat{\beta}_Lv_{t-L}
$$
This is known as an order-$L$ #autoregression model or $\text{AR}(L)$
