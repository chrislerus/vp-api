from rest_framework import serializers
from random_data.models import Country, City, State


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', )


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name', )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', )