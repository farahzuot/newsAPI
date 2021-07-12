from django.db import models
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
from .models import Post
from .permissions import PermissionAdminStaff
# Create your views here.

class newsListCreateView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PermissionAdminStaff,IsAuthenticated)


class newsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PermissionAdminStaff,IsAuthenticated)
