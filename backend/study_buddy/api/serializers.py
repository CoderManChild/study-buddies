from rest_framework import serializers
from .models import studyTime

class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = studyTime
        fields = ('id', 'name', 'minutesStudied')