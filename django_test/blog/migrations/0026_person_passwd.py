# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_userform_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='passwd',
            field=models.CharField(default=123, max_length=128),
            preserve_default=False,
        ),
    ]
