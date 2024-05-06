############################################################################################################
#
# Routes:
#
#   /owners/
#       GET retrieve all buildings
#       POST insert a new building
#
#       Implementation: API_OwnerEnum
#
#   /owners/<owner ID>/
#       GET retrieve owner information  
#       PUT update owner information  
#       DELETE removes an owner
#
#       Implementation: API_OwnerInfo
#
#   /owners/<owner ID>/units
#       GET retrieve owner's building units
#
#       Implementation: API_OwnerUnitEnum
#
############################################################################################################

import json
import uuid
import django.db

from django.http import HttpResponse
from django.template import loader
from .models import Owner  
from .models import Contact
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
# route: /owners
#=========================================================================================

def API_OwnerEnum(request):

  if request.method == "GET":
    return API_OwnerEnum_GET(request)
  elif request.method == "POST":
    return API_OwnerEnum_POST(request)
  else:
    response = {"envelope":{}}
    response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)

#-----------------------------------------------------------------------------------------

def API_OwnerEnum_GET(request):

  response = {}
  response["envelope"] = {}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {"owners": []}
  response["envelope"]["hResult"] = qry_owners(response["data"]["owners"])
  
  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_OwnerEnum_POST(request):
    
  #------------------------------------------------------------------
  # insert a new owner
  #------------------------------------------------------------------
    
  Data = json.loads(request.body)

  #------------------------------------------------------------------    
  # Error checking
  #------------------------------------------------------------------    

  response = {}
  response["envelope"] = {}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {}

  if Data["firstName"] == "":
    hResult = '0x80010001'
  elif Data["lastName"] == "":
    hResult = '0x80010002'
  elif Data["address1"] == "":
    hResult = '0x80010003'
  #elif Data["address2"] == "":
  #  hResult = '0x80010004'
  elif Data["city"] == "":
    hResult = '0x80010005'
  elif Data["prov"] == "":
    hResult = '0x80010006'
  elif Data["zip"] == "":
    hResult = '0x80010007'
  elif Data["country"] == "":
    hResult = '0x80010008'
  elif Data["phone1"] == "":
    hResult = '0x80010009'
  else:

    #------------------------------------------------------------------    
    # Insert owner in database
    #------------------------------------------------------------------    

    ownerID = str(uuid.uuid4())

    try:
      hResult = '0x00000000'
      cursor = connection.cursor()
      cursor.execute(
        "INSERT INTO CONTACT VALUES(%s, %s, %s, %s, %s, 'IMMO', current_timestamp, 'IMMO', current_timestamp)", 
        [ownerID, Data["firstName"], ' ', Data["lastName"], '0'])
      cursor.execute(
        "INSERT INTO ADDRESS VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'IMMO', current_timestamp, 'IMMO', current_timestamp)", 
        [ownerID, '0', Data["address1"], Data["address2"], Data["city"], Data["prov"], Data["country"], Data["zip"], Data["phone1"], Data["phone2"], Data["fax"], Data["email"]])
    except django.db.IntegrityError as e:
      hResult = '0x80020002'
      response["envelope"]["msg"] = "SQLSTATE - " + e.__cause__.pgcode
    except django.db.DatabaseError as e:
      response["envelope"]["msg"] = "SQLSTATE - " + e.__cause__.pgcode
      hResult = '0x80020001'

  response["envelope"]["hResult"] = hResult

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /owners/<owner_id>
#=========================================================================================

def API_OwnerInstance(request, id):

  if request.method == "GET":
    return API_OwnerInstance_GET(request, id)
  elif request.method == "PUT":
    return API_OwnerInstance_PUT(request, id)
  elif request.method == "DELETE":
    return API_OwnerInstance_DELETE(request, id)
  else:
    response = {"envelope":{}}
    response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["envelope"]["hResult"] = '0x8000FFFF'
    return HttpResponse(json.dumps(response), content_type="application/json", status_code=405)

#-----------------------------------------------------------------------------------------

def API_OwnerInstance_GET(request, id):

  response = {}
  
  response["envelope"] = {}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = '0x00000000'
  response["data"] = qry_ownerInfo_SELECT(id)

  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_OwnerInstance_PUT(request, id):

  Data = json.loads(request.body)

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {}

  response["envelope"]["hResult"] = qry_ownerInfo_UPDATE(id, Data)

  return HttpResponse(json.dumps(response), content_type="application/json")

#-----------------------------------------------------------------------------------------

@transaction.atomic
def API_OwnerInstance_DELETE(request, id):

  response = {"envelope":{}}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["data"] = {}

  response["envelope"]["hResult"] = qry_Owner_DELETE(id)

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
#=========================================================================================
#
# QUERIES
#
#=========================================================================================
#=========================================================================================

#=========================================================================================
# query: return list (array) of owners
#=========================================================================================

def qry_owners(info):

  try:
    cursor = connection.cursor()
    cursor.execute("select b.id, b.fname, b.mname, b.lname, c.address1, c.address2, c.city, c.department, c.zip, c.country, c.phone1, c.phone2, c.fax, c.email from contact b join address c on b.id = c.contact_id where b.status = '0' And c.status = '0'", [id])

    for row in cursor.fetchall():

      info.append({'id': row[0], 
                   'firstName': row[1], 
                   'middleName': row[2],
                   'lastName': row[3],
                   'address1': row[4],
                   'address2': row[5],
                   'city': row[6],
                   'province': row[7],
                   'zip': row[8],
                   'country': row[9],
                   'phone1': row[10],
                   'phone2': row[11],
                   'fax': row[12],
                   'email': row[13]})
      
    hResult = '0x00000000'
  except django.db.DatabaseError as e:
    hResult = '0x80020001'

  return hResult

#=========================================================================================
# query: return information on an owner
#=========================================================================================


def qry_ownerInfo_SELECT(id):

  info = {}

  try:
    cursor = connection.cursor()
    cursor.execute("select b.fname, b.mname, b.lname, c.address1, c.address2, c.city, c.department, c.zip, c.country, c.phone1, c.phone2, c.fax, c.email from contact b join address c on b.id = c.contact_id where b.id = %s and b.status = '0' And c.status = '0'", [id])
    row = cursor.fetchone()

    info["id"] = id
    info["firstName"] = row[0]
    info["middleName"] = row[1]
    info["lastName"] = row[2]
    info["address1"] = row[3]
    info["address2"] = row[4]
    info["city"] = row[5]
    info["province"] = row[6]
    info["zip"] = row[7]
    info["country"] = row[8]
    info["phone1"] = row[9]
    info["phone2"] = row[10]
    info["fax"] = row[11]
    info["email"] = row[12]
    info["hresult"] = '0x00000000'
  except django.db.IntegrityError as e:
    info["hresult"] = '0x80020002'
  except django.db.DatabaseError as e:
    info["hresult"] = '0x80020001'

  return info

#=========================================================================================
# query: update information on an owner
#=========================================================================================

def qry_ownerInfo_UPDATE(id, Data):
      
  try:
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE CONTACT SET FNAME = %s, LNAME= %s, UPDU='IMMO', UPDD=CURRENT_TIMESTAMP WHERE ID = %s And STATUS = '0'", 
        [Data["firstName"], Data["lastName"], id])
    cursor.execute(
        "UPDATE ADDRESS SET STATUS = '7', UPDU='IMMO', UPDD=CURRENT_TIMESTAMP WHERE CONTACT_ID = %s And STATUS = '0'", 
        [id])
    cursor.execute(
        "INSERT INTO ADDRESS VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'IMMO', current_timestamp, 'IMMO', current_timestamp)", 
        [id, '0', Data["address1"], Data["address2"], Data["city"], 
         Data["province"], Data["country"], Data["zip"], Data["phone1"], Data["phone2"], Data["fax"], Data["email"]])
    hResult = '0x00000000'
  except django.db.IntegrityError as e:
    hResult = '0x80020002'
  except django.db.DatabaseError as e:
    hResult = '0x80020001'

  return hResult

#=========================================================================================
# query: delete owner
#=========================================================================================

def qry_Owner_DELETE(owner_id):

  # if owner is an administrator, remove the owner    
  try:
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE ADMINISTRATOR SET STATUS='7', UPDU = 'IMMO', UPDD = CURRENT_TIMESTAMP WHERE CONTACT_ID = %s", 
        [owner_id])
  except django.db.DatabaseError as e:
    # not found, ok, we continue
    hResult = '0x00000000'

  try:
    cursor.execute(
        "UPDATE BUILDING_OWNER SET STATUS='7', END_DATE = current_timestamp, UPDU = 'IMMO', UPDD = CURRENT_TIMESTAMP WHERE OWNER_ID = %s", 
        [owner_id])
    hResult = '0x00000000'
  except django.db.DatabaseError as e:
    hResult = '0x80020001'

  return hResult