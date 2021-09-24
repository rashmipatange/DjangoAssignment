from django.urls import path
from .views import PhoneViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', PhoneViewSet, basename='todos')
urlpatterns = router.urls