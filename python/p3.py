def fib(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fib(x - 2) + fib(x - 1)

if __name__ == "__main__":
	good_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
	# 100 fib. numbers too slow with this implementation
	fib_10 = [fib(x) for x in range(10)]
	assert fib_10 == good_10
