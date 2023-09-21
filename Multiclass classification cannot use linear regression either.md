[[Classification]]

- Now suppose we have a response variable $Y$ that can take on $3$ different values: \* a patient presents at the emergency room, and we must [[Classification|classify]] them according to their symptoms:  $$
  Y = \left\{ \begin{array}{ll}
  1 & \text{if } \text{stroke} \\
  2 & \text{if } \text{drug overdose} \\
  3 & \text{if } \text{epileptic seizure}
  \end{array} \right.
  $$
- The coding suggests an ordering of the classes
  - and in fact implies that the difference between `stroke` and `drug overdose` is the same as the difference between `drug overdose` and `epileptic seizure`
- [[Linear Regression|Linear regression]] is **not** appropriate here
  - it is a linear function  of $X$, and hence will take on values outside of the range $[1,3]$
  - it will also imply that the difference between `stroke` and `drug overdose` is twice as large as the difference between `drug overdose` and `epileptic seizure`
  - [[Discriminant analysis for classification]] or multi-class [[Logistic Regression|logistic regression]] are better alternatives