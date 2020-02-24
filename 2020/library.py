import math


class Library:
	"""A library"""
	books = None
	libraries = None
	libraries_to_scan = None
	time_left = None

	def __init__(self, id, setup_time, rate, book_ids):
		self.id = id
		self.setup_time = setup_time
		self.rate = rate
		self.book_ids = book_ids
		self.score = 0

	def __lt__(self, other):
		return self.score > other.score

	def update_score(self):
		# number of books that can still be scanned in time left to actually scan
		books_left = (Library.time_left - self.setup_time) * self.rate
		# remove reference of book to library if cannot be scanned in time
		if books_left <= 0:
			for book_id in self.book_ids:
				Library.books[book_id].library_ids.remove(self.id)
			self.book_ids = []
			self.score = 0
			return
		elif books_left < len(self.book_ids):
			for book_id in self.book_ids[books_left+1:]:
				Library.books[book_id].library_ids.remove(self.id)
			self.book_ids = self.book_ids[:books_left]

		# calculate score of remaining books
		self.score = sum(Library.books[book_id].score for book_id in self.book_ids) / self.setup_time

		if self.score == 0:
			for book_id in self.book_ids:
				Library.books[book_id].library_ids.remove(self.id)
			self.book_ids = []
