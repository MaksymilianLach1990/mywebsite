from django.db import models
import datetime

# Create your models here.

class Scenes(models.Model):
    class Meta:
        ordering = ('name', 'created_at')

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=300)
    created_at = models.DateField(default=datetime.date.today, db_index=True)

    def __str__(self):
        return f'{self.name}'


class Phrase(models.Model):
    class Meta:
        ordering = ('scenes', 'order')

    scenes = models.ForeignKey(Scenes, models.PROTECT, null=True, blank=True)
    character_name = models.CharField(max_length=100, null=False)
    sentence = models.TextField(max_length=400)
    order = models.IntegerField(unique=True)
    created_at = models.DateField(default=datetime.date.today, db_index=True)

    def __str__(self):
        return f'{self.scenes} - {self.order} - {self.created_at}'


class World(models.Model):
    class Meta:
        ordering = ('world_pl', 'world_fr')

    scenes = models.ForeignKey(Scenes, models.PROTECT, null=True, blank=True)
    world_pl = models.CharField(max_length=100)
    world_fr = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    phonetic = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.world_pl} - {self.world_fr}'