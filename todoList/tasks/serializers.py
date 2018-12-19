from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description')
