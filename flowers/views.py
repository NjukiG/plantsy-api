from django.shortcuts import render

from rest_framework import generics
# from rest_framework import generics, permissions  # new

from .models import Flowers
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import FlowersSerializer

class FlowersList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer

class FlowersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    # permission_classes = (permissions.IsAdminUser,) # new
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer

# Create your views here.
