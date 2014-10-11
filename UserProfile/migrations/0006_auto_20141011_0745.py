# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '__first__'),
        ('UserProfile', '0005_remove_profile_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view_date', models.DateTimeField(auto_now=True)),
                ('deal', models.ForeignKey(to='deal.Deal')),
                ('user', models.ForeignKey(to='UserProfile.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profile',
            name='viewing_history',
            field=models.ManyToManyField(to='deal.Deal', through='UserProfile.History'),
            preserve_default=True,
        ),
    ]
