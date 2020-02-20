from submission import write, read
from calculate import calculate
from time import time

# main
if __name__ == '__main__':
	# initialization
	file_names = [
		'a_example',
		'b_read_on',
		'c_incunabula',
		'd_tough_choices',
		'e_so_many_books',
		'f_libraries_of_the_world'
	]

	for file_name in file_names:
		print()
		print(f'Reading {file_name}')
		tic = time()
		books, libraries, nr_of_days = read(f'in/{file_name}.txt')
		toc = time()
		print(f'Read {file_name} in {toc - tic:.2} s')

		print(f'Calculating solution for {file_name}')
		tic = time()
		libraries_to_scan = calculate(books, libraries, nr_of_days)
		toc = time()
		print(f'Calculated solution for {file_name} in {toc - tic:.2f} s')

		print(f'Writing {file_name}')
		tic = time()
		write(f'out/{file_name}.txt', libraries_to_scan)
		toc = time()
		print(f'Wrote {file_name} in {toc - tic:.2} s')
