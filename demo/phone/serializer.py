from rest_framework import serializers
from phone import models


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'phone_num',
        )
        model = models.Phone_number