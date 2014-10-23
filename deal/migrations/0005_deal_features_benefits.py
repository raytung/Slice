# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0004_remove_deal_features_benefits'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='features_benefits',
            field=models.TextField(default=b' ', max_length=500),
            preserve_default=True,
        ),
    ]
