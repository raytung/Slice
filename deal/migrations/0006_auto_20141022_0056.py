# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0005_deal_features_benefits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='savings_unit',
            new_name='savings_per_unit',
        ),
    ]
