# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0004_deal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'upload_image/')),
                ('deal', models.ForeignKey(related_name=b'image', to='deal.Deal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='deal',
            name='image',
        ),
    ]
