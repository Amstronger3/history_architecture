from rest_framework import serializers
from .models import Language, Map, GeneralMap, Sections, Layers, Articles, Price, Museums, Route, Gallery


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'title')


class LayersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Layers
        fields = ('id', 'title', 'title_language')


class GeneralMapSerializer(serializers.ModelSerializer):
    general_map_x_y = serializers.SerializerMethodField('general_map_x_yFunc')

    def general_map_x_yFunc(self, obj):
        return [x.strip() for x in obj.map_x_y.split(',')]

    class Meta:
        model = GeneralMap
        fields = ('id', 'title', 'general_map_x_y')


class SectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sections
        fields = ('id', 'title', 'title_language')


class MapsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Map
        fields = ('id', 'title', 'highlight_x', 'highlight_y', 'pin_x', 'pin_y', 'title_language')


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ('id', 'title', 'route_x', 'route_y', 'title_language')


class ArticlesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('image_function')
    coordinates = serializers.SerializerMethodField('coordinates_function')
    layer_ids = serializers.SerializerMethodField('layer_idsFunc')
    sections = serializers.SerializerMethodField('sectionsFunc')

    def coordinates_function(self, obj):
        return MapsSerializer(obj.map).data

    def image_function(self, obj):
        image = obj.main_picture.url if obj.main_picture else None
        return image

    def layer_idsFunc(self, obj):
        return LayersSerializer(obj.layers, many=True).data

    def sectionsFunc(self, obj):
        return SectionsSerializer(obj.section, many=True).data

    class Meta:
        model = Articles
        fields = ('id', 'title', 'image', 'layer_ids', 'brief_description', 'coordinates', 'sequence', 'sections', 'title_language', 'brief_description_language', 'full_description_language', 'audio_language')


class MuseumsSerializer(ArticlesSerializer):

    class Meta(ArticlesSerializer.Meta):
        model = Museums
        fields = ('id', 'title', 'image', 'layer_ids', 'brief_description', 'coordinates', 'sequence', 'sections', 'title_language', 'brief_description_language', 'full_description_language')


class GallerySerializer(serializers.ModelSerializer):

    gallery_picture = serializers.SerializerMethodField('gallery_picture_function')

    def gallery_picture_function(self, obj):
        image = obj.image.url if obj.image else None
        return image

    class Meta:
        model = Gallery
        fields = ('id', 'gallery_picture', 'brief_description', 'sequence', 'brief_description_language')


class FullArticleSerializer(ArticlesSerializer):

    gallery = serializers.SerializerMethodField('gallery_function')

    def gallery_function(self, obj):
        return GallerySerializer(obj.gallery, many=True).data

    audiofile = serializers.SerializerMethodField('audiofile_function')

    def audiofile_function(self, obj):
        audiofile = obj.audio_text.url if obj.audio_text else None
        return audiofile

    class Meta(ArticlesSerializer.Meta):
        model = Articles
        fields = ArticlesSerializer.Meta.fields + ('full_description', 'language', 'gallery', 'audiofile',)


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('id', 'title', 'price')


class FullMuseumSerializer(MuseumsSerializer):

    museum_price = serializers.SerializerMethodField('museum_price_function')

    def museum_price_function(self, obj):
        return PriceSerializer(obj.price).data

    gallery = serializers.SerializerMethodField('gallery_function')

    def gallery_function(self, obj):
        return GallerySerializer(obj.gallery, many=True).data

    audiofile = serializers.SerializerMethodField('audiofile_function')

    def audiofile_function(self, obj):
        audiofile = obj.audio_text.url if obj.audio_text else None
        return audiofile

    class Meta(MuseumsSerializer.Meta):
        model = Museums
        fields = MuseumsSerializer.Meta.fields + ('website', 'tickets', 'museum_price', 'full_description', 'language',
                                                  'gallery', 'start_time', 'end_time', 'audiofile',)


# class AllContentSerializer(serializers.ModelSerializer):
#
#     languages = serializers.SerializerMethodField('languages_function')
#     maps = serializers.SerializerMethodField('maps_function')
#     general_maps = serializers.SerializerMethodField('general_maps_function')
#     sections = serializers.SerializerMethodField('sections_function')
#     layers = serializers.SerializerMethodField('layers_function')
#     articles = serializers.SerializerMethodField('articles_function')
#     prices = serializers.SerializerMethodField('prices_function')
#     museums = serializers.SerializerMethodField('museums_function')
#     routes = serializers.SerializerMethodField('routes_function')
#     gallery = serializers.SerializerMethodField('gallery_function')
#
#     def languages_function(self):
#         return LanguageSerializer(Language.objects.all(), many=True).data
#
#     def maps_function(self):
#         return MapsSerializer(Map.objects.all(), many=True).data
#
#     def general_maps_function(self):
#         return GeneralMapSerializer(GeneralMap.objects.all(), many=True).data
#
#     def sections_function(self):
#         return SectionsSerializer(Sections.objects.all(), many=True).data
#
#     def layers_function(self):
#         return LayersSerializer(Layers.objects.all(), many=True).data
#
#     def articles_function(self):
#         return FullArticleSerializer(Articles.objects.all(), many=True).data
#
#     def prices_function(self):
#         return PriceSerializer(Price.objects.all(), many=True).data
#
#     def museums_function(self):
#         return FullMuseumSerializer(Museums.objects.all(), many=True).data
#
#     def routes_function(self):
#         return RouteSerializer(Route.objects.all(), many=True).data
#
#     def gallery_function(self):
#         return GallerySerializer(Gallery.objects.all(), many=True).data



