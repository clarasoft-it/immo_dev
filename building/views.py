#========================================================================================
#
# A building is made up of these parts:
#
#   1) An ID, a name and an address; this is he building's basic information
#   2) one or more units, each unit has a default quote share and one or more owners
# 
# Routes:
#
#   /buildings/
#       GET retrieve all buildings
#       POST insert a new building
#
#       Implementation: API_BuildingEnum
#
#   /buildings/<building ID>/
#       GET retrieve building information (including unit information) 
#       DELETE removes a building and all related entities
#
#       Implementation: API_BuildingInfo
#
#   /buildings/<building ID>/owners
#       GET retrieve building owners 
#
#       Implementation: API_BuildingOwners
#
#   /buildings/<building ID>/address
#       GET retrieve building address (basic inforamtion)
#       PUT update building address (basic information)
#
#       Implementation: API_BuildingAddress
#
#   /buildings/<building ID>/units
#       GET retrive building units
#       POST insert a new unit in a building      
#
#       Implementation: API_UnitEnum
#
#   /buildings/<building ID>/units/quoteShares
#       GET retrive building unit quote shares
#       PUT update building unit quote shares
#
#       Implementation: API_UnitEnum
#
#   /buildings/<building ID>/units/<unit name>
#       GET retrive information on a building unit (including a list of owners)
#       PUT update a building unit (including its owners)
#       DELETE remove a building unit
#
#       Implementation: API_UnitInfo
#
#========================================================================================

import json
import uuid
import django.db

from django.http import HttpResponse
from .models import Building  
from .models import Unit
from owner.views import *
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
#=========================================================================================

def API_BuildingEnum(request):

  if request.method == "GET":
    return API_BuildingEnum_GET(request, id)
  elif request.method == "POST":
    return API_BuildingEnum_POST(request)
  else:
    response = {"envelope":{}}
    response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)

#-----------------------------------------------------------------------------------------

def API_BuildingEnum_GET(request, id):
    
  buildings = Building.objects.all()

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = "0x00000000"
  response["data"] = {}

  #return only if builing is active
  response["data"]["buildings"] = qry_buildings()
  
  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_BuildingEnum_POST(request):  
    
  #------------------------------------------------------------------
  # insert a new building
  # The building must have at least one unit and one owner
  #------------------------------------------------------------------

  Data = json.loads(request.body)
  
  response = {"envelope":{}}
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
# route: /buildings/<building-id>
#=========================================================================================

def API_BuildingInstance(request):

  if request.method == "GET":
    return API_BuildingInstance_GET(request, id)
  elif request.method == "DELETE":
    return API_BuildingInstance_DELETE(request)
  else:
    response = {"envelope":{}}
    response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)
  
#-----------------------------------------------------------------------------------------

def API_BuildingInstance_GET(request, id):

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["hResult"] = '0x00000000'

  # returns information of the building if it is active; only active units and owners are reurned
  response["data"] = qry_buildingInfo(id)

  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_BuildingInstance_DELETE(request):  

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {}

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /builings/<building-id>/owners
#=========================================================================================

def API_BuildingOwners(request):

  if request.method == "GET":
    return API_BuildingOwners_GET(request, id)
  else:
    response = {"envelope":{}}
    response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)

#-----------------------------------------------------------------------------------------

def API_BuildingOwners_GET(request, id):

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {}

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: buildings/<building-id>/address
#=========================================================================================

def API_BuildingAddress(request, id):

  if request.method == "GET":
    return API_BuildingAddress_GET(request, id)
  elif request.method == "PUT":
    return API_BuildingAddress_PUT(request, id)
  else:
    response = {"envelope":{}}
    response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)

#-----------------------------------------------------------------------------------------

def API_BuildingAddress_GET(request, id):

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = '0x00000000'

  # Returns the active address if the building is active
  response["data"] = qry_buildingAddress(id)

  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_BuildingAddress_PUT(request, id):

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {}

  response["envelope"]["hResult"] = qry_BuildingAddress_UPDATE(id, json.loads(request.body))

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /builings/<building-id>/units
#=========================================================================================

def API_UnitEnum(request, id):

  if request.method == "GET":
    return API_UnitEnum_GET(request, id)
  elif request.method == "POST":
    return API_UnitEnum_POST(request, id)
  else:
    response = {"envelope":{}}
    response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)

#-----------------------------------------------------------------------------------------

def API_UnitEnum_GET(request, id):
    
  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = "0x00000000"

  # returns the active units of the buuilding if it is also active
  response["data"] = qry_units(id)
  
  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_UnitEnum_POST(request, id):  
    
  #------------------------------------------------------------------
  # insert a new building unit
  #------------------------------------------------------------------

  Data = json.loads(request.body)
  
  response = {"envelope":{}}
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
# route: /builings/<building-id>/units/quoteSahres
#=========================================================================================

def API_UnitQuoteShares(request):

  if request.method == "GET":
    return API_UnitQuoteShares_GET(request, id)
  elif request.method == "PUT":
    return API_UnitQuoteShares_POST(request)
  else:
    response = {"envelope":{}}
    response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)

#-----------------------------------------------------------------------------------------

def API_UnitQuoteShares_GET(request, id):
    
  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = "0x00000000"
  
  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

def API_UnitQuoteShares_POST(request, id):
    
  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = "0x00000000"
  
  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /builings/<building_id>/units/<unit-name>
#=========================================================================================

def API_UnitInstance(request):

  if request.method == "GET":
    return API_UnitInstance_GET(request, id)
  elif request.method == "PUT":
    return API_UnitInstance_PUT(request)
  elif request.method == "DELETE":
    return API_UnitInstance_DELETE(request)
  else:
    response = {"envelope":{}}
    response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)

#-----------------------------------------------------------------------------------------

def API_UnitInstance_GET(request, building_id, unit_name):

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["hResult"] = '0x00000000'

  # Returns unit information for active units if the building is also active
  response["data"] = qry_unitInfo(building_id, unit_name)

  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_UnitInstance_PUT(request, building_id, unit_name):

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["hResult"] = '0x00000000'

  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_UnitInstance_DELETE(request, building_id, unit_name):

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["hResult"] = '0x00000000'

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

  buildings = Building.objects.filter(status='0').order_by("name")

  info = []
  for x in buildings:
    info.append({'id': x.id, 'status': x.status, 'name': x.name, 'no': x.no, 'street': x.street, 'city': x.city, 'prov': x.department, 'zip': x.zip, 'country':x.country})

  return info

#=========================================================================================
# query: return list (array) of building units
#=========================================================================================

def qry_units(building_id):

  cursor = connection.cursor()
  cursor.execute("select name from building where id = %s and status = '0'", [building_id])
  columns = [col[0] for col in cursor.description]
  buildingInfo = [dict(zip(columns, row)) for row in cursor.fetchall()]

  info = {"buildingID": building_id, "buildingName": buildingInfo[0]["name"], "units": []}

  cursor.execute("select a.building_id, a.name, a.base_share, b.owner_id, c.fname, c.lname, c.address1, c.address2, c.city, c.department, c.zip, c.country, c.phone1, c.phone2, c.fax, c.email from unit a join building_owner b on a.building_id = b.building_id And a.name = b.unit_name And a.status = b.status Join contact c on b.owner_id = c.id And b.status = c.status where a.building_id = %s And a.status = '0'", [building_id])
  columns = [col[0] for col in cursor.description]
  units = [dict(zip(columns, row)) for row in cursor.fetchall()]

  curUnit = ""
  for unit in units:
    if curUnit != unit["name"]:
      curUnit = unit["name"]
      item = info["units"].append({"name": unit["name"], "baseShare": str(unit["base_share"]), "owners":[]})
      info["units"][-1]["owners"].append({"firstName": unit["fname"], "lastName": unit["lname"]})
    else:
      info["units"][-1]["owners"].append({"firstName": unit["fname"], "lastName": unit["lname"]})
  
  return info

#=========================================================================================
# query: return information on a building
#=========================================================================================

def qry_buildingInfo(id):

  cursor = connection.cursor()
  cursor.execute("select id, status, no, street, city, department, zip, country, name from building where id = %s and status = '0'", [id])
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
  
  cursor.execute("select a.building_id, a.name, a.base_share, b.owner_id, c.fname, c.lname, c.address1, c.address2, c.city, c.department, c.zip, c.country, c.phone1, c.phone2, c.fax, c.email from unit a join building_owner b on a.building_id = b.building_id And a.name = b.unit_name And a.status = b.status Join contact c on b.owner_id = c.id And b.status = c.status where a.building_id = %s And a.status = '0'", [id])
  columns = [col[0] for col in cursor.description]
  units = [dict(zip(columns, row)) for row in cursor.fetchall()]

  curUnit = ""
  for unit in units:
    if curUnit != unit["name"]:
      curUnit = unit["name"]
      item = info["units"].append({"name": unit["name"], "baseShare": str(unit["base_share"]), "owners":[]})
      info["units"][-1]["owners"].append({"firstName": unit["fname"], "lastName": unit["lname"]})
    else:
      info["units"][-1]["owners"].append({"firstName": unit["fname"], "lastName": unit["lname"]})
  
  return info

#=========================================================================================
# query: return building name and address
#=========================================================================================

def qry_buildingAddress(id):

  cursor = connection.cursor()
  cursor.execute("select id, status, no, street, city, department, zip, country, name from building where id = %s and status = '0'", [id])
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

  return info

#=========================================================================================
# query: return information on a building unit
#=========================================================================================

def qry_unitInfo(building_id, unit_name):

  unit = Unit.objects.filter(id=building_id, name=unit_name, status='0')

  info = {}
  info["building_id"] = unit.building_id
  info["name"] = unit.name

  return info

#=========================================================================================
# query: update buiding address (basic information)
#=========================================================================================

def qry_BuildingAddress_UPDATE(id, Data):
      
  try:
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE BUILDING SET NAME=%s, NO=%s, STREET=%s, CITY=%s, DEPARTMENT=%s, COUNTRY=%s, ZIP=%s, UPDU='IMMO', UPDD=CURRENT_TIMESTAMP WHERE ID = %s", 
        [Data["name"], Data["no"], Data["street"], Data["city"], Data["prov"], Data["country"], Data["zip"], id])
    hResult = '0x00000000'
  except django.db.IntegrityError as e:
    hResult = '0x80020002'
  except django.db.DatabaseError as e:
    hResult = '0x80020001'

  return hResult