from django.db import models

# Create your models here.
class Tags(models.Model):
    tag = models.CharField(max_length=128, db_index=True)
    datapoints = models.CharField(max_length=256)

class User(models.Model):
    user_id = models.CharField(max_length=256, primary_key=True)
    user_name = models.CharField(max_length=128)
    
class Datapoint(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    unit = models.CharField(max_length=16)
    uncertainty = models.CharField(max_length=16)
    tags = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    geotag = models.CharField(max_length=200)
    owner_id = models.ForeignKey(User)
    created = models.DateTimeField()
    last_modified = models.DateTimeField()

class Measurement(models.Model):
    datapoint = models.ForeignKey(Datapoint)
    quantity = models.IntegerField()
    occuredTime = models.DateTimeField()
    recordedTime = models.DateTimeField()
    