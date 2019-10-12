from django.db import models
from django.db.models import Q,QuerySet

class Ss(models.Model):
    name = models.CharField(max_length=45)
    parent = models.ForeignKey('self',related_name='children',blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=750)


class Probe(models.Model):
    t1 = models.CharField(max_length=255)
    desc = models.CharField(max_length=750)


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)

