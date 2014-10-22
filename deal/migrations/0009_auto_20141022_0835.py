# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0008_auto_20141022_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='thumbnail_height',
            field=models.PositiveIntegerField(default=b'64', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deal',
            name='thumbnail_width',
            field=models.PositiveIntegerField(default=b'64', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'upload_image/'),
        ),
    ]
