# Generated by Django 4.0.1 on 2022-01-28 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Descreption',
            field=models.TextField(default='not found'),
        ),
        migrations.AddField(
            model_name='products',
            name='Exipir_data',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='products',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]