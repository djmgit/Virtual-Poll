# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
