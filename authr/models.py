from uuid import uuid4
from .managers import UserManager

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	username = None		# no usernames...
	id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
	email = models.EmailField(verbose_name='email address', unique=True, max_length=100)
	intrests = models.ManyToManyField('bucket.Tag', related_name='users')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	def __str__(self) -> str:
		return self.email

	def __repr__(self) -> str:
		return f"<User {self.email}>"
