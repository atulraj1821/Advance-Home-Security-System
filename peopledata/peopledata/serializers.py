from rest_framework import serializers
from .models import Known
from .models import Criminal

class KnownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Known
        fields = ['id', 'image']


class CriminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criminal
        fields = ['id', 'image']


