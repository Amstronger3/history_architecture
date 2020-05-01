from audiofield.fields import AudioField
from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Map(models.Model):
    title = models.CharField(max_length=200, unique=True)
    highlight_x = models.FloatField(default=0)
    highlight_y = models.FloatField(default=0)
    pin_x = models.FloatField(default=0)
    pin_y = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Map'
        verbose_name_plural = 'Maps'


class GeneralMap(models.Model):
    title = models.CharField(max_length=200, unique=True)
    map_x = models.FloatField(default=0)
    map_y = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'General Map'
        verbose_name_plural = 'General Map'


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
    map = models.ForeignKey(Map, on_delete=models.CASCADE, null=True, related_name='articles')
    layers = models.ManyToManyField(Layers, blank=True, related_name='articles')
    section = models.ManyToManyField(Sections, blank=True, related_name='articles')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, related_name='articles')
    type = models.CharField(max_length=30, choices=ARTICLE_TYPE)
    main_picture = models.ImageField(upload_to='media/main_pictures/', null=True)
    brief_description = models.TextField()
    full_description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_text = AudioField(upload_to='media/audio/', blank=True,
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
    title = models.CharField(max_length=200, unique=True)
    website = models.CharField(max_length=200, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    tickets = models.CharField(max_length=200)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True, related_name='museums')
    map = models.ForeignKey(Map, on_delete=models.CASCADE, null=True, related_name='museums')
    layers = models.ManyToManyField(Layers, blank=True, related_name='museums')
    section = models.ManyToManyField(Sections, blank=True, related_name='museums')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, related_name='museums')
    type = models.CharField(max_length=30, choices=ARTICLE_TYPE)
    main_picture = models.ImageField(upload_to='media/main_pictures/', null=True)
    brief_description = models.TextField()
    full_description = models.TextField(null=True)
    audio_text = AudioField(upload_to='media/audio/', blank=True,
                            ext_whitelist=(".mp3", ".wav", ".ogg"),
                            help_text="Allowed type - .mp3, .wav, .ogg")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Museum'
        verbose_name_plural = 'Museums'

    def __str__(self):
        return self.title


class Route(models.Model):
    title = models.CharField(max_length=200, unique=True)
    route_x = models.FloatField(default=0)
    route_y = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'


class Gallery(models.Model):
    image = models.ImageField(upload_to='media/gallery/')
    brief_description = models.TextField()
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE, null=True, related_name='gallery')
    museums = models.ForeignKey(Museums, on_delete=models.CASCADE, null=True, related_name='gallery')

