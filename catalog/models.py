from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    publish_year = models.IntegerField()
    artist_id = models.IntegerField(null=True, blank=True, db_index=True)

    def __unicode__(self):
        # ``artist_name`` is added in the query, with ``extra``
        return "{} [{}]".format(self.title, self.artist_name)


class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, related_name='songs')
