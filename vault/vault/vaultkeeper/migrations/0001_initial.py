# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('cardID', models.AutoField(serialize=False, primary_key=True)),
                ('ownerID', models.IntegerField()),
                ('bankID', models.IntegerField()),
                ('debit', models.FloatField(default=0)),
                ('credit', models.FloatField(default=0)),
                ('currency', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CentralAccount',
            fields=[
                ('centralAccountID', models.AutoField(serialize=False, primary_key=True)),
                ('debit', models.FloatField(default=0)),
                ('credit', models.FloatField(default=0)),
                ('currency', models.CharField(max_length=10)),
                ('accountName', models.CharField(max_length=50)),
                ('accountCountry', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transactionID', models.IntegerField()),
                ('cardID', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('authorized', models.BooleanField(default=False)),
                ('settled', models.BooleanField(default=False)),
                ('merchant_name', models.CharField(max_length=50)),
                ('merchant_country', models.CharField(max_length=10)),
                ('merchant_city', models.CharField(max_length=50)),
                ('merchant_mcc', models.IntegerField()),
                ('transaction_currency', models.CharField(max_length=10)),
                ('transaction_amount', models.FloatField(default=0.0)),
                ('billing_currency', models.CharField(max_length=10)),
                ('billing_amount', models.FloatField(default=0.0)),
                ('settlement_currency', models.CharField(max_length=10)),
                ('settlement_amount', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
