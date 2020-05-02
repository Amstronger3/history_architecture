# Generated by Django 3.0.5 on 2020-05-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200503_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalmap',
            name='sequence',
        ),
        migrations.AddField(
            model_name='articles',
            name='sequence',
            field=models.FloatField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museums',
            name='sequence',
            field=models.FloatField(default=False),
            preserve_default=False,
        ),
    ]
