# Generated by Django 3.0.5 on 2020-09-12 11:17

import dashboard.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200716_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_x',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_y',
            field=models.CharField(max_length=1000),
        )
    ]
