def calculate(books, libraries, nr_of_days):
	setup_libraries = {}
	day = 0

	while day < nr_of_days:
		# Sort on metric and select libary
		libraries_sorted = {k: v for k, v in sorted(libraries.items(), key=lambda l: (l[1], l[0]))}
		if len(list(libraries_sorted.keys())) == 0:
			return setup_libraries

		setup_curr_library = libraries_sorted[list(libraries_sorted.keys())[0]]

		# Update books
		nr_of_books = int((min(setup_curr_library.max_active_time, nr_of_days - day) - setup_curr_library.number_of_setup_days) * setup_curr_library.number_of_books_per_day)
		setup_curr_library.sent_book_ids = setup_curr_library.book_ids[:nr_of_books]
		books = [book for book in books if book not in setup_curr_library.book_ids[:nr_of_books]]
		setup_libraries[setup_curr_library.id] = setup_curr_library

		del libraries[setup_curr_library.id]
		day += setup_curr_library.number_of_setup_days

	return setup_libraries
