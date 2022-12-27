from django.db import models

class Stats(models.Model):
    strength = models.IntegerField(max=10)
    agility = models.IntegerField(max=10)
    intelligence = models.IntegerField(max=10)
    cool = models.IntegerField(max=10)
    perception = models.IntegerField(max=10)
    luck = models.IntegerField(max=10)
    endurance = models.IntegerField(max=10)
    willpower = models.IntegerField(max=10)

    