from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class AppInfo(GenericAPIView):
    serializer_class = AppInfoSerializer

    def get(self, request):
        """
        Get application info
        ---
        Request header(body):
            - name: Authorization
            - value: Token xxxxxxxxxxxxxxxxxx

        Response parameters(String):
                - 'success' -- success

            Response status(int):
                - 200 - success, about object
        """
        app_info = About.objects.all().first()
        serializer = self.serializer_class(app_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
