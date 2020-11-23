from rest_framework import serializers
from .models import OwesandOwedBy
from django.contrib.auth.models import User


class OwesandOwedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = OwesandOwedBy
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
