from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','title','description','writer','created_at','updated_at']
        model = Post