# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '__first__')
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('short_desc', models.CharField(default=b'No Description', max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('cost_per_unit', models.DecimalField(max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('available_units', models.PositiveIntegerField(default=1)),
                ('savings', models.DecimalField(default=1, max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('num_units', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField(help_text=b'MM/DD/YYYY hh:mm')),
                ('end_date', models.DateTimeField(help_text=b'MM/DD/YYYY hh:mm')),
                ('state', models.CharField(max_length=4, choices=[(b'CMNG', b'Coming up'), (b'STRT', b'Started'), (b'ENDD', b'Ended'), (b'CNCL', b'Canceled'), (b'DLYD', b'Delayed')])),
                ('delivery_method', models.TextField()),
                ('min_pledge_amount', models.PositiveIntegerField()),
                ('time_posted', models.DateTimeField(auto_now=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='deal.Category')),
                ('owner', models.ForeignKey(to='UserProfile.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SearchTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='deal',
            name='search_tags',
            field=models.ManyToManyField(to='deal.SearchTag'),
            preserve_default=True,
        ),
    ]
