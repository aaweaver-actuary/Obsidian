```python
class Organism:
	def __init__(self):
		"""
		Class Attributes:
		----------------
		loc : tuple
			Location of the organism in the world.
		genome : Genome
			The genome of the organism.
		"""
		self.loc = None
		self.genome = Genome()
		self.brain = Brain()
```
