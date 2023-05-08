from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from .serializers import CustomUserCreateSerializer, ProfileUserSerializer, UpdateUserProfileSerializer
from .models import CustomUser, UserProfile
from ..core.models import RealEstate


class CreateCustomUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUserCreateSerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def user_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    serializer = ProfileUserSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def user_update_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    serializer = UpdateUserProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors)


@api_view(['POST'])
def rent_payment(request):
    pass

