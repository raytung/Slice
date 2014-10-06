# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deal'
        db.create_table(u'deal_deal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('cost_per_unit', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('num_units', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('start_date', self.gf('django.db.models.fields.TimeField')()),
            ('end_date', self.gf('django.db.models.fields.TimeField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('delivery_method', self.gf('django.db.models.fields.TextField')()),
            ('min_pledge_amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('time_posted', self.gf('django.db.models.fields.TimeField')()),
            ('last_modified_date', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'deal', ['Deal'])


    def backwards(self, orm):
        # Deleting model 'Deal'
        db.delete_table(u'deal_deal')


    models = {
        u'deal.deal': {
            'Meta': {'object_name': 'Deal'},
            'cost_per_unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'delivery_method': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'end_date': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_date': ('django.db.models.fields.TimeField', [], {}),
            'min_pledge_amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'num_units': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'start_date': ('django.db.models.fields.TimeField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'time_posted': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['deal']