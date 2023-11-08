from abc import ABC, abstractmethod

class Character(ABC):
	"""Abstract class Character."""

	def __init__(self, name, is_alive=True):
		"""
		Constructor for Character.

		Parameters:
		'name', mandatory parameter, it's the first name
		of the character.
		'is_alive', optional boolean parameter, defaults to True.
		"""
		self.first_name = name
		self.is_alive = is_alive

	@abstractmethod
	def die(self):
		pass

class Stark(Character):
	"""Class Stark, inheritor of Character class."""

	def die(self):
		"""
		Abstract method 'die', it changes the health state of the character.
		setting 'is_alive' value to False.
		"""
		self.is_alive = False
