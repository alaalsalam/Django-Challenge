# Generated by Django 4.0.2 on 2022-02-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_products_crate_time_products_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/products/%y/%m/%d'),
        ),
    ]