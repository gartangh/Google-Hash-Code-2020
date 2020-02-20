class Book:
	"""A book"""

	def __init__(self, id, score):
		self.id = id
		self.score = score

	def __str__(self):
		return f'{self.id}\n'
