import math


class Library:
	"""A library"""
	books = {}
	libraries = {}
	libraries_to_scan = {}
	time_left = 0

	def __init__(self, setup_time, rate, book_ids):
		self.setup_time = setup_time
		self.rate = rate
		self.book_ids = book_ids
		self.sent_book_ids = []
		self.score = 0

	def __lt__(self, other):
		return self.score > other.score

	def update_score(self):
		# number of books that can still be scanned in the given time frame
		books_left = max(0, (Library.time_left - self.setup_time)) * self.rate
		# check if limited by the given time frame
		if books_left < len(self.book_ids):
			# limited by the given time frame
			self.score = sum(Library.books[book_id].score for book_id in self.book_ids[:books_left])

		# all books can be scanned
		self.score = sum(Library.books[book_id].score for book_id in self.book_ids) / self.setup_time
