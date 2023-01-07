from django.db import models
from django.conf import settings
from .stats import Stats


class Player(models.Model):
    __object_type__ = 'character'
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)

    health_points = models.FloatField(max=1000)
    action_points = models.IntegerField(max=25)

    biography = 0# TODO: characteristics growth through the game

    appearance = 0# TODO: one to one field to appearance model
    player_class = 0# TODO: one to one field to character class model
    body_type = models.CharField(max_length=100)

    
    stats = models.OneToOneField(
        Stats,
        on_delete=models.CASCADE,
    )
    skills = 0# TODO: one to many to skills model

    stash = 0# TODO: one to one field to stash model
    inventory = 0# TODO: one to one field to inventory model
    implants = 0# TODO: one to many field to implants model
    
    mount = 0# TODO: one to many field to mount model
    summon = 0# TODO: one to many field to summon model

    location = 0# TODO: one to one field to location model [[],[],[]]


    # @property
    # def get_perks(self):
    #     return biography.perks + implants.perks + stats.perks

    @property
    def summary_resist(self):
        for item in self.inventory.get_equiped_items:
            item.get_resistance



    #TODO: add separate model for perks

