from django.http import HttpResponse
from django.template import loader
from .models import Building  
from .models import Unit
from owner.views import *
from .models import BuildingOwner
import json
import uuid
import django.db
from datetime import datetime
from tools.tools import *
from django.db import transaction
from django.db import connection

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

@transaction.atomic
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

    try:
      hResult = '0x00000000'
      cursor = connection.cursor()
      cursor.execute(
        "INSERT INTO BUILDING VALUES(%s, '0', %s, %s, %s, %s, %s, %s, %s, 'IMMO', current_timestamp, 'IMMO', current_timestamp)", 
        [buildingID, Data["name"], Data["no"], Data["street"], Data["city"], Data["prov"], Data["country"], Data["zip"]])
    except django.db.IntegrityError as e:
      hResult = '0x80020002'
      response["envelope"]["msg"] = "SQLSTATE - " + e.__cause__.pgcode
    except django.db.DatabaseError as e:
      response["envelope"]["msg"] = "SQLSTATE - " + e.__cause__.pgcode
      hResult = '0x80020001'

    response["data"]["buildingId"] = buildingID

  # endif

  response["envelope"]["hResult"] = hResult

  return HttpResponse(json.dumps(response), content_type="application/json")


#=========================================================================================
# route: /builings/<building-id>/units
# handles GET and POST 
# example: http://127.0.0.1:8000/buildings/ae66f43d-50db-4ee7-806f-59e220c23e7b/units/
#=========================================================================================

def api_units(request, id):

  if request.method == "POST":
    return api_POST_unit(request, id)
  elif request.method == "GET":
    return api_GET_unitEnum(request, id)

#=========================================================================================
# route: /builings/<building id>/units
# method GET
# example: http://127.0.0.1:8000/buildings
#=========================================================================================

def api_GET_unitEnum(request, building_id):
    
  buildings = Unit.objects.all(building_id)

  response = {}
  response["envelope"] = {}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = "0x00000000"
  response["data"] = {}
  response["data"]["buildings"] = qry_units()
  
  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /builings/<building id>/units
# method POST
# example: http://127.0.0.1:8000/buildings/ae66f43d-50db-4ee7-806f-59e220c23e7b/units
#=========================================================================================

@transaction.atomic
def api_POST_unit(request, id):  
    
  #------------------------------------------------------------------
  # insert a new building unit
  #------------------------------------------------------------------

  Data = json.loads(request.body)
  
  response = {}
  response["envelope"] = {}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {}

  if Data['name'] == "":
    hResult = '0x80010001'
  elif Data['baseShare'] == "":
    hResult = '0x80010002'
  elif len(Data["owners"]) == 0:  
    hResult = '0x80010003'
  else:
    
    try:
      cursor = connection.cursor()
      cursor.execute(
      "INSERT INTO UNIT VALUES(%s, %s, '0', %s, 'IMMO', current_timestamp, 'IMMO', current_timestamp)", 
      [id, Data["name"], Data["baseShare"]])

      # Insert owners

      for owner in Data["owners"]:
        cursor.execute(
          "INSERT INTO BUILDING_OWNER VALUES(%s, %s, %s, '0', current_date, current_date, '0', 'IMMO', current_timestamp, 'IMMO', current_timestamp)", 
          [id, Data["name"], owner["id"]])
        
      hResult = '0x00000000'
    except django.db.IntegrityError as e:
      hResult = '0x80020002'
      response["envelope"]["msg"] = "SQLSTATE - " + e.__cause__.pgcode
    except django.db.DatabaseError as e:
      hResult = '0x80020001'
      response["envelope"]["msg"] = "SQLSTATE - " + e.__cause__.pgcode
    except:
      hResult = '0x8FFFFFFF'


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
  response["hResult"] = '0x00000000'
  response["data"] = qry_buildingInfo(id)

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /builings/<building_id>/<unit-name>
# method GET
# example: http://127.0.0.1:8000/buildings/ae66f43d-50db-4ee7-806f-59e220c23e7b
#=========================================================================================

def api_GET_unit(request, building_id, unit_name):

  response = {}
  
  response["enveloppe"] = {}
  response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["hResult"] = '0x00000000'
  response["data"] = qry_unitInfo(building_id, unit_name)

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
    info.append({'id': x.id, 'status': x.status, 'name': x.name, 'no': x.no, 'street': x.street, 'city': x.city, 'prov': x.department, 'zip': x.zip, 'country':x.country})

  return info

#=========================================================================================
# query: return list (array) of building units
#=========================================================================================

def qry_units(building_id):

  units = Unit.objects.filter(id=building_id)

  info = []
  for x in units:
    info.append({'id': x.id, 'name': x.name})

  return info

#=========================================================================================
# query: return information on a building
#=========================================================================================

def qry_buildingInfo(id):

  cursor = connection.cursor()
  cursor.execute('select id, status, no, street, city, department, zip, country, name from building where id = %s', [id])
  columns = [col[0] for col in cursor.description]
  buildinInfo = [dict(zip(columns, row)) for row in cursor.fetchall()]

  info = {}
  info["id"] = buildinInfo[0]["id"]
  info["status"] = buildinInfo[0]["status"]
  info["name"] = buildinInfo[0]["name"]
  info["no"] = buildinInfo[0]["no"]
  info["street"] = buildinInfo[0]["street"]
  info["city"] = buildinInfo[0]["city"]
  info["zip"] = buildinInfo[0]["zip"]
  info["prov"] = buildinInfo[0]["department"]
  info["country"] = buildinInfo[0]["country"]
  info["units"] = []

  cursor.execute('select a.building_id, a.name, a.base_share, b.owner_id, c.fname, c.lname, c.address1, c.address2, c.city, c.department, c.zip, c.country, c.phone1, c.phone2, c.fax, c.email from unit a join building_owner b on a.building_id = b.building_id And a.name = b.unit_name Join contact c on b.owner_id = c.id where a.building_id = %s', [id])
  columns = [col[0] for col in cursor.description]
  units = [dict(zip(columns, row)) for row in cursor.fetchall()]

  curUnit = ""
  for unit in units:
    if curUnit != unit["name"]:
      curUnit = unit["name"]
      item = info["units"].append({"name": unit["name"], "baseShare": unit["base_share"], "owners":[]})
      info["units"][-1]["owners"].append({"firstName": unit["fname"], "lastName": unit["lname"]})
    else:
      info["units"][-1]["owners"].append({"firstName": unit["fname"], "lastName": unit["lname"]})
  
  return info

#=========================================================================================
# query: return information on a building unit
#=========================================================================================

def qry_unitInfo(building_id, unit_name):

  unit = Unit.objects.get(id=id)

  info = {}
  info["building_id"] = unit.building_id
  info["name"] = unit.name

  return info

