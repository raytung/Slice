# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '__first__'),
        ('UserProfile', '0006_auto_20141011_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bookmarks',
            field=models.ManyToManyField(related_name=b'bookmark', to='deal.Deal'),
            preserve_default=True,
        ),
    ]
