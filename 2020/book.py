class Book:
	"""A book"""

	def __init__(self, score):
		self.score = score
		self.library_ids = []

	def __str__(self):
		return f'{self.id}\n'

	def __lt__(self, other):
		return self.score > other.score
