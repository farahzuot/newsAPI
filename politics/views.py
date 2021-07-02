from django.db import models
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import PoliticSerializer
from .models import Politic
from .permissions import PermissionAdminStaff
# Create your views here.

class newsListCreateView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Politic.objects.all()
    serializer_class = PoliticSerializer
    permission_classes = (PermissionAdminStaff,IsAuthenticated)


class newsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Politic.objects.all()
    serializer_class = PoliticSerializer
    permission_classes = (PermissionAdminStaff,IsAuthenticated)
