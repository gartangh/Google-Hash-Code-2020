from book import Book
from library import Library
from time import time


def read(filename):
	with open(filename) as file:
		# read in general info
		nr_of_books, nr_of_libraries, time_left = [int(nr) for nr in file.readline().split()]
		Library.time_left = time_left

		# read in books
		Library.books = {book_id: Book(int(book_score)) for book_id, book_score in enumerate(file.readline().split())}

		# read in libraries
		for id in range(nr_of_libraries):
			# read in library info
			_, time_left, rate = [int(nr) for nr in file.readline().split()]
			# read in library book ids
			book_ids = [int(book_id) for book_id in file.readline().split()]

			# add library id to the books of that library
			for library_book_id in book_ids:
				Library.books[library_book_id].library_ids.append(id)

			# sort books by score
			sub_dict = {book_id: Library.books[book_id] for book_id in book_ids}
			book_ids = [book_id for book_id, _ in sorted(sub_dict.items(), key=lambda book: (book[1], book[0]))]

			# create library object
			library = Library(id, time_left, rate, book_ids)
			library.update_score()
			Library.libraries[id] = library


def write(filename):
	with open(filename, "w+") as file:
		file.write(f"{len(Library.libraries_to_scan)}\n")
		for library_id, book_ids in Library.libraries_to_scan.items():
			file.write(f"{library_id} {len(book_ids)}\n")
			file.write(" ".join([str(book_id) for book_id in book_ids]) + "\n")


def calculate():
	while Library.time_left > 0:
		# stop when no libraries left
		if not bool(Library.libraries):
			return

		# sort libraries by score and select the best library
		Library.libraries = {library_id: library for library_id, library in
							 sorted(Library.libraries.items(), key=lambda library: (library[1], library[0]))}
		current_library_id, current_library = list(Library.libraries.items())[0]

		# stop condition if no books can be sent at the beginning
		if len(current_library.book_ids) == 0:
			return

		# update time left
		Library.time_left -= current_library.setup_time

		# send books by making deep copy to of book ids to libraries to scanL
		Library.libraries_to_scan[current_library_id] = [book_id for book_id in current_library.book_ids]

		# remove sent books, all references of libraries to it and the current library
		for book_id in Library.libraries_to_scan[current_library_id]:
			for library_id in Library.books[book_id].library_ids:
				Library.libraries[library_id].book_ids.remove(book_id)
			del Library.books[book_id]
		del Library.libraries[current_library_id]

		# update scores and remove empty libraries (there should be no references of books to it)
		ids_to_remove = []
		for library_id, library in Library.libraries.items():
			library.update_score()
			if library.score == 0:
				ids_to_remove.append(library_id)
		for library_id in ids_to_remove:
			del Library.libraries[library_id]


# main
if __name__ == '__main__':
	# initialization
	filenames = [
		'a_example',
		'b_read_on',
		'c_incunabula',
		# 'd_tough_choices',
		'e_so_many_books',
		'f_libraries_of_the_world'
	]

	for filename in filenames:
		print(filename)

		# reset all variables
		Library.books = {}
		Library.libraries = {}
		Library.libraries_to_scan = {}
		Library.time_left = 0

		# read
		print(f'Reading ... ', end='')
		start = time()
		read(f'in/{filename}.txt')
		print(f'{time() - start:.2f} s')

		# calculate
		print(f'Calculating ... ', end='')
		start = time()
		calculate()
		print(f'{time() - start:.2f} s')

		# write
		print(f'Writing ... ', end='')
		start = time()
		write(f'out/{filename}.txt')
		print(f'{time() - start:.2f} s')
		print()
