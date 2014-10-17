# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0007_profile_bookmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bookmarks',
            field=models.ManyToManyField(related_name=b'bookmarks', to=b'deal.Deal'),
        ),
    ]
