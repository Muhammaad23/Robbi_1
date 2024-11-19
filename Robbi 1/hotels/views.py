from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import HotelSerializer
from rest_framework import generics
from rest_framework import viewsets
from .serializers import MehmonxonaSerializer
from django_filters import rest_framework as filters


class MehmonxonaFilter(filters.FilterSet):
    address = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Mehmonxona
        fields = ['address']

class MehmonxonaViewSet(viewsets.ModelViewSet):
    queryset = Mehmonxona.objects.all()
    serializer_class = MehmonxonaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MehmonxonaFilter


class HotelView(APIView):
    def get(self, request):
        # Retrieve all hotel (Hotel)
        hotel = Hotel.objects.all()
        serializer = HotelSerializer(hotel, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new hotel (Hotel)
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new hotel instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer