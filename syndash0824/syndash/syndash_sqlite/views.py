# Create your views here.
from django.http import HttpResponse
from syndash_sqlite.models import DataPoint, Measurement, Tags, User
import json

def datapoints(request):
    if request.method == 'POST':
        datapoint = json.load(request.raw_post_data)
        print datapoint
        return HTTPResponse("Datapoint is created")
    else:
        return HTTPResponse("Error: not supported method")

def datapoint(request, datapoint_id):
    if request.method == 'GET':
        datapoint = Datapoint.objects.get(pk=datapoint_id)
        return HTTPResponse(json.dump(datapoint))