from rest_framework import generics
from . import models
from . import serializers
# Create your views here.

class LinkListApi(generics.ListAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer

class LinkCreateApi(generics.CreateAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer

class LinkDetailApi(generics.RetrieveAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer

class LinkUpdateApi(generics.UpdateAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer

class LinkDeleteApi(generics.DestroyAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer