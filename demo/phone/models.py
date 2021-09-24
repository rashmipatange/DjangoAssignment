from django.db import models
from django.urls import reverse


# Create your models here.
class Phone_number(models.Model):
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}, {self.phone_num}'
