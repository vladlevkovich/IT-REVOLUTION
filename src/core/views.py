from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import RealEstate
from .serializers import *


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def home(request):
    queryset = RealEstate.objects.filter(is_active_in_lease=True, in_rent=False)
    serializer = RealEstateSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, pk):
    queryset = RealEstate.objects.get(pk=pk)
    serializer = RealEstateDetailSerializer(queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_real_estate(request):
    # permission_classes = [permissions.IsAuthenticated]
    if request.user.is_authenticated:
        serializer = AddOrUpdateEstateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_real_estates(request, pk):
    try:
        queryset = RealEstate.objects.get(pk=pk)
    except RealEstate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if queryset.user == request.user:
        serializer = AddOrUpdateEstateSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_real_estate(request, pk):
    queryset = RealEstate.objects.get(pk=pk)
    if queryset.user == request.user:
        # serializer = RealEstateSerializer(data=request.data)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
