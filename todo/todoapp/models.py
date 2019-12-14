from django.db import models

class Todo(models.Model):
    data = models.TextField()