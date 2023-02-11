from django.contrib import admin
from .models import Foo
from .models import TestingRoom

admin.site.register(Foo)
#admin.site.register(TestingRoom)

class TestingRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "room_number" , "bldg" , "capacity")

admin.site.register(TestingRoom, TestingRoomAdmin)
