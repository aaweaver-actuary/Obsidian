[[Neural Networks]]

- they only show the simplest of [[Recurrent Neural Networks]]
- one variation treats the sequence as a 1-D image and uses [[Convolutional Neural Networks]] for fitting
	- eg a sequence of words using an #embedding representation can be viewed as an image, and the [[Convolutional Neural Networks]] convolves by sliding a [[Convolutional Filter]] along the sequence
- can have additional [[Hidden Layers In a Neural Network|hidden layers]], where each [[Hidden Layers In a Neural Network|hidden layer]] is itself a sequence, and treats the previous [[Hidden Layers In a Neural Network|hidden layer]] as an input sequence
- can have output also be a sequence
	- then input and output share the [[Hidden Layers In a Neural Network|hidden layers]] 
	- #seq2seq learning are used for language translation