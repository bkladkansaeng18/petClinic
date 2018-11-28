from django.shortcuts import render
from user.models import *
from doctor.models import *
import json
import datetime
from django.http import JsonResponse
import operator
# Create your views here.
def userpage(request):
    return render(request, 'user.html')

def userData(request,pk):
    obj = user.objects.get(pk=pk)
    pet = mypet.objects.filter(user= obj)
    listPet = []
    for p in pet:
        d = {"petName":p.name , "type":p.type , "birthDate":p.birthDate , "age":p.age , "breed":p.breed , "sick":p.sickness}
        listPet.append(d)
    return JsonResponse(listPet, safe=False)

def appData(request,pk):
    date = datetime.datetime.now()
    obj = user.objects.get(pk=pk)
    pet = mypet.objects.filter(user = obj)
    apm = []
    for p in pet:
        app = appointment.objects.filter(pet_name = p)
        for a in app:
            d = {"pet":a.pet_name.name , "date":a.next_due , "time":a.time , "description":a.Description}
            if date.year < int(a.next_due[6:]):
                apm.append(d)
            elif date.year == int(a.next_due[6:]) and date.month < int(a.next_due[3:5]) :
                apm.append(d)
            elif date.year == int(a.next_due[6:]) and date.month == int(a.next_due[3:5]) and date.day <= int(a.next_due[:2]):
                apm.append(d)
    for i in range(len(apm)-1,-1,-1):
        for j in range(i):
            year1 = apm[j]["date"]
            year2 = apm[j+1]["date"]
            if int(year1[:2]) > int(year2[:2]):
                apm[j],apm[j+1] = apm[j+1],apm[j]
    print(apm)
    for i in range(len(apm)-1,-1,-1):
        for j in range(i):
            year1 = apm[j]["date"]
            year2 = apm[j+1]["date"]
            if int(year1[3:5]) > int(year2[3:5]):
                apm[j],apm[j+1] = apm[j+1],apm[j]
    print(apm)
    for i in range(len(apm)-1,-1,-1):
        for j in range(i):
            year1 = apm[j]["date"]
            year2 = apm[j+1]["date"]
            if int(year1[6:]) > int(year2[6:]):
                apm[j],apm[j+1] = apm[j+1],apm[j]
    print(apm)
    return JsonResponse(apm, safe=False)

def medRecData(request):
    pk = json.loads(request.body.decode('utf-8'))
    obj = user.objects.get(pk=pk['pk'])
    pet = mypet.objects.filter(user = obj)
    medRec = []
    for p in pet:
        mpet = []
        meds = medical.objects.filter(pet_name = p)
        for r in meds:
            d = {"date":r.medical_date , "age":r.age , "symptom":r.symptom , "medicine":r.medicine , "notation":r.monation , "vet":r.veterinarian }
            mpet.append(d)
        medRec.append(mpet)
    # print("Medical----->",medRec,"\n")

    return JsonResponse(medRec, safe=False)

def vacRecData(request):
    pk = json.loads(request.body.decode('utf-8'))
    obj = user.objects.get(pk=pk['pk'])
    pet = mypet.objects.filter(user = obj)
    medRec = []
    for p in pet:
        mpet = []
        meds = vaccine.objects.filter(pet_name = p)
        for r in meds:
            d = {"givenDate":r.vaccine_date , "age":r.age , "immunization":r.immunization , "vaccine":r.vaccine , "dose":r.dose , "nextDue":r.next_due , "vet":r.veterinarian }
            mpet.append(d)
        medRec.append(mpet)
    # print("Vaccine----->",medRec,"\n")
    return JsonResponse(medRec, safe=False)

def delPet(req):
    data = json.loads(req.body.decode('utf-8'))
    obj = user.objects.get(pk=data['pk'])
    pet = mypet.objects.get(user = obj,name = data['petName'])
    pet.delete()
    return JsonResponse({'sts':'complete'})


def fonTest(req,pk):
    obj = user.objects.get(pk=pk)
    # app = appointment.objects.get(pet_name = obj.)
    context={"name": obj.name,"surname": obj.surname,"email":obj.email,"tel":obj.tel,"pk":pk}
    # context={"name":'d',"surname":'p'}
    return render(req,'user.html',context)

def editProfile(request,pk):
    obj = json.loads(request.body.decode('utf-8'))
    profile = user.objects.get(pk = pk)
    profile.name = obj['name']
    profile.surname = obj['surname']
    profile.tel =  obj['tel']
    profile.email = obj['email']
    profile.save()
    a={'oak':2}
    return JsonResponse(a)