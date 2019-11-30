from django.db import models

class Medee(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    zurag = models.ImageField(upload_to="medee_zurag")
    liketoo = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')