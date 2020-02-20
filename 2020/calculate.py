def calculate(books, libraries, nr_of_days):
	step_size = 1
	setup_libraries = []
	setup_curr_library = None
	setup_curr_days_left = 0
	for day in range(0, nr_of_days, step_size):
		# Calculate weighted score (metric)
		for library_id, library in libraries.items():
			library.calcWeightedScore()

		# Sort on metric
		libraries_sorted = libraries
		# TO DO

		# Update books
		for setup_library in setup_libraries:
			

		# Update libraries
		if setup_curr_days_left == 0:
			if setup_curr_library is None:
				# Mark library as set up
				setup_libraries.append(setup_curr_library)
			
			# Select new library
			setup_curr_library = list(libraries_sorted.keys())[0]
			setup_curr_days_left = setup_curr_library.nr_of_setup_days
		else:
			setup_curr_days -= 1
			
	return libraries_to_scan
