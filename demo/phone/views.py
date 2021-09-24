
from rest_framework import viewsets
from phone import models
from .serializer import PhoneSerializer
# Create your views here.


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = models.Phone_number.objects.all()
    serializer_class = PhoneSerializer

