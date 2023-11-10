class calculator:
	def __init__(self, arr):
		self.array = arr

	def __add__(self, object) -> None:
		self.array = [i + object for i in self.array]
		print(self.array)

	def __mul__(self, object) -> None:
		self.array = [i * object for i in self.array]
		print(self.array)

	def __sub__(self, object) -> None:
		self.array = [i - object for i in self.array]
		print(self.array)

	def __truediv__(self, object) -> None:
		try:
			self.array = [i / object for i in self.array]
			print(self.array)
		except Exception as e:
			print (f'{type(e).__name__} : {e}')
