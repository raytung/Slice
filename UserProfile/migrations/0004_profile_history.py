# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '__first__'),
        ('UserProfile', '0003_auto_20141011_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='history',
            field=models.ManyToManyField(to='deal.Deal'),
            preserve_default=True,
        ),
    ]
