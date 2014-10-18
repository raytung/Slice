# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0001_initial'),
        ('UserProfile', '0008_auto_20141017_0433')
    ]

    operations = [
        migrations.AddField(
            model_name='Deal',
            name='owner',
            field=models.ManyToManyField(related_name=b'owner', to='UserProfile.Profile'),
            preserve_default=True,
        ),
    ]
