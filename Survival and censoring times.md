[[Survival Analysis]]

### Definitions

- For each individual we suppose that there is a true #failure-time or #event-time $T$, as well as a true [[Censoring Time|censoring time]] $C$
- The [[Survival Time|survival time]] represents the time at which the event of interest occurs
    - eg death
- The [[Censoring Time|censoring time]] is the time at which data is #censored
    - eg the time the patient drops out of the study or the study ends

### Notation

- $T$ - [[Survival Time|survival time]]
- $C$ - [[Censoring Time|censoring time]]
- $Y = \min (T, C)$ what we are interested in -- the [[Survival Time|observed survival time]]
- $T < C \implies$ the event occurs before censoring
    - we observe the true [[Survival Time|survival time]] $T$
- $T > C \implies$ censoring occurs before the event
    - we observe the [[Censoring Time|censoring time]] $C$
- $\delta$ - status indicator:
    $$
    \delta = \left\{ \begin{array}{cc}
    1 & \text{if } T \leq C \\
    0 & \text{if } T > C
    \end{array} \right. \hspace{18em}
    $$
- In our dataset we observe $n$ pairs $(Y, \delta)$, which we denote as $(y_1, \delta_1), \dots, (y_n, \delta_n)$
- 

