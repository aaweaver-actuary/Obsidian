#recurrent-neural-network #rnn #neural-network-architecture 

![[1 ccHxugJhQo7VH4GAAZt3Sg.png]]

- on left side you see the abbreviated form -- represented as a cycle
- on right side you see the sequence
	- on the bottom you have your input sequence $x_1, x_2, \dots, x_n$, indexed by time $t$
		- each observation is treated as a sequence of the same length
			- if they are not the same length, they are padded to be the same length
	- above the inputs, you have a #hidden-layer sequence of #activations 
		- these are also vectors - maybe same size, maybe different
	- $x_2$ is input to $A_2$
		- the previous #hidden-layer vector $A_1$ is also input to $A_2$ 
	- so $A_2$ gets input from $A_1$ and $x_2$
	- $A_3$ gets input from $x_3$ and $A_2$ 
	- ultimately the $A_i$ are accumulating a memory of what has happened in the sequence
	- memory is carried forward by the $A$s
	- also note that the same #weights $W_x$ and $W_H$ are used at each step as you move along
		- this is where the name "recurrent" in #recurrent-neural-network comes from
	- finally there is a set of output vectors $y_1, y_2, \dots, y_n$, with the same #weights $W_Y$ being used
		- you get a sequence of outputs, though maybe only interested in the accumulated knowledge of the output, so only interested in the last one