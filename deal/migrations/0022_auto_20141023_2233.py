# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0021_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'upload_image/', blank=True),
        ),
    ]
