from django.http import HttpResponse
from django.template import loader
from .models import Owner  
from .models import Contact
import json
import uuid
from datetime import datetime
import django.db
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
# handles GET and POST
# example: http://127.0.0.1:8000/owners
#=========================================================================================

def api_owners(request):

  if request.method == "POST":
    return api_POST_owner(request)
  elif request.method == "GET":
    return api_GET_ownerEnum()

#=========================================================================================
# route: /owners
# method GET
# example:  http://127.0.0.1:8000/owners
#=========================================================================================

def api_GET_ownerEnum():
    
  #------------------------------------------------------------------
  # retrieve all owners
  #------------------------------------------------------------------

  response = {}
  response["envelope"] = {}
  response["envelope"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["envelope"]["hResult"] = "0x00000000"
  response["data"] = {}
  response["data"]["owners"] = qry_owners()
  
  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# route: /owners/<owner_id>
# method POST
# example: http://127.0.0.1:8000/owners/ae66f43d-50db-4ee7-806f-59e220c23e7b
#=========================================================================================


@transaction.atomic
def api_POST_owner(request):  
    
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
        "INSERT INTO OWNER VALUES(%s, '0', 'IMMO', current_timestamp, 'IMMO', current_timestamp)", 
        [ownerID])
      cursor.execute(
        "INSERT INTO CONTACT VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'IMMO', current_timestamp, 'IMMO', current_timestamp)", 
        [ownerID, '0', Data["firstName"], Data["lastName"], Data["address1"], Data["address2"], Data["city"], 
         Data["prov"], Data["country"], Data["zip"], Data["phone1"], Data["phone2"], Data["fax"], Data["email"]])
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
# Method: POST
# example: http://127.0.0.1:8000/owners/ae66f43d-50db-4ee7-806f-59e220c23e7b
#=========================================================================================

def api_GET_owner(request, id):

  response = {}
  
  response["enveloppe"] = {}
  response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["hResult"] = '0x00000000'
  response["data"] = qry_ownerInfo(id)

  return HttpResponse(json.dumps(response), content_type="application/json")

#=========================================================================================
# query: return list (array) of owners
#=========================================================================================

def qry_owners():

  owners = Owner.objects.all()

  info = []
  for x in owners:
    contact = Contact.objects.get(id=x.id, status='0')
    info.append({'id':x.id, 
                 'firstName': contact.fname, 
                 'lastName': contact.lname,
                 'address_1': contact.address1,
                 'address_2': contact.address2,
                 'city': contact.city,
                 'province': contact.department,
                 'zip': contact.zip,
                 'country': contact.country,
                 'phone_1': contact.phone1,
                 'phone_2': contact.phone2,
                 'fax': contact.fax,
                 'email': contact.email
                 })

  return info

#=========================================================================================
# query: return information on an owner
#=========================================================================================

def qry_ownerInfo(id):

  contact = Contact.objects.get(id=id, status='0')

  info = {}
  info["id"] = contact.id
  info["firstName"] = contact.fname
  info["lastName"] = contact.lname
  info["address_1"] = contact.address1
  info["address_2"] = contact.address2
  info["city"] = contact.city
  info["province"] = contact.department
  info["zip"] = contact.zip
  info["country"] = contact.country
  info["phone_1"] = contact.phone1
  info["phone_2"] = contact.phone2
  info["fax"] = contact.fax
  info["email"] = contact.email

  return info
