from library import Library
from book import Book

def read(filename):
	with open(filename) as file:
		file_lines = file.readlines()

		# Read in general info
		info = file_lines[0].split(" ")
		nr_of_books = int(info[0])
		nr_of_libraries = int(info[1])
		nr_of_days = int(info[2])

		# Read in books
		books_scores = [int(book_score) for book_score in file_lines[1].split(" ")]
		books = []
		for book_id, book_score in enumerate(books_scores):
			book = Book(book_id, book_score)
			books.append(book)

		# Read in libraries
		libraries = []
		for library_id in range(nr_of_libraries):
			library_info = file_lines[2 + (2 * library_id)].split(" ")
			library_nr_of_books = int(library_info[0])
			library_nr_of_setup_days = int(library_info[1])
			library_nr_of_books_per_day = int(library_info[2])

			library_book_ids = [int(library_book_id) for library_book_id in file_lines[2 + (2 * library_id + 1)].split(" ")]
			library_books = []		
			for library_book_id in library_book_ids:
				library_books.append(books[library_book_id])
			
			library = Library(library_id, library_books, library_nr_of_setup_days, library_nr_of_books_per_day)
			libraries.append(library)
	return books, libraries, nr_of_days


def write(filename, libraries_to_scan):
	# TODO change to this year
	with open(filename, "w+") as file:
		file.write(f"{len(libraries_to_scan)}\n")
		for library_to_scan in libraries_to_scan:
			file.write(f"{library_to_scan.id} {len(library_to_scan.books)}\n")
			file.write(" ".join([str(book.id) for book in library_to_scan.books]) + "\n")
