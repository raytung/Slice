# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0006_deal_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='thumbnail',
            field=models.ImageField(height_field=64, width_field=64, null=True, upload_to=b'upload_image/'),
        ),
    ]
