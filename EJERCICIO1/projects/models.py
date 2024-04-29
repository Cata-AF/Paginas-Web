import uuid
import email
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
# Create your models here.
from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField(null=True, blank=True)
    document = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name