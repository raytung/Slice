# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pledge', '0002_auto_20141012_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commitment',
            name='last_modified_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='commitment',
            name='requests',
            field=models.TextField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='commitment',
            name='time_commited',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
