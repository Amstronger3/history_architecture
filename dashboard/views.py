from rest_framework.generics import GenericAPIView
from .models import Articles, Sections, Layers, Museums
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class AllArticles(GenericAPIView):
    serializer_class = ArticlesSerializer

    def get(self, request):
        """
        Get all articles
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Request parameters(url):
            - section_id: int
            - layer_id: int or str if 'all' value (returns articles by all layers)
        Response parameters(String):
                - 'success' -- success
                - 'fail' -- fail

            Response status(int):
                - 200 - success, articles objects
                - 400 - fail. wrong parameters, section or articles doesn`t exist, error message
        """
        section_id = request.GET.get('section_id', None)
        layer_id = request.GET.get('layer_id', None)
        if layer_id and section_id:
            try:
                section = Sections.objects.get(id=section_id)
            except Sections.DoesNotExist:
                result = {'message': 'Section doesnt exist'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            try:
                layer = Layers.objects.all().values_list('id', flat=True) if layer_id == 'all' else Layers.objects.get(id=layer_id)
            except Layers.DoesNotExist:
                result = {'message': 'Layer doesnt exist'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            articles = Articles.objects.filter(section=section, layers__id__in=[layer])
        else:
            if section_id:
                try:
                    section = Sections.objects.get(id=section_id)
                    articles = Articles.objects.filter(section=section)
                except Sections.DoesNotExist:
                    result = {'message': 'Section doesnt exist'}
                    return Response(result, status=status.HTTP_400_BAD_REQUEST)
            elif layer_id:
                try:
                    layer = Layers.objects.all().values_list('id', flat=True) if layer_id == 'all' else Layers.objects.get(id=layer_id)
                    articles = Articles.objects.filter(layers__id__in=[layer])
                except Layers.DoesNotExist:
                    result = {'message': 'Layer doesnt exist'}
                    return Response(result, status=status.HTTP_400_BAD_REQUEST)
            else:
                articles = Articles.objects.all()
        serializer = self.serializer_class(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllMaps(GenericAPIView):
    serializer_class = MapsSerializer

    def get(self, request):
        """
        Get all maps
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Response parameters(String):
                - 'success' -- success

            Response status(int):
                - 200 - success, articles objects
        """
        maps = Map.objects.all()
        serializer = self.serializer_class(maps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetArticle(GenericAPIView):
    serializer_class = FullArticleSerializer

    def get(self, request):
        """
        Get specific article by id
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Request parameters(url):
            - article_id: int

        Response parameters(String):
                - 'success' -- success
                - 'fail' -- fail

            Response status(int):
                - 200 - success, article object
                - 400 - fail. wrong parameters, article object doesnt exist, error message
                - 400 - fail. article id parameter was not inputted, error message
        """
        article_id = request.GET.get('article_id', None)
        if article_id:
            try:
                article = Articles.objects.get(id=article_id)
            except Articles.DoesNotExist:
                result = {'message': 'Article doesnt exist'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
        else:
            result = {'message': 'Article id parameter was not inputted'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(article)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllLayers(GenericAPIView):
    serializer_class = LayersSerializer

    def get(self, request):
        """
        Get all layers
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Response parameters(String):
                - 'success' -- success

            Response status(int):
                - 200 - success, article object
        """
        layers = Layers.objects.all()
        return Response(self.serializer_class(layers, many=True).data, status=status.HTTP_200_OK)


class AllMuseums(GenericAPIView):
    serializer_class = MuseumsSerializer

    def get(self, request):
        """
        Get all museums
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Response parameters(String):
                - 'success' -- success

            Response status(int):
                - 200 - success, museums objects
        """
        museums = Museums.objects.all()
        return Response(self.serializer_class(museums, many=True).data, status=status.HTTP_200_OK)


class GetMuseum(GenericAPIView):
    serializer_class = FullMuseumSerializer

    def get(self, request):
        """
        Get specific museum by id
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Request parameters(url):
            - museum_id: int

        Response parameters(String):
                - 'success' -- success
                - 'fail' -- fail

            Response status(int):
                - 200 - success, article object
                - 400 - fail. wrong parameters, museum object doesnt exist, error message
                - 400 - fail. museum id parameter was not inputted, error message
        """
        museum_id = request.GET.get('museum_id', None)
        if museum_id:
            try:
                museums = Museums.objects.get(id=museum_id)
            except Articles.DoesNotExist:
                result = {'message': 'Museum doesnt exist'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
        else:
            result = {'message': 'Museum id parameter was not inputted'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(museums)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllContent(GenericAPIView):
    serializer_class = AllContentSerializer

    def get_queryset(self):
        model = self.kwargs.get('model')
        return model.objects.all()

    def get_serializer_class(self):
        AllContentSerializer.Meta.model = self.kwargs.get('model')
        return AllContentSerializer

    def get(self, request):
        """
        Get all application content
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Response parameters(String):
                - 'success' -- success

            Response status(int):
                - 200 - success, all application objects
        """

        languages = LanguageSerializer(Language.objects.all(), many=True).data
        maps = MapsSerializer(Map.objects.all(), many=True).data
        general_maps = GeneralMapSerializer(GeneralMap.objects.all(), many=True).data
        sections = SectionsSerializer(Sections.objects.all(), many=True).data
        layers = LayersSerializer(Layers.objects.all(), many=True).data
        articles = FullArticleSerializer(Articles.objects.all(), many=True).data
        prices = PriceSerializer(Price.objects.all(), many=True).data
        museums = FullMuseumSerializer(Museums.objects.all(), many=True).data
        routes = RouteSerializer(Route.objects.all(), many=True).data
        gallery = GallerySerializer(Gallery.objects.all(), many=True).data
        return Response({'languages': languages, 'maps': maps, 'general_maps': general_maps, 'sections': sections,
                         'layers': layers, 'articles': articles, 'prices': prices, 'museums': museums, 'routes': routes,
                         'gallery': gallery}, status=status.HTTP_200_OK)


class AllGeneralMaps(GenericAPIView):
    serializer_class = GeneralMapSerializer

    def get(self, request):
        """
        Get all general maps
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Response parameters(String):
                - 'success' -- success
                - 'fail' -- fail

            Response status(int):
                - 200 - success, articles objects
        """
        generals_maps = GeneralMap.objects.all()
        serializer = self.serializer_class(generals_maps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
