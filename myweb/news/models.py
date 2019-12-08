from django.db import models

from django.contrib.auth.models import User

class Medee(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    zurag = models.ImageField(upload_to="medee_zurag")
    liketoo = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


class LikeCounter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medee = models.ForeignKey(Medee, on_delete=models.CASCADE)
    liked_date = models.DateTimeField('date liked')