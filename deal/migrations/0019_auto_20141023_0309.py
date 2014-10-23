# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0018_auto_20141023_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(upload_to=b'upload_image/', blank=True),
        ),
    ]
