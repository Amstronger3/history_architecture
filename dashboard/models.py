from audiofield.fields import AudioField
from django.db import models


class Map(models.Model):
    title = models.CharField(max_length=200, unique=True)
    highlight_x = models.IntegerField(default=0)
    highlight_y = models.IntegerField(default=0)
    pin_x = models.IntegerField(default=0)
    pin_y = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Map'
        verbose_name_plural = 'Maps'


class Sections(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'


class Layers(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Layer'
        verbose_name_plural = 'Layers'


ARTICLE_TYPE_MONUMENT = 'monument'
ARTICLE_TYPE_MUSEUM = 'museum'
ARTICLE_TYPE = (
    (ARTICLE_TYPE_MONUMENT, 'monument'),
    (ARTICLE_TYPE_MUSEUM, 'museum')
)


class Articles(models.Model):
    title = models.CharField(max_length=200, unique=True)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, null=True)
    layers = models.ManyToManyField(Layers, blank=True, related_name='articles')
    section = models.ManyToManyField(Sections, blank=True, related_name='articles')
    type = models.CharField(max_length=30, choices=ARTICLE_TYPE)
    main_picture = models.ImageField(upload_to='media/article_main_pictures/')
    gallery = models.ImageField(upload_to='media/article_gallery/')
    brief_description = models.TextField()
    full_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    audio_text = AudioField(upload_to='media/article_audio/', blank=True,
                            ext_whitelist=(".mp3", ".wav", ".ogg"),
                            help_text="Allowed type - .mp3, .wav, .ogg")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Price(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'


class Museums(models.Model):
    website = models.CharField(max_length=200, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    tickets = models.CharField(max_length=200)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Museum'
        verbose_name_plural = 'Museums'

    def __str__(self):
        return self.website


class Route(models.Model):
    title = models.CharField(max_length=200, unique=True)
    route_x = models.CharField(max_length=200)
    route_y = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

