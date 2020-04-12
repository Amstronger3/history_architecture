from rest_framework import serializers
from .models import About


class AppInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ('general_information', 'web_site', 'mail',)
