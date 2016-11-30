# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_employee_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='entry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Entry'),
            preserve_default=False,
        ),
    ]