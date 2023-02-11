"""
	3 - Sliding Window

In the previous two lessons, we learned about the three 
operations that carry out feature extraction from an 
image:

	- filter with a convolution layer
	- detect with ReLU activation
	- condense with a maximum pooling layer

The convolution and pooling operations share a common 
feature: they are both performed over a SLIDING WINDOW. 

With convolution, this "window" is given by the 
dimensions of the kernel, the parameter 'kernel_size'. 
With pooling, it is the pooling window, given by 
'pool_size'.

----

There are two additional parameters affecting both 
convolution and pooling layers: these are the STRIDES 
of the window and whether to use PADDING at the image 
edges.

The STRIDES parameter says how far the window should 
move at each step, and the PADDING parameter describes 
how we handle the pixels at the edges of the input.
"""