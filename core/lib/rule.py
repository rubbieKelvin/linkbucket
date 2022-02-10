import re
from maprule.fields import Field
from typing import Pattern

class RegExField(Field):
	NICK = "match"
	REGEX:Pattern|None = None
	
	def __init__(self, nullable: bool = False):
		super().__init__(nullable=nullable)

	def compare(self, other: str|None) -> bool:
		self.error = f"{self.name}, \"{other}\" is not a valid {self.NICK}"
		if (not self.REGEX) or (self.nullable and other == None):
			return True

		if other == None:
			return False

		return bool(re.fullmatch(self.REGEX, other))

class EmailField(RegExField):
	NICK = "email"
	REGEX: Pattern|None = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

class PasswordField(Field):
	""" requires up to 6 characters and atleast 2 digits
	"""
	def compare(self, other: str) -> bool:
		self.error = f"{self.name} should have at least 6 characters"
		return len(other) >= 6
