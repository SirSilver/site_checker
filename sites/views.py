from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import generics
from .models import Site, Status
from .serializers import SiteSerializer, StatusSerializer


class StatusListView(generics.ListAPIView):
    """View for list of statuses, if `url` parameter provided then return filtered queryset"""
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        url = self.request.query_params.get('url', None)
        if url is not None:
            queryset = queryset.filter(site__name=url)
        return queryset


class SiteViewSet(viewsets.ModelViewSet):
    """ViewSet for Site model"""
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
