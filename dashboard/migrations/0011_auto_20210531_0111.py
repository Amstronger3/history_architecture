# Generated by Django 3.0.5 on 2021-05-30 22:11

import dashboard.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20210531_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='audio_language',
            field=models.ManyToManyField(blank=True, related_name='article_audio_language', to='dashboard.Language', verbose_name='Article Audio Language'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='brief_description_language',
            field=models.ManyToManyField(blank=True, related_name='article_brief_description_language', to='dashboard.Language', verbose_name='Article Brief Description Language'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_description_language',
            field=models.ManyToManyField(blank=True, related_name='article_full_description_language', to='dashboard.Language', verbose_name='Article Full Description Language'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title_language',
            field=models.ManyToManyField(blank=True, related_name='article_title_language', to='dashboard.Language', verbose_name='Article Title Language'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='brief_description_language',
            field=models.ManyToManyField(blank=True, related_name='galleries_brief_description_language', to='dashboard.Language', verbose_name='Galleries Brief Description Language'),
        ),
        migrations.AlterField(
            model_name='layers',
            name='title_language',
            field=models.ManyToManyField(blank=True, related_name='layers_title_language', to='dashboard.Language', verbose_name='Layers Title Language'),
        ),
        migrations.AlterField(
            model_name='map',
            name='title_language',
            field=models.ManyToManyField(blank=True, related_name='map_title_language', to='dashboard.Language', verbose_name='Map Title Language'),
        ),
        migrations.AlterField(
            model_name='museums',
            name='brief_description_language',
            field=models.ManyToManyField(blank=True, related_name='museums_brief_description_language', to='dashboard.Language', verbose_name='Museums Brief Description Language'),
        ),
        migrations.AlterField(
            model_name='museums',
            name='full_description_language',
            field=models.ManyToManyField(blank=True, related_name='museums_full_description_language', to='dashboard.Language', verbose_name='Museums Full Description Language'),
        ),
        migrations.AlterField(
            model_name='museums',
            name='title_language',
            field=models.ManyToManyField(blank=True, related_name='museums_title_language', to='dashboard.Language', verbose_name='Museums Title Language'),
        ),
        migrations.AlterField(
            model_name='route',
            name='title_language',
            field=models.ManyToManyField(blank=True, related_name='route_title_language', to='dashboard.Language', verbose_name='Route Title Language'),
        ),
        migrations.AlterField(
            model_name='sections',
            name='title_language',
            field=models.ManyToManyField(blank=True, related_name='sections_title_language', to='dashboard.Language', verbose_name='Sections Title Language'),
        ),
    ]
