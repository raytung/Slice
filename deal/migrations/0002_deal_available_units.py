# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0001_initial'),
        ('UserProfile', '0006_auto_20141011_0745')
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='available_units',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
