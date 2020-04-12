from django.conf.urls import url
from .views import AppInfo

urlpatterns = [
    url(r'^app_info/$', AppInfo.as_view()),
]
