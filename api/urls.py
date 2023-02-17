from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'foos', views.FooViewSet)
router.register(r'testingRooms',views.TestingRoomViewSet)
router.register(r'testingRoomsAvailability',views.TestingRoomViewAvailabilitySet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
