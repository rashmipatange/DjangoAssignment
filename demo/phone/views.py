
from rest_framework import viewsets
from phone.models import Phone_number
from .serializer import PhoneSerializer
# Create your views here.



class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone_number.objects.all()
    serializer_class = PhoneSerializer

