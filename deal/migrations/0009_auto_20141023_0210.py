# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0008_auto_20141022_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='end_date',
            field=models.DateTimeField(help_text=b'dd/MM/YYYY hh:mm'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='features_benefits',
            field=models.TextField(default=b' ', max_length=500),
        ),
        migrations.AlterField(
            model_name='deal',
            name='short_desc',
            field=models.CharField(default=b' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='deal',
            name='start_date',
            field=models.DateTimeField(help_text=b'dd/MM/YYYY hh:mm'),
        ),
    ]
