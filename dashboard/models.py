from django.db import models
from .validators import validate_music_file_extension


class Language(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Map(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='map_title_language', verbose_name="Map Title Language", null=True)
    highlight_x = models.CharField(max_length=200)
    highlight_y = models.CharField(max_length=200)
    pin_x = models.CharField(max_length=200)
    pin_y = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Map'
        verbose_name_plural = 'Maps'


class GeneralMap(models.Model):
    title = models.CharField(max_length=200, unique=True)
    map_x_y = models.CharField(max_length=200)
    zoom = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'General Map'
        verbose_name_plural = 'General Map'


class Sections(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='sections_title_language', verbose_name="Sections Title Language", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'


class Layers(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='layers_title_language', verbose_name="Layers Title Language", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Layer'
        verbose_name_plural = 'Layers'


ARTICLE_TYPE_MONUMENT = 'monument'
ARTICLE_TYPE_MUSEUM = 'museum'
ARTICLE_TYPE_SMALL_OBJECTS = 'small_objects'
ARTICLE_TYPE = (
    (ARTICLE_TYPE_MONUMENT, 'monument'),
    (ARTICLE_TYPE_MUSEUM, 'museum'),
    (ARTICLE_TYPE_SMALL_OBJECTS, 'small_objects')
)


class Articles(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='article_title_language', verbose_name="Article Title Language", null=True)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, null=True, related_name='articles')
    layers = models.ManyToManyField(Layers, blank=True, related_name='articles')
    section = models.ManyToManyField(Sections, blank=True, related_name='articles')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, related_name='articles')
    type = models.CharField(max_length=30, choices=ARTICLE_TYPE)
    main_picture = models.ImageField(upload_to='media/main_pictures/', null=True)
    sequence = models.FloatField()
    brief_description = models.TextField(null=True)
    brief_description_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='article_brief_description_language', verbose_name="Article Brief Description Language", null=True)
    full_description = models.TextField(null=True)
    full_description_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='article_full_description_language', verbose_name="Article Full Description Language", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_text = models.FileField(upload_to='media/audio/', validators=[validate_music_file_extension])
    audio_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='article_audio_language', verbose_name="Article Audio Language", null=True)

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
    title_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='museums_title_language', verbose_name="Museums Title Language", null=True)
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
    sequence = models.FloatField()
    brief_description = models.TextField(null=True)
    brief_description_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='museums_brief_description_language', verbose_name="Museums Brief Description Language", null=True)
    full_description = models.TextField(null=True)
    full_description_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='museums_full_description_language', verbose_name="Museums Full Description Language", null=True)
    audio_text = models.FileField(upload_to='media/audio/', validators=[validate_music_file_extension])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Museum'
        verbose_name_plural = 'Museums'

    def __str__(self):
        return self.title


class Route(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='route_title_language', verbose_name="Route Title Language", null=True)
    route_x = models.CharField(max_length=1000)
    route_y = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'


class Gallery(models.Model):
    image = models.ImageField(upload_to='media/gallery/')
    brief_description = models.TextField()
    brief_description_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='galleries_brief_description_language', verbose_name="Galleries Brief Description Language", null=True)
    sequence = models.FloatField()
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE, blank=True, null=True, related_name='gallery')
    museums = models.ForeignKey(Museums, on_delete=models.CASCADE, blank=True, null=True, related_name='gallery')
    three_d_panoramas = models.FileField(upload_to='media/gallery/')
    three_d_tour = models.FileField(upload_to='media/gallery/')


