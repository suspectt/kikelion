# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 18:35
from __future__ import unicode_literals

import board.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[board.models.content_validator]),
        ),
    ]