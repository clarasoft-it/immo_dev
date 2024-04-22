from django.http import HttpResponse
from django.template import loader
from .models import Owner  
from .models import Contact
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
# route: /owners
# handles GET and POST
# example: http://127.0.0.1:8000/owners
#=========================================================================================

def api_owners(request):

  if request.method == "POST":
    return api_POST_building(request)
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
# route: /builings/<building_id>
# method POST
# example: http://127.0.0.1:8000/buildings/ae66f43d-50db-4ee7-806f-59e220c23e7b
#=========================================================================================

def api_POST_building(request):  
    
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
  elif Data["address2"] == "":
    hResult = '0x80010004'
  elif Data["city"] == "":
    hResult = '0x80010005'
  elif Data["prov"] == "":
    hResult = '0x80010006'
  elif Data["zip"] == "":
    hResult = '0x80010007'
  elif Data["country"] == "":
    hResult = '0x80010008'
  else:

    #------------------------------------------------------------------    
    # Insert owner in database
    #------------------------------------------------------------------    

    ownerID = str(uuid.uuid4())
    contactID = str(uuid.uuid4())

    record = Owner(id = ownerID,
                 contact_id = contactID,
                 fname = Data["firstName"],
                 lname = Data["lastName"],
                 status = '0',
                 crtu = 'Django-Immo',
                 crtd = datetime.now(),
                 updu = 'Django-Immo',
                 updd = datetime.now())

    record.save()

    record = Contact(id = contactID, 
                address1 = Data["address1"],
                address2 = Data["address2"],
                city = Data["city"],
                department = Data["prov"],  
                country = Data["country"],
                zip = Data["zip"],
                phone1 = Data["phone1"],
                phone2 = Data["phone2"],
                fax = Data["fax"],
                email = Data["email"],
                crtu = 'Django-Immo',
                crtd = datetime.now(),
                updu = 'Django-Immo',
                updd = datetime.now())
    
    record.save()
    hResult = '0x00000000'

    #------------------------------------------------------------------    
    # Add response creation info
    #------------------------------------------------------------------    

    response["data"]["ownerId"] = ownerID
    response["data"]["contactId"] = contactID

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
    info.append({'id':x.id, 'firstName': x.fname, 'lastName': x.lname})

  return info

#=========================================================================================
# query: return information on an owner
#=========================================================================================

def qry_ownerInfo(id):

  owner = Owner.objects.get(id=id)

  info = {}
  info["id"] = owner.id
  info["firstName"] = owner.fname
  info["lastName"] = owner.lname

  return info
