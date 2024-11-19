from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotels
from .serializers import HotelsSerializer
from rest_framework import generics

class HotelsView(APIView):
    def get(self, request):
        # Retrieve all hotels (Hotels)
        hotels = Hotels.objects.all()
        serializer = HotelsSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new hotel (Hotels)
        serializer = HotelsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new hotel instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer