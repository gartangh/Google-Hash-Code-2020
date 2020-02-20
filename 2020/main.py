from submission import write, read
from book import Book
from library import Library
from calculate import calculate

# main
if __name__ == '__main__':
	# initialization
	file_names = [
		'a_example',
		# 'b_read_on',
		# 'c_incunabula',
		# 'd_tough_choices',
		# 'e_so_many_books',
		# 'f_libraries_of_the_world'
	]

	for file_name in file_names:
		print(f'Reading {file_name}')
		books, libraries, nr_of_days = read(f'in/{file_name}.txt')
		print(f'Read {file_name}')

		print(f'Calculating solution for {file_name}')
		libraries_to_scan = calculate(books, libraries, nr_of_days)
		print(f'Calculated solution for {file_name}')

		print(f'Writing {file_name}')
		write(f'out/{file_name}.txt', libraries_to_scan)
		print(f'Wrote {file_name}')
