# serializers.py (Django)
from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients']  # Ensure fields match your model
