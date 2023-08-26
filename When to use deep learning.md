#neural-network #statistical-learning 

- #cnn's[^1] have had enormous success in image #classification[^3]  and modeling
	- starting to be used in medical diagnosis
- #rnn's [^2] have had big wins in speech modeling, language translation, and forecasting

question becomes: should we always use #deep-learning?
- often we see that the big successes occur when the #signal-to-noise-ratio is high
	- eg image recognition and language translation
		- humans can easily pick out what an image is, or understand some text
			- there is very little noise in this type of data -- it is almost entirely signal
	- datasets are large, #overfitting is not really a problem
		- [[Overfitting can be thought of as fitting the noise -- if there isn't much noise, there isn't much to overfit to]]
- [[For noisier data, simpler models often work better]]
- they endorse the #occams-razor principle:
	- prefer simpler models if they perform as well because there is value in model #interpretability 
- 


[^1]: [[Convolutional Neural Networks]]
[^2]: [[Recurrent Neural Networks]]
[^3]: [[Classification]] 