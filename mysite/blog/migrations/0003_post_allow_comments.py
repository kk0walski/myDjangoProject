# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170926_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='allow_comments',
            field=models.BooleanField(default=True),
        ),
    ]
