# Generated by Django 3.0.4 on 2020-03-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='museums',
            options={'verbose_name': 'Museum', 'verbose_name_plural': 'Museums'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Price', 'verbose_name_plural': 'Prices'},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name': 'Route', 'verbose_name_plural': 'Routes'},
        ),
        migrations.AddField(
            model_name='map',
            name='title',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
