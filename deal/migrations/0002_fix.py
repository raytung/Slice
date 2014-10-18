# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='owner',
            field=models.ManyToManyField(related_name=b'owner', to='UserProfile.Profile'),
            preserve_default=True,
        ),
    ]
