from rest_framework import serializers
from django.contrib.auth.models import User

from random_data.serializers import CitySerializer

from users.models import Citizen, Mayor


class DetailCitizenSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Citizen
        fields = ('user', 'city', 'is_anon')

    def get_user(self, obj):
        return UserSerializer(obj.user, context=self.context).data

    def get_city(self, obj):
        return CitySerializer(obj.city, context=self.context).data


class AllCitizenSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Citizen
        fields = ('user', 'is_anon', 'city')

    def get_user(self, obj):
        return UserSerializer(obj.user, context=self.context).data

    def get_city(self, obj):
        return CitySerializer(obj.city, context=self.context).data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class AllMayorSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Mayor
        fields = ('user', 'city')

    def get_user(self, obj):
        return UserSerializer(obj.user, context=self.context).data

    def get_city(self, obj):
        return CitySerializer(obj.city, context=self.context).data


class DetailMayorSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Mayor
        fields = ('user', 'city')

    def get_user(self, obj):
        return UserSerializer(obj.user, context=self.context).data

    def get_city(self, obj):
        return CitySerializer(obj.city, context=self.context).data

