#time-series #neural-network #recurrent-neural-network 

- we only have a single series of data - how would we set this up for a #rnn ?
- We extract many short mini-series of input sequences $X=\{X_1, X_2, \dots, X_L\}$ with a predefined length $L$ known as the #lag
$$
X_1 = \left(\begin{array}{c}
v_{t-L} \\ r_{t-L} \\ z_{t-L}
\end{array}\right),
\space
X_2 = \left(\begin{array}{c}
v_{t-L+1} \\ r_{t-L+1} \\ z_{t-L+1}
\end{array}\right),
\dots, \space
X_L = \left(\begin{array}{c}
v_{t-1} \\ r_{t-1} \\ z_{t-1}
\end{array}\right) \hspace{9em}
$$
and 
$$
Y=v_t \hspace{29em}
$$
- Similar in structure to a more [[Traditional autoregression procedure]]

