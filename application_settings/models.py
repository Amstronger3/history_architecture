from django.db import models


class About(models.Model):
    general_information = models.TextField()
    web_site = models.CharField(max_length=100, unique=True)
    mail = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
