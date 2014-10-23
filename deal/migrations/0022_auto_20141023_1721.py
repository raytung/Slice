# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0021_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='non_monetary_condition',
            field=models.TextField(max_length=800, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='cost_per_unit',
            field=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='deal',
            name='savings_per_unit',
            field=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
