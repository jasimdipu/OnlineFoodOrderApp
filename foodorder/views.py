from rest_framework.response import Response

from .serializers import CustomerSerializer, SocialSerializer
from .models import Customer, Socialmedia

from rest_framework import generics


# Create your views here.
# GET, POST, PUT, DELETE

class SocialList(generics.ListAPIView):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = SocialSerializer(queryset, many=True)
        return Response(serializer.data)


class SocialLinkCreate(generics.ListCreateAPIView):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialSerializer
