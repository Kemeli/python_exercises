import numpy as np

def check_errors(family, start, end):
	if type(start) != int or type(end) != int or type(family) != list:
		print("family must have list type / start and end must have int type")
		return False
	return True


def slice_me(family: list, start: int, end: int) -> list:
	"""
	Slices a list of data using NumPy and returns the result as a Python list.

	Parameters:
	family (list): The list of data to be sliced.
	start (int): The starting index for the slice.
	end (int): The ending index for the slice.

	Returns:
	list: A list containing the sliced data.

	If errors are found during error checking, the function returns None.

	Example:
	>>> data = [1, 2, 3, 4, 5]
	>>> result = slice_me(data, 1, 4)
	>>> print(result)
	[2, 3, 4]

	Example:
	>>> data = [1, 2, 3, 4, 5]
	>>> result = slice_me(data, 1, -2)
	>>> print(result)
	[2, 3]
	"""

	if (check_errors(family, start, end) == False):
		return None
	np_family = np.array(family)
	print(f'My shape is : {np_family.shape}')

	np_new = np_family[start:end]
	print(f'My new shape is : {np_new.shape}')

	return np_new.tolist()
