def calculate(books, libraries, nr_of_days):
	step_size = 1000
	setup_libraries = []
	setup_curr_library = None
	day = 0

	while day < nr_of_days:
		# Calculate weighted score (metric)
		# for library_id, library in libraries.items():
			# library.calcWeightedScore(books)

		# Sort on metric and select libary
		libraries_sorted = {k: v for k, v in sorted(libraries.items(), key=lambda l: (l[1], l[0]))}
		setup_curr_library = libraries_sorted[list(libraries_sorted.keys())[0]]

		# Update books
		nr_of_books = int((min(setup_curr_library.max_active_time, nr_of_days - day) - setup_curr_library.number_of_setup_days) * setup_curr_library.number_of_books_per_day)
		setup_curr_library.sent_book_ids = setup_curr_library.book_ids[:nr_of_books]
		setup_libraries.append(setup_curr_library)

		day += setup_curr_library.number_of_setup_days

	return setup_libraries
