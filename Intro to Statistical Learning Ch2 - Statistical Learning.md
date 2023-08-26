---
annotation-target: pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf
---

![[pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf]]



>%%
>```annotation-json
>{"created":"2023-08-26T21:49:10.947Z","text":"### For prediction:\n\n1. reducible error\n2. irreducible error","updated":"2023-08-26T21:49:10.947Z","document":{"title":"ch02-statistical-learning.pdf","link":[{"href":"urn:x-pdf:d09fd072cdb7b2110a007c005f51c262"},{"href":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf"}],"documentFingerprint":"d09fd072cdb7b2110a007c005f51c262"},"uri":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","target":[{"source":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","selector":[{"type":"TextPositionSelector","start":5916,"end":5983},{"type":"TextQuoteSelector","exact":"The accuracy of ˆY as a prediction for Y depends on two quantities,","prefix":" whom the estimate of Y is high.","suffix":"which we will call the reducible"}]}]}
>```
>%%
>*%%PREFIX%%whom the estimate of Y is high.%%HIGHLIGHT%% ==The accuracy of ˆY as a prediction for Y depends on two quantities,== %%POSTFIX%%which we will call the reducible*
>%%LINK%%[[#^ot41p4tnaza|show annotation]]
>%%COMMENT%%
>### For prediction:
>
>1. reducible error
>2. irreducible error
>%%TAGS%%
>
^ot41p4tnaza


>%%
>```annotation-json
>{"created":"2023-08-26T21:50:07.103Z","text":"1. $\\epsilon$ may contain **unmeasured** variables that are useful for predicting $Y$\n2. $\\epsilon$ may also contain **unmeasurable** variation ","updated":"2023-08-26T21:50:07.103Z","document":{"title":"ch02-statistical-learning.pdf","link":[{"href":"urn:x-pdf:d09fd072cdb7b2110a007c005f51c262"},{"href":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf"}],"documentFingerprint":"d09fd072cdb7b2110a007c005f51c262"},"uri":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","target":[{"source":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","selector":[{"type":"TextPositionSelector","start":6809,"end":6855},{"type":"TextQuoteSelector","exact":"Why is the irreducible error larger than zero?","prefix":"educe the error introduced by \".","suffix":" The quantity \"may con-tain unme"}]}]}
>```
>%%
>*%%PREFIX%%educe the error introduced by ".%%HIGHLIGHT%% ==Why is the irreducible error larger than zero?== %%POSTFIX%%The quantity "may con-tain unme*
>%%LINK%%[[#^eg5uxgjia5i|show annotation]]
>%%COMMENT%%
>1. $\epsilon$ may contain **unmeasured** variables that are useful for predicting $Y$
>2. $\epsilon$ may also contain **unmeasurable** variation 
>%%TAGS%%
>
^eg5uxgjia5i


>%%
>```annotation-json
>{"created":"2023-08-26T21:52:34.328Z","text":"### Reasons to estimate $f$\n\n1. prediction\n2. inference","updated":"2023-08-26T21:52:34.328Z","document":{"title":"ch02-statistical-learning.pdf","link":[{"href":"urn:x-pdf:d09fd072cdb7b2110a007c005f51c262"},{"href":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf"}],"documentFingerprint":"d09fd072cdb7b2110a007c005f51c262"},"uri":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","target":[{"source":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","selector":[{"type":"TextPositionSelector","start":4905,"end":4954},{"type":"TextQuoteSelector","exact":"two main reasons that we may wish to estimate f :","prefix":".2.1.1 Why Estimate f?There are ","suffix":" predictionand inference. We dis"}]}]}
>```
>%%
>*%%PREFIX%%.2.1.1 Why Estimate f?There are%%HIGHLIGHT%% ==two main reasons that we may wish to estimate f :== %%POSTFIX%%predictionand inference. We dis*
>%%LINK%%[[#^6e51bltyter|show annotation]]
>%%COMMENT%%
>### Reasons to estimate $f$
>
>1. prediction
>2. inference
>%%TAGS%%
>
^6e51bltyter


>%%
>```annotation-json
>{"created":"2023-08-26T21:54:13.392Z","text":"### Mean square error\n$$\n\\begin{align}\nE[Y - \\hat{Y}]^2 =& E[f(X) + \\epsilon - \\hat{f}(X)]^2 \\\\\n=& [f(X) - \\hat{f}(X)]^2 + \\text{Var}(\\epsilon)\n\n\\end{align}\n$$","updated":"2023-08-26T21:54:13.392Z","document":{"title":"ch02-statistical-learning.pdf","link":[{"href":"urn:x-pdf:d09fd072cdb7b2110a007c005f51c262"},{"href":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf"}],"documentFingerprint":"d09fd072cdb7b2110a007c005f51c262"},"uri":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","target":[{"source":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","selector":[{"type":"TextPositionSelector","start":7764,"end":7856},{"type":"TextQuoteSelector","exact":"Assume for a moment that both ˆf and X are fixed,so that the only variability comes from \". ","prefix":"elds theprediction ˆY = ˆf (X). ","suffix":"Then, it is easy to show thatE(Y"}]}]}
>```
>%%
>*%%PREFIX%%elds theprediction ˆY = ˆf (X).%%HIGHLIGHT%% ==Assume for a moment that both ˆf and X are fixed,so that the only variability comes from ".== %%POSTFIX%%Then, it is easy to show thatE(Y*
>%%LINK%%[[#^on2fpjgcwg7|show annotation]]
>%%COMMENT%%
>### Mean square error
>$$
>\begin{align}
>E[Y - \hat{Y}]^2 =& E[f(X) + \epsilon - \hat{f}(X)]^2 \\
>=& [f(X) - \hat{f}(X)]^2 + \text{Var}(\epsilon)
>
>\end{align}
>$$
>%%TAGS%%
>
^on2fpjgcwg7


>%%
>```annotation-json
>{"created":"2023-08-26T21:56:45.249Z","text":"### Focus of this book:\nTechniques for estimating $f$ with the aim of minimizing the reducible error","updated":"2023-08-26T21:56:45.249Z","document":{"title":"ch02-statistical-learning.pdf","link":[{"href":"urn:x-pdf:d09fd072cdb7b2110a007c005f51c262"},{"href":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf"}],"documentFingerprint":"d09fd072cdb7b2110a007c005f51c262"},"uri":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","target":[{"source":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","selector":[{"type":"TextPositionSelector","start":8211,"end":8233},{"type":"TextQuoteSelector","exact":"The focus of this book","prefix":" with the error term \". variance","suffix":" is on techniques for estimating"}]}]}
>```
>%%
>*%%PREFIX%%with the error term ". variance%%HIGHLIGHT%% ==The focus of this book== %%POSTFIX%%is on techniques for estimating*
>%%LINK%%[[#^9tco0h6wn47|show annotation]]
>%%COMMENT%%
>### Focus of this book:
>Techniques for estimating $f$ with the aim of minimizing the reducible error
>%%TAGS%%
>
^9tco0h6wn47


>%%
>```annotation-json
>{"created":"2023-08-26T21:57:57.024Z","text":"### Reducible error:\n$[f(X) - \\hat{f}(X)]^2$","updated":"2023-08-26T21:57:57.024Z","document":{"title":"ch02-statistical-learning.pdf","link":[{"href":"urn:x-pdf:d09fd072cdb7b2110a007c005f51c262"},{"href":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf"}],"documentFingerprint":"d09fd072cdb7b2110a007c005f51c262"},"uri":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","target":[{"source":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","selector":[{"type":"TextPositionSelector","start":7922,"end":7940},{"type":"TextQuoteSelector","exact":"[ f (X) − ˆf (X)]2","prefix":" ˆY )2 = E[f (X) + \"− ˆf (X)]2= ","suffix":"︸ ︷︷ ︸Reducible+ Var(\")︸ ︷︷ ︸Irr"}]}]}
>```
>%%
>*%%PREFIX%%ˆY )2 = E[f (X) + "− ˆf (X)]2=%%HIGHLIGHT%% ==[ f (X) − ˆf (X)]2== %%POSTFIX%%︸ ︷︷ ︸Reducible+ Var(")︸ ︷︷ ︸Irr*
>%%LINK%%[[#^7dcmktrfm2e|show annotation]]
>%%COMMENT%%
>### Reducible error:
>$[f(X) - \hat{f}(X)]^2$
>%%TAGS%%
>
^7dcmktrfm2e


>%%
>```annotation-json
>{"created":"2023-08-26T21:58:53.679Z","text":"### Irreducible error:\n$\\text{Var}(\\epsilon)$","updated":"2023-08-26T21:58:53.679Z","document":{"title":"ch02-statistical-learning.pdf","link":[{"href":"urn:x-pdf:d09fd072cdb7b2110a007c005f51c262"},{"href":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf"}],"documentFingerprint":"d09fd072cdb7b2110a007c005f51c262"},"uri":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","target":[{"source":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","selector":[{"type":"TextPositionSelector","start":7957,"end":7963},{"type":"TextQuoteSelector","exact":"Var(\")","prefix":" (X) − ˆf (X)]2︸ ︷︷ ︸Reducible+ ","suffix":"︸ ︷︷ ︸Irreducible, (2.3)where E("}]}]}
>```
>%%
>*%%PREFIX%%(X) − ˆf (X)]2︸ ︷︷ ︸Reducible+%%HIGHLIGHT%% ==Var(")== %%POSTFIX%%︸ ︷︷ ︸Irreducible, (2.3)where E(*
>%%LINK%%[[#^xjkzx7d1lu|show annotation]]
>%%COMMENT%%
>### Irreducible error:
>$\text{Var}(\epsilon)$
>%%TAGS%%
>
^xjkzx7d1lu


>%%
>```annotation-json
>{"created":"2023-08-26T22:01:54.152Z","text":"### For inference:\n1. which predictors are associated with the response?\n2. what is the relationship between the response and each predictor?\n3. can the relationship between $Y$ and each predictor be adequately summarized using a linear equation, or is the relationship more complicated?\n","updated":"2023-08-26T22:01:54.152Z","document":{"title":"ch02-statistical-learning.pdf","link":[{"href":"urn:x-pdf:d09fd072cdb7b2110a007c005f51c262"},{"href":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf"}],"documentFingerprint":"d09fd072cdb7b2110a007c005f51c262"},"uri":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","target":[{"source":"vault:/pdf/intro-to-statistical-learning/ch02-statistical-learning.pdf","selector":[{"type":"TextPositionSelector","start":8506,"end":8593},{"type":"TextQuoteSelector","exact":"We are often interested in understanding the association between Y andX1, . . . , X p. ","prefix":"ys unknown in practice.Inference","suffix":"In this situation we wish to est"}]}]}
>```
>%%
>*%%PREFIX%%ys unknown in practice.Inference%%HIGHLIGHT%% ==We are often interested in understanding the association between Y andX1, . . . , X p.== %%POSTFIX%%In this situation we wish to est*
>%%LINK%%[[#^mml3j9wsox|show annotation]]
>%%COMMENT%%
>### For inference:
>1. which predictors are associated with the response?
>2. what is the relationship between the response and each predictor?
>3. can the relationship between $Y$ and each predictor be adequately summarized using a linear equation, or is the relationship more complicated?
>
>%%TAGS%%
>
^mml3j9wsox
