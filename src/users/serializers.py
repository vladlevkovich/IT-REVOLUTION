from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import CustomUser, UserProfile, DebitCart
from ..core.models import RealEstate
from ..core.serializers import RealEstateSerializer


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileUserSerializer(serializers.ModelSerializer):
    real_estate = RealEstateSerializer(many=True, read_only=True)
    # real_estate = RealEstateSerializer(many=True, read_only=True)
    # real_estate = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'avatar', 'real_estate', 'phone_number')

    # def get_real_estate(self, obj):
    #     real_estate = RealEstate.objects.filter(user=obj.user)
    #     serializer = RealEstateSerializer(real_estate, many=True)
    #
    #     return serializer.data


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance


class AddCardDebitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitCart
        fields = '__all__'

    def create(self, validated_data):
        card = DebitCart.objects.create(
            number_card=validated_data['number_card'],
            month_end=validated_data['month_end'],
            year_end=validated_data['year_end']
        )
        card.save()
        return card
