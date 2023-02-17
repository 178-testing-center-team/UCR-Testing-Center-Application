from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import FooSerializer, TestingRoomSerializer, TestingRoomAvailabilitySerializer
from .models import Foo, TestingRoom, TestingRoomAvailability

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class FooViewSet(viewsets.ModelViewSet):
    queryset = Foo.objects.all().order_by('name')
    serializer_class = FooSerializer
    
class TestingRoomViewSet(viewsets.ModelViewSet):
    queryset = TestingRoom.objects.all()
    serializer_class = TestingRoomSerializer
    
class TestingRoomViewAvailabilitySet(viewsets.ModelViewSet):
    queryset = TestingRoomAvailability.objects.all()
    serializer_class = TestingRoomAvailabilitySerializer