# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0002_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='deal',
        ),
        migrations.RemoveField(
            model_name='history',
            name='user',
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
