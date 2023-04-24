from django.shortcuts import render

from rest_framework import generics

from .models import Flowers
from .serializers import FlowersSerializer

class FlowersList(generics.ListCreateAPIView):
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer
    
class FlowersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer

# Create your views here.
