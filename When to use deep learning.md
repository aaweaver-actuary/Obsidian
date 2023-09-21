[[Neural Networks]] 

- [[Convolutional Neural Networks]] have had enormous success in image [[Classification|classification]] and modeling
	- starting to be used in medical diagnosis
- [[Recurrent Neural Networks]] have had big wins in speech modeling, language translation, and forecasting[^4]

question becomes: should we always use [[Deep Learning|deep learning]]?
- often we see that the big successes occur when the #signal-to-noise-ratio is high
	- eg image recognition and language translation
		- humans can easily pick out what an image is, or understand some text
			- there is very little noise in this type of data -- it is almost entirely signal
	- datasets are large, [[Overfitting|overfitting]] is not really a problem
		- [[Overfitting can be thought of as fitting the noise -- if there isn't much noise, there isn't much to overfit to]]
- [[For noisier data, simpler models often work better]]
- they endorse the #occams-razor principle:
	- prefer simpler models if they perform as well because there is value in model #interpretability
- 

[^4]: [[Recurrent Neural Network Forecaster]]