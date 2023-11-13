import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
	return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
	"""Creates a Student data class and initializes it's attributes.

	Attributes:
	name (str) : Student first name;
	surname (str) : student last name;
	active (bool, optional);
	login (str) : Student login, generated through generate_id();
	id (str) : Student id, generated using it's name and surname.
	"""
	name : str = field(init=True)
	surname : str = field(init=True)
	active: bool = field(init=False, default=True)
	login: str = field(init=False)
	id: str = field(init=False, default=generate_id())

	def __post_init__(self):
		"""inicializes 'login' attribute, after class __init__() is called"""
		self.login = self.name[0].capitalize() + self.surname.lower()
