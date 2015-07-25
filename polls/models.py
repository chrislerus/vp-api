from django.db import models
from users.models import Citizen, Mayor


class Question(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=256)
    author = models.ForeignKey(Citizen)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=256)
    author = models.ForeignKey(Mayor)
    question = models.ForeignKey(Question)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Message(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=256)
    author = models.ForeignKey(Mayor)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)