# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='deal',
            name='features_benefits',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='deal',
            name='short_desc',
            field=models.CharField(default=b'No Description', max_length=200),
        ),
    ]
