from rest_framework import serializers
from .models import Customer, Socialmedia


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        # fields = ('first_name', 'last_name', 'email')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socialmedia
        fields = "__all__"

