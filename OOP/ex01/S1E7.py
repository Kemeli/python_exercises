from S1E9 import Character

class Baratheon(Character):
	"""Representing the Baratheon family."""

	def __init__(self, name, is_alive=True):
		super().__init__(name, is_alive)
		self.family_name = "Baratheon"
		self.eyes = "brown"
		self.hairs = "dark"

	def __str__():
		return

	def __repr__(self):
		return f" Vector: ({self.family_name!r}, {self.eyes!r}, {self.hairs!r})"

	def die(self):
		"""
		Abstract method 'die', it changes the health state of the character.
		setting 'is_alive' value to False.
		"""
		self.is_alive = False


class Lannister(Character):
	"""Representing the Lannister family."""

	def __init__(self, name, is_alive=True):
		super().__init__(name, is_alive)
		self.family_name = "Lannister"
		self.eyes = "blue"
		self.hairs = "light"

	def __str__():
		return

	def __repr__(self):
		return f" Vector: ({self.family_name!r}, {self.eyes!r}, {self.hairs!r})"

	def die(self):
		"""
		Abstract method 'die', it changes the health state of the character.
		setting 'is_alive' value to False.
		"""
		self.is_alive = False

	def create_lannister(name, is_alive=True):
		return Lannister(name, is_alive)
