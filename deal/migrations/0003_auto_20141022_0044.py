# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0002_deal_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='savings',
            new_name='savings_unit',
        ),
        migrations.AddField(
            model_name='deal',
            name='features_benefits',
            field=models.TextField(default=b' ', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='short_desc',
            field=models.CharField(default=b' ', max_length=200),
        ),
    ]
