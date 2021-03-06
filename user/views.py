from django.shortcuts import render ,redirect
from user.models import *
from doctor.models import *
from createStaff.models import staff
import json
import base64
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
        print(app)
        for a in app:

            temp = a.next_due.split('/')
            d = {"pet":a.pet_name.name , "date":a.next_due , "time":a.time , "description":a.Description}
            if date.year < int(temp[2]):
                apm.append(d)
            elif date.year == int(temp[2]) and date.month < int(temp[1]) :
                apm.append(d)
            elif date.year == int(temp[2]) and date.month == int(temp[1]) and date.day <= int(temp[0]):
                apm.append(d)
                
    for i in range(len(apm)-1,-1,-1):
        for j in range(i):
            year1 = apm[j]["time"].split(':')
            year2 = apm[j+1]["time"].split(':')
            if int(year1[1]) > int(year2[1]):
                apm[j],apm[j+1] = apm[j+1],apm[j]
    for i in range(len(apm)-1,-1,-1):
        for j in range(i):
            year1 = apm[j]["time"].split(':')
            year2 = apm[j+1]["time"].split(':')
            if int(year1[0]) > int(year2[0]):
                apm[j],apm[j+1] = apm[j+1],apm[j]

    for i in range(len(apm)-1,-1,-1):
        for j in range(i):
            year1 = apm[j]["date"].split('/')
            year2 = apm[j+1]["date"].split('/')
            if int(year1[0]) > int(year2[0]):
                apm[j],apm[j+1] = apm[j+1],apm[j]
    for i in range(len(apm)-1,-1,-1):
        for j in range(i):
            year1 = apm[j]["date"].split('/')
            year2 = apm[j+1]["date"].split('/')
            if int(year1[1]) > int(year2[1]):
                apm[j],apm[j+1] = apm[j+1],apm[j]
    for i in range(len(apm)-1,-1,-1):
        for j in range(i):
            year1 = apm[j]["date"].split('/')
            year2 = apm[j+1]["date"].split('/')
            if int(year1[2]) > int(year2[2]):
                apm[j],apm[j+1] = apm[j+1],apm[j]
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
    return JsonResponse(medRec, safe=False)

def delPet(req):
    data = json.loads(req.body.decode('utf-8'))
    obj = user.objects.get(pk=data['pk'])
    pet = mypet.objects.get(user = obj,name = data['petName'])
    pet.delete()
    return JsonResponse({'sts':'complete'})


def fonTest(req,pk):
    insession = req.session.get('username')
    objUser = user.objects.filter(username = insession)
    objStaff = staff.objects.filter(username = insession)
    if(len(objUser) > 0 ):
        pk = pk.encode()
        decoded_data = base64.b64decode(pk)
        pk = decoded_data.decode()
        if int(pk)== objUser[0].pk:
            obj = user.objects.get(pk=pk) 
            context={"name": obj.name,"surname": obj.surname,"email":obj.email,"tel":obj.tel,"pk":pk}
            return render(req,'user.html',context)
        else:
            pk_str = str(objUser[0].pk).encode()
            encoded_data = base64.b64encode(pk_str)
            encoded_data = str(encoded_data)[2:-1]
            str_url = '../user/'+encoded_data
            print(str_url)
            return redirect(str_url)           
    elif (len(objStaff) > 0 ):
        pk_str = str(objStaff[0].pk).encode()
        encoded_data = base64.b64encode(pk_str)
        encoded_data = str(encoded_data)[2:-1]
        if objStaff[0].status == 'Doctor':
            str_url = '../doctor/'+encoded_data
        else :
            str_url = '../staff/'+encoded_data
        return redirect(str_url)
    else:
        req.session['username'] = ''
        return render(req,'index.html')


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
