from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import FooSerializer, TestingRoomSerializer, TestingRoomAvailabilitySerializer, ProfessorReservationSerializer
from .models import Foo, TestingRoom, TestingRoomAvailability, ProfessorReservation
from rest_framework.decorators import action
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class FooViewSet(viewsets.ModelViewSet):
    queryset = Foo.objects.all().order_by('name')
    serializer_class = FooSerializer
    
class TestingRoomViewSet(viewsets.ModelViewSet):
    queryset = TestingRoom.objects.all()
    serializer_class = TestingRoomSerializer
    
    @action(methods=['get'], detail=False)
    def getTestingRoom(self,request):
        # getting our get parameters
        room =  request.GET['roomNum']
        building = request.GET['bldg']
        # filtering for our room
        getRoom = TestingRoom.objects.filter(bldg = building).filter(room_number = room)
        serializer = TestingRoomSerializer(getRoom, many=True)
        return Response(serializer.data)
    
class TestingRoomViewAvailabilitySet(viewsets.ModelViewSet):
    #queryset = TestingRoomAvailability.objects.filter(testing_room_id = 7)
    queryset = TestingRoomAvailability.objects.all()
    serializer_class = TestingRoomAvailabilitySerializer
    
    @action(methods=['get'], detail=False)
    def roomAvailability(self,request):
        # getting our get parameters
        id =  request.GET['id']
        # filtering for our room
        getAvailability = TestingRoomAvailability.objects.filter(testing_room_id = id)
        serializer = TestingRoomAvailabilitySerializer(getAvailability, many=True)
        return Response(serializer.data)

class ProfessorReservationSet(viewsets.ModelViewSet):
    #queryset = TestingRoomAvailability.objects.filter(testing_room_id = 7)
    queryset = ProfessorReservation.objects.all()
    serializer_class = ProfessorReservationSerializer
    