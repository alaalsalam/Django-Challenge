# Generated by Django 4.0.1 on 2022-02-01 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('makeup', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect_us',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='connect_us',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
