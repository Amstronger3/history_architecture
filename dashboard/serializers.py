from rest_framework import serializers
from .models import Language, Map, GeneralMap, Sections, Layers, Articles, Price, Museums, Route, Gallery


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'title')


class LayersSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('title_func')
    title_eng = serializers.SerializerMethodField('title_eng_func')
    title_rus = serializers.SerializerMethodField('title_rus_func')

    def title_func(self, obj):
        if not '*****' in obj.title:
            return obj.title

    def title_eng_func(self, obj):
        if '*****' in obj.title:
            return obj.title.split('*****')[0].strip()

    def title_rus_func(self, obj):
        if '*****' in obj.title:
            return obj.title.split('*****')[1].strip()

    class Meta:
        model = Layers
        fields = ('id', 'title', 'title_eng', 'title_rus', 'title_language',)


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
    title = serializers.SerializerMethodField('title_func')
    title_eng = serializers.SerializerMethodField('title_eng_func')
    title_rus = serializers.SerializerMethodField('title_rus_func')

    def title_func(self, obj):
        if not '*****' in obj.title:
            return obj.title

    def title_eng_func(self, obj):
        if '*****' in obj.title:
            return obj.title.split('*****')[0].strip()

    def title_rus_func(self, obj):
        if '*****' in obj.title:
            return obj.title.split('*****')[1].strip()

    class Meta:
        model = Map
        fields = (
            'id', 'title', 'title_eng', 'title_rus', 'highlight_x', 'highlight_y', 'pin_x', 'pin_y', 'title_language')


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'title', 'route_x', 'route_y', 'title_language')


class ArticlesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('image_function')
    coordinates = serializers.SerializerMethodField('coordinates_function')
    layer_ids = serializers.SerializerMethodField('layer_idsFunc')
    sections = serializers.SerializerMethodField('sectionsFunc')
    title = serializers.SerializerMethodField('title_func')
    title_eng = serializers.SerializerMethodField('title_eng_func')
    title_rus = serializers.SerializerMethodField('title_rus_func')

    brief_description = serializers.SerializerMethodField('brief_description_func')
    brief_description_drop_on_eng = serializers.SerializerMethodField('brief_description_eng_func')
    brief_description_drop_on_rus = serializers.SerializerMethodField('brief_description_rus_func')

    full_description = serializers.SerializerMethodField('full_description_func')
    full_description_eng = serializers.SerializerMethodField('full_description_eng_func')
    full_description_rus = serializers.SerializerMethodField('full_description_rus_func')

    def coordinates_function(self, obj):
        return MapsSerializer(obj.map).data

    def image_function(self, obj):
        image = obj.main_picture.url if obj.main_picture else None
        return image

    def layer_idsFunc(self, obj):
        return LayersSerializer(obj.layers, many=True).data

    def sectionsFunc(self, obj):
        return SectionsSerializer(obj.section, many=True).data

    def title_func(self, obj):
        if not '*****' in obj.title:
            return obj.title

    def title_eng_func(self, obj):
        if '*****' in obj.title:
            return obj.title.split('*****')[0].strip()

    def title_rus_func(self, obj):
        if '*****' in obj.title:
            return obj.title.split('*****')[1].strip()

    def brief_description_func(self, obj):
        if not '*****' in obj.brief_description:
            return obj.brief_description

    def brief_description_eng_func(self, obj):
        if '*****' in obj.brief_description:
            return obj.brief_description.split('*****')[0].strip()

    def brief_description_rus_func(self, obj):
        if '*****' in obj.brief_description:
            return obj.brief_description.split('*****')[1].strip()

    def full_description_func(self, obj):
        if not '*****' in str(obj.full_description):
            return obj.full_description

    def full_description_eng_func(self, obj):
        if '*****' in str(obj.full_description):
            return obj.full_description.split('*****')[0].strip()

    def full_description_rus_func(self, obj):
        if '*****' in str(obj.full_description):
            return obj.full_description.split('*****')[1].strip()

    class Meta:
        model = Articles
        fields = ('id', 'title', 'title_eng',
                  'title_rus', 'image', 'layer_ids', 'brief_description', 'brief_description_drop_on_eng',
                  'brief_description_drop_on_rus', 'full_description', 'full_description_eng', 'full_description_rus',
                  'coordinates', 'sequence', 'sections',
                  'title_language', 'brief_description_language', 'full_description_language', 'audio_language')


class MuseumsSerializer(ArticlesSerializer):
    title = serializers.SerializerMethodField('title_func')
    title_eng = serializers.SerializerMethodField('title_eng_func')
    title_rus = serializers.SerializerMethodField('title_rus_func')

    brief_description = serializers.SerializerMethodField('brief_description_func')
    brief_description_drop_on_eng = serializers.SerializerMethodField('brief_description_eng_func')
    brief_description_drop_on_rus = serializers.SerializerMethodField('brief_description_rus_func')

    full_description = serializers.SerializerMethodField('full_description_func')
    full_description_eng = serializers.SerializerMethodField('full_description_eng_func')
    full_description_rus = serializers.SerializerMethodField('full_description_rus_func')

    def title_func(self, obj):
        if not '*****' in obj.title:
            return obj.title

    def title_eng_func(self, obj):
        if '*****' in obj.title:
            return obj.title.split('*****')[0].strip()

    def title_rus_func(self, obj):
        if '*****' in obj.title:
            return obj.title.split('*****')[1].strip()

    def brief_description_func(self, obj):
        if not '*****' in obj.brief_description:
            return obj.brief_description

    def brief_description_eng_func(self, obj):
        if '*****' in obj.brief_description:
            return obj.brief_description.split('*****')[0].strip()

    def brief_description_rus_func(self, obj):
        if '*****' in obj.brief_description:
            return obj.brief_description.split('*****')[1].strip()

    def full_description_func(self, obj):
        if not '*****' in str(obj.full_description):
            return obj.full_description

    def full_description_eng_func(self, obj):
        if '*****' in str(obj.full_description):
            return obj.full_description.split('*****')[0].strip()

    def full_description_rus_func(self, obj):
        if '*****' in str(obj.full_description):
            return obj.full_description.split('*****')[1].strip()

    class Meta(ArticlesSerializer.Meta):
        model = Museums
        fields = ('id', 'title', 'title_eng',
                  'title_rus', 'image', 'layer_ids', 'brief_description', 'brief_description_drop_on_eng',
                  'brief_description_drop_on_rus', 'full_description', 'full_description_eng', 'full_description_rus',
                  'coordinates', 'sequence', 'sections', 'title_language', 'brief_description_language',
                  'full_description_language')


class GallerySerializer(serializers.ModelSerializer):
    gallery_picture = serializers.SerializerMethodField('gallery_picture_function')
    three_d_panoramas_file = serializers.SerializerMethodField('three_d_panoramas_function')
    three_d_tour_file = serializers.SerializerMethodField('three_d_tour_function')
    image_in_360_file = serializers.SerializerMethodField('image_in_360_file_function')
    brief_description = serializers.SerializerMethodField('brief_description_func')
    brief_description_drop_on_eng = serializers.SerializerMethodField('brief_description_eng_func')
    brief_description_drop_on_rus = serializers.SerializerMethodField('brief_description_rus_func')

    def gallery_picture_function(self, obj):
        image = obj.image.url if obj.image else None
        return image

    def three_d_panoramas_function(self, obj):
        three_d_panoramas = obj.three_d_panoramas.url if obj.three_d_panoramas.name else None
        return three_d_panoramas

    def three_d_tour_function(self, obj):
        three_d_tour = obj.three_d_tour.url if obj.three_d_tour.name else None
        return three_d_tour

    def image_in_360_file_function(self, obj):
        image_in_360 = obj.image_in_360.url if obj.image_in_360.name else None
        return image_in_360

    def brief_description_func(self, obj):
        if not '*****' in obj.brief_description:
            return obj.brief_description

    def brief_description_eng_func(self, obj):
        if '*****' in obj.brief_description:
            return obj.brief_description.split('*****')[0].strip()

    def brief_description_rus_func(self, obj):
        if '*****' in obj.brief_description:
            return obj.brief_description.split('*****')[1].strip()

    class Meta:
        model = Gallery
        fields = ('id', 'gallery_picture', 'brief_description', 'brief_description_drop_on_eng',
                  'brief_description_drop_on_rus', 'sequence', 'brief_description_language',
                  'three_d_panoramas_file', 'three_d_tour_file', 'image_in_360_file')


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
