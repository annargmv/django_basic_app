# Codes from https://wsvincent.com/django-rest-framework-react-tutorial/
# todos/models.py
from django.db import models


class Backend(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title