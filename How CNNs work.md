#statistical-learning 

- #cnn builds up an image in a #hierarchical fashion
	- first, it tries to ID little shapes or color splotches or edges in the image
		- eg it starts with very small features
	- edges and shapes are recognized and pieced together to form more complex shapes, eventually assembling the target image
	- this #hierarchical construction is achieved using #convolution-layers and #pooling-layers