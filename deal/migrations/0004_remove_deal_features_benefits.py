# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0003_auto_20141022_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='features_benefits',
        ),
    ]
