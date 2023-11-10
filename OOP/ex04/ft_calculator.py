class calculator:
	"""offers static methods to dotproduct, vector addition and vector subtraction"""
	pass
	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		"""prints de docproduct of two float lists """

		dot = sum(i[0] * i[1] for i in zip(V1, V2))
		print(f'Dot product is: {dot}')

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		"""prints the addition of two float lists"""

		add = [i[0] + i[1] for i in zip(V1, V2)]
		print(f'Add vector is: {add}')

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		"""prints the subtraction of two float lists"""

		sous = [i[0] - i[1] for i in zip(V1, V2)]
		print(f'Sous vector is: {sous}')
