from django.http import HttpResponse
from django.template import loader
from .models import Building  
from .models import BuildingOwner
import json
import uuid
from datetime import datetime

#=========================================================================================
#=========================================================================================
#
# API
#
#=========================================================================================
#=========================================================================================

#=========================================================================================
# route: /builings
# handles GET and POST 
# example: http://127.0.0.1:8000/buildings
#=========================================================================================

def api_buildings(request):

  if request.method == "POST":
    return api_POST_building(request)
  elif request.method == "GET":
    return api_GET_buildingEnum(request, id)

#=========================================================================================
# route: /builings
# method GET
# example: http://127.0.0.1:8000/buildings
#=========================================================================================

def api_GET_buildingEnum(request, id):
    
  buildings = Building.objects.all()

  response = {}
  response["envelope"] = {}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = "0x00000000"
  response["data"] = {}
  response["data"]["buildings"] = qry_buildings()
  
  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /builings/<building_id>
# method POST
# example: http://127.0.0.1:8000/buildings/ae66f43d-50db-4ee7-806f-59e220c23e7b
#=========================================================================================

def api_POST_building(request):  
    
  #------------------------------------------------------------------
  # insert a new building
  # The building must have at least one unit and one owner
  #------------------------------------------------------------------

  Data = json.loads(request.body)
  
  response = {}
  response["envelope"] = {}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {}

  if Data["name"] == "":
    hResult = '0x80010001'
  elif Data["no"] == "":
    hResult = '0x80010002'
  elif Data["street"] == "":
    hResult = '0x80010003'
  elif Data["city"] == "":
    hResult = '0x80010004'
  elif Data["prov"] == "":
    hResult = '0x80010005'
  elif Data["zip"] == "":
    hResult = '0x80010006'
  elif Data["country"] == "":
    hResult = '0x80010007'
  else:

    buildingID = str(uuid.uuid4())

    record = Building(id = buildingID, 
                    name = Data["name"],    
                    no = Data["no"],
                    street = Data["street"],
                    city = Data["city"],
                    department = Data["prov"],  
                    zip = Data["zip"],
                    country = Data["country"],
                    crtu = 'Django-Immo',
                    crtd = datetime.now(),
                    updu = 'Django-Immo',
                    updd = datetime.now())

    record.save()

    hResult = '0x00000000'
    response["data"]["buildingId"] = buildingID

  # endif

  response["envelope"]["hResult"] = hResult

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /builings/<building_id>
# method GET
# example: http://127.0.0.1:8000/buildings/ae66f43d-50db-4ee7-806f-59e220c23e7b
#=========================================================================================

def api_GET_building(request, id):

  response = {}
  
  response["enveloppe"] = {}
  response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["hResult"].hResult = '0x00000000'
  response["data"] = qry_buildingInfo(id)

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
#=========================================================================================
#
# QUERIES
#
#=========================================================================================
#=========================================================================================

#=========================================================================================
# query: return list (array) of buildings
#=========================================================================================

def qry_buildings():

  buildings = Building.objects.all()

  info = []
  for x in buildings:
    info.append({'id': x.id, 'name': x.name, 'no': x.no, 'street': x.street, 'city': x.city, 'prov': x.department, 'zip': x.zip, 'country':x.country})

  return info

#=========================================================================================
# query: return information on a building
#=========================================================================================

def qry_buildingInfo(id):

  building = Building.objects.get(id=id)

  units = BuildingOwner.objects.filter(building_id = id).all()

  info = {}
  info["id"] = building.id
  info["name"] = building.name
  info["no"] = building.no
  info["street"] = building.street
  info["city"] = building.city
  info["zip"] = building.zip
  info["prov"] = building.department
  info["country"] = building.country
  info["units"] = []

  cur_unit = ""
  index = -1
  for x in units:
    if cur_unit != x.unit_name:
      cur_unit = x.unit_name 
      index = index + 1
      info["units"].append({"name":x.unit_name, "owners": []})
      info["units"][index]["owners"].append({'id': x.owner_id, 'firstName': x.owner.fname, 'lastName': x.owner.lname})
    else:
      n=0
      info["units"][index]["owners"].append({'id': x.owner_id, 'firstName': x.owner.fname, 'lastName': x.owner.lname})

  return info


