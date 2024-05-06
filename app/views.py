from django.shortcuts import render
from django.http import HttpResponse
from tools.tools import *
from owner.views import qry_owners
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

  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid) 

  return render(request, "appLogin.html", {"langid": langid, "captions":captions})

#-------------------------------------------------------------------------------------
# Application main page
#-------------------------------------------------------------------------------------

def App(request, langid):

  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid) 

  return render(request, "app.html", {"captions":captions})

#-------------------------------------------------------------------------------------
# Owner functions
#-------------------------------------------------------------------------------------

def AppOwnerIndex(request, langid):
  
  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid)
  captions["OWNER_UPDATE"] = T_GetCaptions("OWNER_UPDATE", langid)
  captions["OWNER_DELETE"] = T_GetCaptions("OWNER_DELETE", langid)
  captions["BUILDINGS_API_POST"] = T_GetCaptions("BUILDINGS_API_POST", langid)
  captions["OWNER_API_GET"] = T_GetCaptions("OWNER_API_GET", langid)
  captions["OWNER_API_PUT"] = T_GetCaptions("OWNER_API_PUT", langid)
  captions["OWNER_API_DELETE"] = T_GetCaptions("OWNER_API_DELETE", langid)
  ownerSet = [];
  qry_owners(ownerSet)

  return render(request, "owner_index.html", {"captions":captions, "owners": ownerSet})

def AppOwnerCreate(request, langid):
  
  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid)
  captions["OWNERS_API_POST"] = T_GetCaptions("OWNERS_API_POST", langid)

  return render(request, "owner_create.html", {"captions":captions})

#-------------------------------------------------------------------------------------
# Building index page
#-------------------------------------------------------------------------------------

def HTML_PAGE_AppBuildingIndex(request, langid):

  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid)
  captions["BUILDING_CREATE"] = T_GetCaptions("BUILDING_CREATE", langid)
  captions["BUILDING_UPDATE"] = T_GetCaptions("BUILDING_UPDATE", langid)
  captions["BUILDING_DELETE"] = T_GetCaptions("BUILDING_DELETE", langid)
  captions["BUILDING_API_GET_ADDRESS"] = T_GetCaptions("BUILDING_API_GET_ADDRESS", langid)
  captions["BUILDING_API_PUT_ADDRESS"] = T_GetCaptions("BUILDING_API_PUT_ADDRESS", langid)
  captions["BUILDING_API_DELETE"] = T_GetCaptions("BUILDING_API_DELETE", langid)

  buildingSet = qry_buildings()

  return render(request, "building_index.html", {"captions": captions, "buildings": buildingSet})

#-------------------------------------------------------------------------------------
# Building instance information page
#-------------------------------------------------------------------------------------

def HTML_PAGE_AppBuildingInfo(request, langid, id):
  
  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid) 
  buildingInfo = qry_buildingInfo(id)

  # get building owners
  
  return render(request, "building_info.html", {"captions": captions, "info": buildingInfo})

#-------------------------------------------------------------------------------------
# Building creation page
#-------------------------------------------------------------------------------------

def HTML_PAGE_AppBuildingCreate(request, langid):
  
  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid) 
  captions["BUILDINGS_API_POST"] = T_GetCaptions("BUILDINGS_API_POST", langid) 

  return render(request, "building_create.html", {"captions": captions})

def AppBuildingUpdate(request):
    return render(request, "building_update.html")

def AppBuildingDelete(request):
    return render(request, "building_delete.html")

def AppUnitCreate(request, langid, building_id):
  
  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid) 
  captions["UNITS_API_POST"] = T_GetCaptions("UNITS_API_POST", langid) 
  captions["UNITS_FORM"] = T_GetCaptions("UNITS_FORM", langid) 
  
  buildingInfo = qry_buildingInfo(id=building_id)
  owners = []
  qry_owners(owners)

  building = {}
  building["id"] = building_id
  building["name"] = buildingInfo["name"]

  return render(request, "unit_create.html", {"captions": captions, "building": building, "owners": owners})

#-------------------------------------------------------------------------------------
# HTML COMPONENT : Building index table
#-------------------------------------------------------------------------------------

def HTML_SECTION_AppBuildingIndexTable(request, langid):
  
  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid) 
  buildingIndex = qry_buildings()

  return render(request, "COMPONENT_buildingInfoTable.html", {"captions": captions, "buildings": buildingIndex})

#-------------------------------------------------------------------------------------
# HTML COMPONENT : Owner index table
#-------------------------------------------------------------------------------------

def HTML_SECTION_AppOwnerIndexTable(request, langid):
  
  captions = {"langid": langid}
  captions["COMMON"] = T_GetCaptions("COMMON", langid) 
  owners = []

  qry_owners(owners)

  return render(request, "COMPONENT_ownerInfoTable.html", {"captions": captions, "owners": owners})

