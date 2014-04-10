from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    is_band = models.BooleanField(default=False)

