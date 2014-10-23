# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0009_auto_20141022_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='thumbnail_height',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='thumbnail_width',
        ),
        migrations.AlterField(
            model_name='deal',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(upload_to=b'upload_image/'),
        ),
    ]
