import math


class Library:
	"""A library"""
	books = None
	libraries = None
	libraries_to_scan = None
	time_left = None

	def __init__(self, setup_time, rate, book_ids):
		self.setup_time = setup_time
		self.rate = rate
		self.book_ids = book_ids
		self.sent_book_ids = []
		self.score = 0

	def __lt__(self, other):
		return self.score > other.score

	def update_score(self):
		if (Library.time_left - self.setup_time) <= 0:
			# to remove this library from the list later
			self.sent_book_ids = []
			return

		# number of books that can still be scanned in the given time frame
		books_left = (Library.time_left - self.setup_time) * self.rate
		# check if limited by the given time frame
		if books_left < len(self.book_ids):
			# limited by the given time frame
			self.score = sum(Library.books[book_id].score for book_id in self.book_ids[:books_left])

		# all books can be scanned
		self.score = sum(Library.books[book_id].score for book_id in self.book_ids) / self.setup_time
