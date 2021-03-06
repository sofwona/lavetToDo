from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=20)
	text =models.TextField(max_length=300)
	created_at=models.DateTimeField(default=datetime.now(),blank=True)
	def __str__(self):
		return self.title
