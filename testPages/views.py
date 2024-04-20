from django.shortcuts import render
from django.http import HttpResponse

def immoTestPages(request):
    #return HttpResponse("IMMO! test pages")
    return render(request, "immoTestPages.html")

def indexOwners(request):
    return render(request, "index_Owners.html")

def indexBuildings(request):
    return render(request, "index_Buildings.html")

def createOwner(request):
    return render(request, "owner_create.html")

def createBuilding(request):
    return render(request, "building_create.html")
