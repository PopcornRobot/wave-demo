from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=100)

class Room(models.Model):
    name = models.CharField(max_length=100)
    page = models.CharField(max_length=100)