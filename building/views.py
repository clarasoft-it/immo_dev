from django.http import HttpResponse
from django.template import loader
from .models import Building  
from .models import BuildingOwner
import json
import uuid
from datetime import datetime

#=========================================================================================
# route: /builings
#
# example:
#
# http://127.0.0.1:8000/buildings
#
#=========================================================================================

def buildings(request):

  # depending on the HTTP method, we select, insert update or delete

  if request.method == "POST":

    #------------------------------------------------------------------
    # insert a new building
    # The building must have at least one unit and one owner
    #------------------------------------------------------------------

    Data = json.loads(request.body)
  
    buildingID = str(uuid.uuid4())

    record = Building(id = buildingID, 
                  name = Data["name"],    
                  no = Data["no"],
                  street = Data["street"],
                  city = Data["city"],
                  department = Data["province"],  
                  zip = Data["zip"],
                  country = Data["country"],
                  crtu = 'Django-Immo',
                  crtd = datetime.now(),
                  updu = 'Django-Immo',
                  updd = datetime.now())

    record.save()

    response = {}
    response["enveloppe"] = {}
    response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["enveloppe"]["hResult"] = "0x00000000"
    response["data"] = {}
    response["data"]["buildingId"] = buildingID

  elif request.method == "GET":

    #------------------------------------------------------------------
    # retrieve all buildings
    # The building must have at least one unit and one owner
    #------------------------------------------------------------------

    buildings = Building.objects.all()

    response = {}
    response["enveloppe"] = {}
    response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["enveloppe"]["hResult"] = "0x00000000"
    response["buildings"] = []
    for x in buildings:
      response["buildings"].append({'id': x.id, 'name': x.name, 'no': x.no, 'street': x.street, 'city': x.city, 'prov': x.department, 'zip': x.zip, 'country':x.country})
  
  return HttpResponse(json.dumps(response), content_type="application/json")


 #=========================================================================================
 # route: /builings/<building_id>
 #
 # example:
 #
 # http://127.0.0.1:8000/buildings/ae66f43d-50db-4ee7-806f-59e220c23e7b
 #
 #=========================================================================================

def building_info(request, id):

  building = Building.objects.get(id=id)

  units = BuildingOwner.objects.filter(building_id = id).all()

  response = {}
  response["enveloppe"] = {}
  response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["id"] = building.id
  response["name"] = building.name
  response["units"] = {}

  cur_unit = ""
  for x in units:
    if cur_unit != x.unit_name:
      cur_unit = x.unit_name 
      response["units"][x.unit_name] = {}
      response["units"][x.unit_name]["owners"] = []
      response["units"][x.unit_name]["owners"].append({'id': x.owner_id, 'first_name': x.owner.fname, 'last_name': x.owner.lname})
    else:
      response["units"][x.unit_name]["owners"].append({'id': x.owner_id, 'first_name': x.owner.fname, 'last_name': x.owner.lname})

  return HttpResponse(json.dumps(response), content_type="application/json")


