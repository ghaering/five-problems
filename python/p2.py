def alternate_elements(lst1, lst2):
	assert len(lst1) == len(lst2)
	def alt(lst1, lst2):
		for idx in range(len(lst1)):
			yield lst1[idx], lst2[idx]
	return list(alt(lst1, lst2))

if __name__ == "__main__":
	lst1 = ["a", "b", "c"]
	lst2 = [1, 2, 3]
	correct = list(zip(lst1, lst2))
	result = alternate_elements(lst1, lst2)
	assert len(correct) == len(result)
	for a, b in zip(correct, result):
		assert a == b
