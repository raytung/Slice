# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0005_auto_20141022_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'upload_image/'),
            preserve_default=True,
        ),
    ]
