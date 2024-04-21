from django.shortcuts import render
from django.http import HttpResponse
from owner.views import qry_owners
from owner.views import qry_ownerInfo
from building.views import qry_buildings
from building.views import qry_buildingInfo

#-------------------------------------------------------------------------------------
# Application main page
#-------------------------------------------------------------------------------------

def App(request):
    #return HttpResponse("IMMO! test pages")
    return render(request, "app.html")

#-------------------------------------------------------------------------------------
# Owner functions
#-------------------------------------------------------------------------------------

def AppOwnerIndex(request):

    ownerSet = qry_owners()
    return render(request, "owner_index.html", {"owners": ownerSet})

def AppOwnerInfo(request, id):

    ownerInfo = qry_ownerInfo(id)
    return render(request, "owner_info.html", {"info": ownerInfo})

def AppOwnerCreate(request):
    return render(request, "owner_create.html")

#-------------------------------------------------------------------------------------
# Building functions
#-------------------------------------------------------------------------------------

def AppBuildingIndex(request):

    buildingSet = qry_buildings()
    return render(request, "building_index.html", {"buildings": buildingSet})

def AppBuildingInfo(request, id):

    buildingInfo = qry_buildingInfo(id)
    return render(request, "building_info.html", {"info": buildingInfo})

def AppBuildingCreate(request):
    return render(request, "building_create.html")

def AppBuildingUpdadte(request):
    return render(request, "building_update.html")

def AppBuildingDelete(request):
    return render(request, "building_delete.html")

