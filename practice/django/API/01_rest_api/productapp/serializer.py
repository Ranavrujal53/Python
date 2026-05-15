from rest_framework import serializers
from productapp.models import *


class Categoryserializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class Addressserializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields ="__all__"

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['address'] = Addressserializer(instance.address).data
        return resp


class Productserializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['category'] = Categoryserializer(instance.category).data
        resp['company'] = Companyserializer(instance.company).data
        return resp