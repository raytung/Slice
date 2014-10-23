# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '__first__'),
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view_date', models.DateTimeField()),
                ('deal', models.ForeignKey(to='deal.Deal')),
                ('user', models.ForeignKey(to='UserProfile.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
