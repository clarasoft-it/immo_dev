from django.http import HttpResponse
from django.template import loader
from .models import Owner  
from .models import Contact
import json
import uuid
from datetime import datetime

#=========================================================================================
# route: /owners
#
# example:
#
# http://127.0.0.1:8000/owners
#
#=========================================================================================

def owners(request):

  # depending on the HTTP method, we select, insert update or delete

  if request.method == "POST":

    #------------------------------------------------------------------
    # insert a new building
    # The building must have at least one unit and one owner
    #------------------------------------------------------------------
    
    Data = json.loads(request.body)

    #------------------------------------------------------------------    
    # Error checking
    #------------------------------------------------------------------    

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
                  department = Data["province"],  
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

    #------------------------------------------------------------------    
    # Create response
    #------------------------------------------------------------------    

    response = {}
    response["enveloppe"] = {}
    response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["enveloppe"]["hResult"] = "0x00000000"
    response["data"] = {}
    response["data"]["ownerId"] = ownerID
    response["data"]["contactId"] = contactID
 
  elif request.method == "GET":

    #------------------------------------------------------------------
    # retrieve all owners
    #------------------------------------------------------------------

    owners = Owner.objects.all()

    response = {}
    response["enveloppe"] = {}
    response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
    response["owners"] = []
    for x in owners:
      response["owners"].append({'id':x.id, 'firstName': x.fname, 'lastName': x.lname})
  
  return HttpResponse(json.dumps(response), content_type="application/json")

 #=========================================================================================
 # route: /owners/<building_id>
 #
 # example:
 #
 # http://127.0.0.1:8000/owners/ae66f43d-50db-4ee7-806f-59e220c23e7b
 #
 #=========================================================================================

def owner_info(request, id):

  owner = Owner.objects.get(id=id)

  response = {}
  response["enveloppe"] = {}
  response["enveloppe"]["token"] = "ae66f43d-50db-4ee7-806f-59e220c23e7b"
  response["id"] = owner.id
  response["contactId"] = owner.contact_id
  response["firstName"] = owner.fname
  response["lastName"] = owner.lname

  return HttpResponse(json.dumps(response), content_type="application/json")


