def calculate(books, libraries, nr_of_days):
	step_size = nr_of_days
	setup_libraries = []
	setup_curr_library = None
	setup_curr_days_left = 0

	return libraries 
	
	for day in range(0, nr_of_days, step_size):
		# Calculate weighted score (metric)
		for library_id, library in libraries.items():
			library.calcWeightedScore(books)

		# Sort on metric
		libraries_sorted = {k: v for k, v in sorted(libraries.items(), key=lambda library: (library[1], library[0]))}

		# Update books
		for setup_library in setup_libraries:
			pass

		# Update libraries
		if setup_curr_days_left == 0:
			if setup_curr_library is None:
				# Mark library as set up
				setup_libraries.append(setup_curr_library)
			
			# Select new library
			setup_curr_library = libraries_sorted[list(libraries_sorted.keys())[0]]
			setup_curr_days_left = setup_curr_library.number_of_setup_days
		else:
			setup_curr_days_left -= nr_of_days
			
	return libraries
