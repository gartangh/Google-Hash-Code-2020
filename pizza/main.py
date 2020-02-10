# imports
import numpy as np


class Slice:
	"""A slice of pizza"""

	def __init__(self, from_r, from_c, to_r, to_c):
		self.from_r = from_r
		self.from_c = from_c
		self.to_r = to_r
		self.to_c = to_c

	def __str__(self):
		return f'{self.from_r} {self.from_c} {self.to_r} {self.to_c}\n'


# main
if __name__ == '__main__':

	pizza = None
	slices = []

	with open('in/a_example.in') as file_in:
		numbers = file_in.readline().split()
		r = int(numbers[0])
		c = int(numbers[0])
		l = int(numbers[0])
		h = int(numbers[0])

		pizza = np.zeros((r, c))

		for i in range(r):
			line = file_in.readline()
			for j in range(c):
				# Tomatoes (T) are 0
				# Mushrooms (M) are 1
				if line[j] == 'M':
					pizza[i, j] = 1

	# TODO find slices
	slices.append(Slice(0, 0, 2, 1))
	slices.append(Slice(0, 2, 2, 2))
	slices.append(Slice(0, 3, 2, 4))

	with open('out/a_example.txt', 'w') as file_out:
		file_out.write(f'{len(slices)}\n')
		for slice in slices:
			file_out.write(str(slice))
