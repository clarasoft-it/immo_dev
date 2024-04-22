from django.shortcuts import render
from django.http import HttpResponse
from owner.views import qry_owners
from owner.views import qry_ownerInfo
from building.views import qry_buildings
from building.views import qry_buildingInfo
from app.models import Caption
import json

#-------------------------------------------------------------------------------------
# Application main page
#-------------------------------------------------------------------------------------

def App(request, langid):

  captions = GetCaptions("COMMON", langid) 

  return render(request, "app.html", {"captions":captions})

#-------------------------------------------------------------------------------------
# Owner functions
#-------------------------------------------------------------------------------------

def AppOwnerIndex(request, langid):
  
  captions = GetCaptions("COMMON", langid) 
  ownerSet = qry_owners()

  return render(request, "owner_index.html", {"captions":captions, "owners": ownerSet})

def AppOwnerInfo(request, langid, id):
  
  captions = GetCaptions("COMMON", langid) 
  ownerInfo = qry_ownerInfo(id)

  return render(request, "owner_info.html", {"captions":captions, "info": ownerInfo})

def AppOwnerCreate(request, langid):
  
  captions = GetCaptions("COMMON", langid) 

  return render(request, "owner_create.html", {"captions":captions})

#-------------------------------------------------------------------------------------
# Building functions
#-------------------------------------------------------------------------------------

def AppBuildingIndex(request, langid):

  captions = GetCaptions("COMMON", langid) 
  buildingSet = qry_buildings()

  return render(request, "building_index.html", {"captions": captions, "buildings": buildingSet})

def AppBuildingInfo(request, langid, id):
  
  captions = GetCaptions("COMMON", langid) 
  buildingInfo = qry_buildingInfo(id)

  return render(request, "building_info.html", {"captions": captions, "info": buildingInfo})

def AppBuildingCreate(request, langid):
  
  captions = GetCaptions("COMMON", langid) 

  return render(request, "building_create.html", {"captions": captions})

def AppBuildingUpdadte(request):
    return render(request, "building_update.html")

def AppBuildingDelete(request):
    return render(request, "building_delete.html")

#-----------------------------------------------------------------------
# GetCations - returns the captions for an application ID and language
#-----------------------------------------------------------------------

def GetCaptions(appid, langid):
  
  captionSet = Caption.objects.filter(app=appid, lang=langid)
    
  captions = {}
  captions["langid"] = langid
  captions["COMMON"] = {}
  
  for x in captionSet:
    # we need to repalce hyphens to undderscore to prevent parse errors in template
    captions["COMMON"]["K_" + x.id.replace("-", "_")] = {"caption": x.caption}
 
  return captions