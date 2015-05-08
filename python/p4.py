from itertools import permutations

def form_largest(lst):
	largest = 0
	for numbers in permutations(lst):
		n = int("".join((str(x) for x in numbers)))
		largest = max(largest, n)
	return largest


if __name__ == "__main__":
	numbers = [50, 2, 1, 9]
	assert form_largest(numbers) == 95021
