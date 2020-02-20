def read(filename):
	# TODO change to this year
	with open(filename) as file:
		line1 = file.readline().split()
		M = int(line1[0])
		N = int(line1[1])

		slices = [int(n) for n in file.readline().split()]

	return M, N, slices


def write(filename, K, slices):
	# TODO change to this year
	with open(filename, "w") as file:
		file.write(f"{K}\n")
		file.write(" ".join([str(n) for n in slices]))
