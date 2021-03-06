from django.conf.urls import url
from .views import AllArticles, AllMaps, GetArticle, AllLayers, AllMuseums, GetMuseum, AllContent, AllGeneralMaps, \
    AllRoutes, AllContentShortened

urlpatterns = [
    url(r'^all_articles/$', AllArticles.as_view()),
    url(r'^all_museums/$', AllMuseums.as_view()),
    url(r'^all_maps/$', AllMaps.as_view()),
    url(r'^all_layers/$', AllLayers.as_view()),
    url(r'^get_article/$', GetArticle.as_view()),
    url(r'^get_museum/$', GetMuseum.as_view()),
    url(r'^all_content/$', AllContent.as_view()),
    url(r'^all_content_shortened/$', AllContentShortened.as_view()),
    url(r'^all_general_maps/$', AllGeneralMaps.as_view()),
    url(r'^all_routes/$', AllRoutes.as_view())

]
