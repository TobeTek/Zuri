from rest_framework import serializers
from . import models

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = "__all__"