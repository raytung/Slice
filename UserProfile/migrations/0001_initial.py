# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_picture', models.FileField(null=True, upload_to=b'UserProfile/static/images/profile', blank=True)),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('mobile_number', models.CharField(max_length=20, blank=True)),
                ('contact_info', models.TextField(max_length=500, blank=True)),
                ('consecutive_incorrect_login_counts', models.PositiveIntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('account', models.OneToOneField(primary_key=True, serialize=False, to='account.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
