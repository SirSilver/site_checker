from rest_framework import serializers
from .models import Site, Status


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['url', 'name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['site', 'code', 'time', 'ip']
