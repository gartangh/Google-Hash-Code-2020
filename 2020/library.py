class Library:
	"""A library"""

	def __init__(self, id, books, number_of_books_per_day):
		self.id = id
		self.books = books
		self.number_of_books_per_day = number_of_books_per_day

	def __str__(self):
		return f'{self.id}\n'
