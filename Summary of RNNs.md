#statistical-learning #neural-network #recurrent-neural-network 

- they only show the simplest of #rnn's
- one variation treats the sequence as a 1-D image and uses #cnn's for fitting
	- eg a sequence of words using an #embedding representation can be viewed as an image, and the #cnn convolves by sliding a #convolutional-filter along the sequence
- can have additional #hidden-layer's, where each #hidden-layer is itself a sequence, and treats the previous #hidden-layer as an input sequence
- can have output also be a sequence
	- then input and output share the #hidden-layer's 
	- #seq2seq learning are used for language translation