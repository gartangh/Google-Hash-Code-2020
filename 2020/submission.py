from library import Library
from book import Book


def read(filename):
	with open(filename) as file:
		# Read in general info
		nr_of_books, nr_of_libraries, nr_of_days = [int(number) for number in file.readline().split()]

		# Read in books
		books = {book_id: Book(book_id, int(book_score)) for book_id, book_score in enumerate(file.readline().split())}

		# Read in libraries
		libraries = {}
		for library_id in range(nr_of_libraries):
			library_nr_of_books, library_nr_of_setup_days, library_nr_of_books_per_day = [int(number) for number in file.readline().split()]
			library_book_ids = [int(number) for number in file.readline().split()]
			library_book_ids = {k: v for k, v in sorted({book_id: books[book_id] for book_id in library_book_ids}.items(), key=lambda book: (book[1], book[0]))}
			libraries[library_id] = Library(library_id, library_book_ids, sum([books[book_id].score for book_id in library_book_ids]), library_nr_of_setup_days,library_nr_of_books_per_day)

			for library_book_id in library_book_ids:
				books[library_book_id].library_ids.append(library_id)

		libraries = {k: v for k, v in sorted(libraries.items(), key=lambda library: (library[1], library[0]))}

	return books, libraries, nr_of_days


def write(filename, libraries_to_scan):
	# TODO change to this year
	with open(filename, "w+") as file:
		file.write(f"{len(libraries_to_scan)}\n")
		for library_id, library in libraries_to_scan.items():
			file.write(f"{library_id} {len(library.book_ids)}\n")
			file.write(" ".join([str(book_id) for book_id in library.book_ids]) + "\n")
