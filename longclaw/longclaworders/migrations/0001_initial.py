# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('longclawproducts', '0001_initial'),
        (settings.PRODUCT_VARIANT_MODEL.split(".")[0], '0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('line_1', models.CharField(max_length=128)),
                ('line_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('postcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Submitted'), (2, 'Fulfilled'), (3, 'Cancelled')], default=1)),
                ('status_note', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('billing_address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_billing_address', to='longclaworders.Address')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_shipping_address', to='longclaworders.Address')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='longclaworders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.PRODUCT_VARIANT_MODEL)),
            ],
        ),
    ]
