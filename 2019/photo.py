class Photo:
	"""A photo"""

	def __init__(self, id, orientation, tags):
		self.id = id
		self.orientation = orientation
		self.tags = tags

	def __str__(self):
		return f'{self.id} {self.orientation} {self.tags}\n'
