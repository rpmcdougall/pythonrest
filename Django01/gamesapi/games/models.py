from django.db import models

# Create your models here.

class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

class Player(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200,blank=False, default='Anonymoose')
    age = models.CharField(max_length=200,blank=False, default='100')

    class Meta:
        ordering = ('name',)