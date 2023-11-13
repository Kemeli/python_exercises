def square(x: int | float) -> int | float:
	"""squares a given value"""

	return x ** 2


def pow(x: int | float) -> int | float:
	"""raises a number to its own power"""

	return x ** x


def outer(x: int | float, function) -> object:
	"""returns a function that will do operation in a value updating the value
	to the result of the previous operation"""

	def inner() -> float:
		"""calls a function given from the outer function as parameter, while
		updating 'x' with the result of the previous inner() call"""

		nonlocal x
		a = function(x)
		x = a
		return a
	return inner
