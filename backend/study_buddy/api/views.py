from django.shortcuts import render
from rest_framework import viewsets
from .serializers import apiSerializer
from .models import studyTime

# Create your views here.

class apiView(viewsets.ModelViewSet):
    serializer_class = apiSerializer
    queryset = studyTime.objects.all()