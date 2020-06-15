# Generated by Django 3.0.5 on 2020-05-27 11:44

import dashboard.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200503_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='audio_text',
            field=models.FileField(default=False, upload_to='media/audio/', validators=[dashboard.validators.validate_music_file_extension]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museums',
            name='audio_text',
            field=models.FileField(default=False, upload_to='media/audio/', validators=[dashboard.validators.validate_music_file_extension]),
            preserve_default=False,
        ),
    ]