from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteViewSet, StatusListView


router = DefaultRouter()
router.register(r'', SiteViewSet)


urlpatterns = [
    path('site_check/', StatusListView.as_view()),
    path('sites/', include(router.urls))
]
