from rest_framework import serializers
from .models import ResearchSession

class ResearchSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchSession
        fields = '__all__'
