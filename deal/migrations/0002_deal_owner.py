# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0008_auto_20141017_0433'),
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='owner',
            field=models.ForeignKey(default=1, to='UserProfile.Profile'),
            preserve_default=False,
        ),
    ]
