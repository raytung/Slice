# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '__first__'),
        ('UserProfile', '0006_auto_20141011_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('units', models.PositiveIntegerField()),
                ('time_commited', models.DateTimeField()),
                ('requests', models.TextField(max_length=200)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('deal', models.ForeignKey(to='deal.Deal')),
                ('user', models.ForeignKey(to='UserProfile.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
