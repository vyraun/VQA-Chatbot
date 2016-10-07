# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vicki', '0002_auto_20161007_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vicki.UserDetail'),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vicki.UserDetail'),
        ),
    ]