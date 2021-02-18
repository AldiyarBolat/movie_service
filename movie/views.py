from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class ListMovie(APIView):
    def get(self, request):
        queryset = models.Movie.objects.all()
        serializer = serializers.MovieSerializer(queryset, many=True)
        return Response(serializer.data)
