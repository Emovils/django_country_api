from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Citizen
from .serializers import CitizenSerializer

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
