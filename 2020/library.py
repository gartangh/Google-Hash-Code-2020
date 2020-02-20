import math

class Library:
	"""A library"""

	def __init__(self, id, books, number_of_setup_days, number_of_books_per_day):
		# Given attributes
		self.id = id
		self.books = books
		self.number_of_setup_days = number_of_setup_days
		self.number_of_books_per_day = number_of_books_per_day
		
		# Derived attributes
		self.total_score = sum([book.score for book in books])
		self.max_active_time = number_of_setup_days + math.ceil(len(books) / number_of_books_per_day)
		
	def __str__(self):
		return f'{self.id}\n'
