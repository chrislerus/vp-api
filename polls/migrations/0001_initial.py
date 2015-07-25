# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_citizen_is_anon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime_created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=256)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to='users.Mayor')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime_created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=256)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to='users.Citizen')),
            ],
        ),
    ]
