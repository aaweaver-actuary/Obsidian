#### types of neurons:
1. Sensory input neuron
2. internal neuron
3. action output neuron

each gene in genome specifies one connection between neurons:
- sensory neuron -> inner neuron
- inner neuron -> action neuron
- inner -> another inner (even itself)

- there are positive and negative connections

input neurons:
- produce float in $[0, 1]$ range
- multiplied by weight of connection in $[-4.0, 4.0]$ range

neuron output = $\tanh(\text{sum}(\text{inputs}))$ $\in [-1.0, 1.0]$  

output neuron = $\tanh(\text{sum}(\text{inputs})) \in [-1.0, 1.0]$ 

![[Pasted image 20230921065035.png]]
![[Pasted image 20230921065302.png]]

