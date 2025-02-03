from django.db import models


# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


class User(models.Model):
    first_interaction = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
