import math


class Library:
	"""A library"""

	def __init__(self, id, book_ids, total_score, number_of_setup_days, number_of_books_per_day):
		# Given attributes
		self.id = id
		self.book_ids = book_ids
		self.number_of_setup_days = number_of_setup_days
		self.number_of_books_per_day = number_of_books_per_day
		
		# Derived attributes
		self.total_score = total_score
		self.max_active_time = number_of_setup_days + math.ceil(len(self.book_ids) / number_of_books_per_day)
		
	def __str__(self):
		return f'{self.id}\n'
