from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from . import models
from . import serializers

import datetime








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

class LinkDetailApi(generics.RetrieveAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer


# QuerySets and Managers Task
class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """

    def get(self, request):
        """
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """

    def get(self, request):
        """
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)