- 8 hex digits = 32bits -> 5 fields:
	1. 1 bit => source type (input, internal)
	2. 7 bit => source ID (take it modulo number of neurons)
	3. 1 bit => sync type (internal or output neuron)
	4. 7 bit => sync ID (exactly which internal/output neuron)
	5. 16 bit remainder => signed 16 bit integer weight 
		- normalized to be in $[-4.0, 4.0]$ 