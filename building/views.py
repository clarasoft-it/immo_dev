from django.http import HttpResponse
from django.template import loader
from .models import Building  
from .models import BuildingOwner
import json

#=========================================================================================
# route: /builings
#
# example:
#
# http://127.0.0.1:8000/buildings
#
#=========================================================================================

def buildings(request):

  buildings = Building.objects.all()

  response = {}
  response["enveloppe"] = {}
  response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["buildings"] = {}
  for x in buildings:
    response["buildings"][x.name] = {'id': x.id, 'no': x.no, 'street': x.street, 'city': x.city, 'prov': x.department, 'zip': x.zip, 'country':x.country}
  
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


