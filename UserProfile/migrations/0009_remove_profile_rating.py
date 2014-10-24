# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0008_auto_20141017_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='rating',
        ),
    ]
