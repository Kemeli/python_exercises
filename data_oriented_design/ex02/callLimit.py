def callLimit(limit: int):
	"""Sets the limit of times a function can be called, by returning a
	decorator to the function.
	Return: decorator callLimiter.
	"""
	count = 0

	def callLimiter(function):
		"""Decorator:
		It wraps around the function and tracks how many times the function has
		been called.
		Return: wrapper limit_function.
		"""

		def limit_function(*args: any, **kwds: any):
			"""Wrapper:
			It limits 'function' calls.
			Increments 'count' when the wrapped function is called and calls
			'function' if 'count' hasn't reached it's 'limit';
			Return: None"""

			nonlocal count
			count += 1
			if count > limit:
				print (f'Error {function} call too many times')
			else:
				function(*args, **kwds)

		return limit_function
	return callLimiter

