from django.shortcuts import render
from django.http import HttpResponse
from tools.tools import *
from owner.views import qry_owners
from owner.views import qry_ownerInfo
from building.views import qry_buildings
from building.views import qry_buildingInfo
from owner.views import *
import json


#-------------------------------------------------------------------------------------
# Application welcome page
#-------------------------------------------------------------------------------------

def AppIndex(request):

  return render(request, "appIndex.html")

#-------------------------------------------------------------------------------------
# Application login page
#-------------------------------------------------------------------------------------

def AppLogin(request, langid):

  captions = T_GetCaptions("COMMON", langid) 

  return render(request, "appLogin.html", {"langid": langid, "captions":captions})

#-------------------------------------------------------------------------------------
# Application main page
#-------------------------------------------------------------------------------------

def App(request, langid):

  captions = T_GetCaptions("COMMON", langid) 

  return render(request, "app.html", {"captions":captions})

#-------------------------------------------------------------------------------------
# Owner functions
#-------------------------------------------------------------------------------------

def AppOwnerIndex(request, langid):
  
  captions = T_GetCaptions("COMMON", langid) 
  ownerSet = qry_owners()

  return render(request, "owner_index.html", {"captions":captions, "owners": ownerSet})

def AppOwnerInfo(request, langid, id):
  
  captions = T_GetCaptions("COMMON", langid) 
  ownerInfo = qry_ownerInfo(id)

  return render(request, "owner_info.html", {"captions":captions, "info": ownerInfo})

def AppOwnerCreate(request, langid):
  
  captions = T_GetCaptions("COMMON", langid) 

  return render(request, "owner_create.html", {"captions":captions})

#-------------------------------------------------------------------------------------
# Building functions
#-------------------------------------------------------------------------------------

def AppBuildingIndex(request, langid):

  captions = T_GetCaptions("COMMON", langid) 
  buildingSet = qry_buildings()

  return render(request, "building_index.html", {"captions": captions, "buildings": buildingSet})

def AppBuildingInfo(request, langid, id):
  
  captions = T_GetCaptions("COMMON", langid) 
  buildingInfo = qry_buildingInfo(id)

  # get building owners
  
  return render(request, "building_info.html", {"captions": captions, "info": buildingInfo})

def AppBuildingCreate(request, langid):
  
  captions = T_GetCaptions("COMMON", langid) 
  messages = T_GetCaptions("BUILDINGS_API_POST", langid) 

  return render(request, "building_create.html", {"captions": captions, "messages": messages})

def AppBuildingUpdadte(request):
    return render(request, "building_update.html")

def AppBuildingDelete(request):
    return render(request, "building_delete.html")

def AppUnitCreate(request, langid, building_id):
  
  captions = T_GetCaptions("COMMON", langid) 
  messages = T_GetCaptions("UNITS_API_POST", langid) 
  formMessages = T_GetCaptions("UNITS_FORM", langid) 
  
  buildingInfo = qry_buildingInfo(id=building_id)
  owners = qry_owners()

  building = {}
  building["id"] = building_id
  building["name"] = buildingInfo["name"]

  return render(request, "unit_create.html", {"captions": captions, "messages": messages, "formMessages": formMessages, "building": building, "owners": owners})
