#statistical-learning #survival-analysis

### Definitions

- For each individual we suppose that there is a true #failure-time or #event-time $T$, as well as a true #censoring-time $C$
- The #survival-time represents the time at which the event of interest occurs
    - eg death
- The #censoring-time is the time at which data is #censored
    - eg the time the patient drops out of the study or the study ends

### Notation

- $T$ - #survival-time
- $C$ - #censoring-time
- $Y = \min (T, C)$ what we are interested in -- the #observed-survival-time
- $T < C \implies$ the event occurs before censoring
    - we observe the true #survival-time $T$
- $T > C \implies$ censoring occurs before the event
    - we observe the #censoring-time $C$
- $\delta$ - status indicator:
    $$
    \delta = \left\{ \begin{array}{cc}
    1 & \text{if } T \leq C \\
    0 & \text{if } T > C
    \end{array} \right. \hspace{18em}
    $$
- In our dataset we observe $n$ pairs $(Y, \delta)$, which we denote as $(y_1, \delta_1), \dots, (y_n, \delta_n)$
- 

