from rest_framework import serializers
from .models import *


class RealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = ('id', 'title', 'image')


class RealEstateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        exclude = ('is_archived', 'in_rent', 'is_active_in_lease')


class AddOrUpdateEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'

    def create(self, validated_data):
        instance = RealEstate.objects.create(**validated_data)
        # instance = RealEstate.objects.create(
        #     title=validated_data['title'],
        #     description=validated_data['description'],
        #     number_rooms=validated_data['number_rooms'],
        #     area=validated_data['area'],
        #     price=validated_data['price']
        # )
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.area = validated_data.get('area', instance.area)
        instance.price = validated_data.get('price', instance.price)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

