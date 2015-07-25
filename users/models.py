from django.db import models
from django.contrib.auth.models import User
from random_data.models import City


class Citizen(models.Model):
    user = models.OneToOneField(User)
    city = models.ForeignKey(City)
    is_anon = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        return super(Citizen, self).save(*args, **kwargs)


class Mayor(models.Model):
    user = models.OneToOneField(User)
    city = models.ForeignKey(City)