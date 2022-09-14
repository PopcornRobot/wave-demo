from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=100)
    