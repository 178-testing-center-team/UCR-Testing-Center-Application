from django.db import models

class Foo(models.Model):
  name = models.CharField(max_length=60)

  def __str__(self):
    return self.name
  
# testing room model
class TestingRoom(models.Model):
  room_number = models.IntegerField()
  bldg = models.CharField(max_length=100)
  capacity = models.IntegerField()
