# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0008_auto_20141017_0433'),
        ('deal', '0002_deal_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('deal', models.ForeignKey(to='deal.Deal')),
                ('user', models.ForeignKey(related_name=b'current_user', to='UserProfile.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
