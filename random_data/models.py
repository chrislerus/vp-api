from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField(default=0)


class State(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField(default=0)


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField(default=0)
    state = models.ForeignKey(to="State")

