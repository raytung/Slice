# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0004_profile_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='history',
        ),
    ]
