# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0007_auto_20141022_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='thumbnail',
            field=models.ImageField(height_field=b'64', width_field=b'64', null=True, upload_to=b'upload_image/'),
        ),
    ]
