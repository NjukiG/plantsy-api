from django.contrib.auth import get_user_model
from rest_framework import viewsets # new
from rest_framework.permissions import IsAdminUser  # new

from .models import Flowers
from .permissions import IsAuthorOrReadOnly
from .serializers import FlowersSerializer, UserSerializer

class FlowersViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer


class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



# The below code was done before optiising to the top one, which is easier.
# They are both practically same and do the same job.



# from django.contrib.auth import get_user_model  # new
# from django.shortcuts import render

# from rest_framework import generics
# # from rest_framework import generics, permissions  # new

# from .models import Flowers
# from .permissions import IsAuthorOrReadOnly  # new
# from .serializers import FlowersSerializer, UserSerializer  # new

# class FlowersList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)  # new
#     queryset = Flowers.objects.all()
#     serializer_class = FlowersSerializer


# class FlowersDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     # permission_classes = (permissions.IsAdminUser,) # new
#     queryset = Flowers.objects.all()
#     serializer_class = FlowersSerializer


# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# # Create your views here.
