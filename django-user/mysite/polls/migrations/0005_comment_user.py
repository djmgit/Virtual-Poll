# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_choice_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(default='none', max_length=200),
        ),
    ]