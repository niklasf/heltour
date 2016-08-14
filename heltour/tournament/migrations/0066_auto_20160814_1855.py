# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0065_auto_20160814_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roundchange',
            name='action',
            field=models.CharField(choices=[('register', 'Register'), ('withdraw', 'Withdraw'), ('half-point-bye', 'Half-Point Bye')], max_length=255),
        ),
    ]
