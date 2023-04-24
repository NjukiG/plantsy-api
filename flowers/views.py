from django.shortcuts import render

# from rest_framework import generics
from rest_framework import generics, permissions  # new

from .models import Flowers
from .serializers import FlowersSerializer

class FlowersList(generics.ListCreateAPIView):
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer

class FlowersDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,) # new
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer

# Create your views here.
