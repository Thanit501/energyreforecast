from django.db.models.fields import CharField
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import matplotlib.pyplot as plt
import logging
import numpy as np
from django.db.models import Count
from .form import *   # form z
from .models import *          # model.py
import pandas as pd
from .EPL import EPL
from django.db.models import Sum

# Create your views here.
def Home(request):
    return render(request, 'predict/firstscreen.html')
    
def select_zone(request):
    zone = daily.objects.all().values('name_zone').annotate(total=Count('name_zone'))
    return render(request, 'predict/select_zone.html', {'zone': zone})

# def select_mach(request):
#     zone = daily.objects.all().values('name_zone').annotate(total=Count('name_zone'))
#     return render(request, 'predict/select_mach.html', {'zone': zone}) 
    
def input_form(request):
    submitted = False
    # zone = request.GET['zone']
    if request.method == "POST":
        # deform = predictForm(request.POST)
        deform = request.POST.dict()
        arrTemp = deform.get('month_range').split("-")
        zoneName = deform.get('zone_name')
        dateIn = arrTemp[0].strip()
        dateIn = dateIn[6:] + "-" + dateIn[:2] + "-" + dateIn[3:5]
        dateOut = arrTemp[1].strip()
        dateOut = dateOut[6:] + "-" + dateOut[:2] + "-" + dateOut[3:5]
        energy = EPL.EnergyPredict(
                                    dateIn=dateIn, 
                                    dateOut=dateOut, 
                                    production=int(deform.get('production')),
                                    monthpredict=(deform.get('month_predict')),  
                                    workingday=int(deform.get('workingday')), 
                                    allocate=int(deform.get('allocate')), 
                                    saving=int(deform.get('saving')),
                                    zone=zoneName, debug=False)         
        graphPath = str(energy.RecID) + '_' + zoneName + '.png'
        # if deform.is_valid():     
        # deform = deform.save(commit=False)
        # deform = deform.save()    

        predict.objects.create(
               name_machine = zoneName,  
               production = energy.production,
               datein = energy.dateIn,
               dateout = energy.dateOut,
               month_predict = energy.monthpredict,
               working_day = energy.workingday,
               allocate = energy.allocate,
               saving = energy.saving,
               energy_predict = energy.energypredict[zoneName],
               after_saving = energy.aftersaving[zoneName],
               before_saving = energy.beforesaving[zoneName],
               var = energy.var[zoneName],
               fix = energy.var[zoneName],
               energyvar = energy.var[zoneName],
               energyfix = energy.var[zoneName],
               techratio = energy.var[zoneName],
               MWh_day = energy.var[zoneName]
    )
        return render(request, 'predict/result_display.html', { 'energy': energy, 
                                                                'production':energy.production,
                                                                'afterVal':energy.aftersaving[zoneName], 
                                                                'beforeVal':energy.beforesaving[zoneName], 
                                                                'predictVal':energy.energypredict[zoneName], 
                                                                'zoneName':zoneName, 
                                                                'RecID':energy.RecID, 
                                                                'graphPath':graphPath})
        

    else:
        form = predictForm
        return render(request, 'predict/input_form.html')
    

def input_form_zp(request):
    submitted = False
    # zone = request.GET['zone']
    if request.method == "POST":
        form = predictForm(request.POST)
        deform = request.POST.dict()
        # print("dateIN : ", deform.get('month_range'))
        arrTemp = deform.get('month_range').split("-")
        zoneName = deform.get('zone_name_zp')
        # print('zoneName : ', zoneName)
        # print(arrTemp[0], arrTemp[1])
        dateIn = arrTemp[0].strip()
        dateIn = dateIn[6:] + "-" + dateIn[:2] + "-" + dateIn[3:5]
        dateOut = arrTemp[1].strip()
        dateOut = dateOut[6:] + "-" + dateOut[:2] + "-" + dateOut[3:5]
        # print("dateOut : ", dateOut)
        # print()  
        energy = EPL.EnergyPredict(
                                    dateIn=dateIn, 
                                    dateOut=dateOut, 
                                    production=int(deform.get('production')),
                                    monthpredict=(deform.get('month_predict')),  
                                    workingday=int(deform.get('workingday')), 
                                    allocate=int(deform.get('allocate')), 
                                    saving=int(deform.get('saving')),
                                    zone=zoneName, debug=False)        
        graphPath = str(energy.RecID) + '_' + zoneName + '.png'
        if form.is_valid():     
        # return HttpResponseRedirect('/result_display', {'form': energy}) 
           form = energy.save(commit=False)
           form.save()    
        
        predict.objects.create(
               name_machine = zoneName,  
               production = energy.production,
               datein = energy.dateIn,
               dateout = energy.dateOut,
               month_predict = energy.monthpredict,
               working_day = energy.workingday,
               allocate = energy.allocate,
               saving = energy.saving,
               energy_predict = energy.energypredict[zoneName],
               after_saving = energy.aftersaving[zoneName],
               before_saving = energy.beforesaving[zoneName],
               var = energy.var[zoneName],
               fix = energy.var[zoneName],
               energyvar = energy.var[zoneName],
               energyfix = energy.var[zoneName],
               techratio = energy.var[zoneName],
               MWh_day = energy.var[zoneName]
    )
        # print('RETURN', graphPath, energy.RecID, energy.aftersaving[zoneName], energy.beforesaving[zoneName], energy.energypredict[zoneName], zoneName)
        return render(request, 'predict/result_display.html', {'energy': energy, 
                                                                'production':energy.production,
                                                                'afterVal':energy.aftersaving[zoneName], 
                                                                'beforeVal':energy.beforesaving[zoneName], 
                                                                'predictVal':energy.energypredict[zoneName], 
                                                                'zoneName':zoneName, 
                                                                'RecID':energy.RecID, 
                                                                'graphPath':graphPath})
    else:
        form = predictForm
        return render(request, 'predict/input_form_zp.html')

def input_form_pl(request):
    submitted = False
    # zone = request.GET['zone']
    if request.method == "POST":
        form = predictForm(request.POST)
        # print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': ['hNq35HrSpHthdeFoxYebCyQBaT5BGbnEu0D6wvxDPPZWyvJcCkGwDMjWrCctxUaq'], 'month_range': ['11/08/2021 - 11/08/2021'], 'month_predict': ['2021-12'], 'production': ['8'], 'workingday': ['8'], 'allocate': ['8'], 'saving': ['8']}>
        # dateIn = request.POST["month_range"]
        # energy = EPL.EnergyPredict(dateIn="2021-01-01", dateOut="2021-03-31", production=request.POST["production"][0], workingday=request.POST["workingday"][0], allocate=request.POST["allocate"][0], saving=request.POST["saving"][0], debug=True)
        deform = request.POST.dict()
        # print("dateIN : ", deform.get('month_range'))
        arrTemp = deform.get('month_range').split("-")
        zoneName = deform.get('zone_name_pl')
        # print('zoneName : ', zoneName)
        # print(arrTemp[0], arrTemp[1])
        dateIn = arrTemp[0].strip()
        dateIn = dateIn[6:] + "-" + dateIn[:2] + "-" + dateIn[3:5]
        dateOut = arrTemp[1].strip()
        dateOut = dateOut[6:] + "-" + dateOut[:2] + "-" + dateOut[3:5]
        # print("dateOut : ", dateOut)
        # print()  
        energy = EPL.EnergyPredict(
                                    dateIn=dateIn, 
                                    dateOut=dateOut, 
                                    production=int(deform.get('production')),
                                    monthpredict=(deform.get('month_predict')),  
                                    workingday=int(deform.get('workingday')), 
                                    allocate=int(deform.get('allocate')), 
                                    saving=int(deform.get('saving')),
                                    zone=zoneName, debug=False) 
        # print("VALUE : ", 
        #                   dateIn, dateOut,   
        #                   deform.get('month_predict'),
        #                   deform.get('production'),
        #                   deform.get('workingday'), 
        #                   deform.get('allocate'), 
        #                   deform.get('saving'))
        # print("Energy by zoneName", energy.aftersaving[zoneName])           
        graphPath = str(energy.RecID) + '_' + zoneName + '.png'
        if form.is_valid():     
        # return HttpResponseRedirect('/result_display', {'form': energy}) 
           form = energy.save(commit=False)
           form.save()    
        predict.objects.create(
               name_machine = zoneName,  
               production = energy.production,
               datein = energy.dateIn,
               dateout = energy.dateOut,
               month_predict = energy.monthpredict,
               working_day = energy.workingday,
               allocate = energy.allocate,
               saving = energy.saving,
               energy_predict = energy.energypredict[zoneName],
               after_saving = energy.aftersaving[zoneName],
               before_saving = energy.beforesaving[zoneName],
               var = energy.var[zoneName],
               fix = energy.var[zoneName],
               energyvar = energy.var[zoneName],
               energyfix = energy.var[zoneName],
               techratio = energy.var[zoneName],
               MWh_day = energy.var[zoneName]
    )
        # print('RETURN', graphPath, energy.RecID, energy.aftersaving[zoneName], energy.beforesaving[zoneName], energy.energypredict[zoneName], zoneName)
        return render(request, 'predict/result_display.html', {'energy': energy, 
                                                                'production':energy.production,
                                                                'afterVal':energy.aftersaving[zoneName], 
                                                                'beforeVal':energy.beforesaving[zoneName], 
                                                                'predictVal':energy.energypredict[zoneName], 
                                                                'zoneName':zoneName, 
                                                                'RecID':energy.RecID, 
                                                                'graphPath':graphPath})
    else:
        form = predictForm
        return render(request, 'predict/input_form_pl.html')

def result_display(request):
    graph = predict_graph.objects.order_by('id').reverse()[0:1]
    form = predict.objects.order_by('id').reverse()[0:1]
    return render(request, 'predict/result_display.html', {'form': form}) 

def input_form_daliy(request):
    context = {}

    if request.method == "POST":
        data = request.POST.copy()
        name_zone = data.get('name_zone')
        name_machine = data.get('zone_name')
        date = data.get('month_daily')
        production = data.get('Production')
        energy = data.get('Energy')
        print(name_zone,name_machine,date,production,energy)

        new = daily()
        new.name_zone = name_zone
        new.name_machine = name_machine
        new.date = date
        new.production = production
        new.energy = energy
        new.save()
        context['status'] = 'success'

    return render(request, 'predict/input_form_daliy.html',context)

def input_form_daily_zp(request):
    context = {}

    if request.method == "POST":
        data = request.POST.copy()
        name_zone = data.get('name_zone')
        name_machine = data.get('zone_name_zp')
        date = data.get('month_daily')
        production = data.get('Production')
        energy = data.get('Energy')
        print(name_zone,name_machine,date,production,energy)

        new = daily()
        new.name_zone = name_zone
        new.name_machine = name_machine
        new.date = date
        new.production = production
        new.energy = energy
        new.save()
        context['status'] = 'success'

    return render(request, 'predict/input_form_daily_zp.html',context)

def input_form_daily_pl(request):
    context = {}

    if request.method == "POST":
        data = request.POST.copy()
        name_zone = data.get('name_zone')
        name_machine = data.get('zone_name_pl')
        date = data.get('month_daily')
        production = data.get('Production')
        energy = data.get('Energy')
        print(name_zone,name_machine,date,production,energy)

        new = daily()
        new.name_zone = name_zone
        new.name_machine = name_machine
        new.date = date
        new.production = production
        new.energy = energy
        new.save()
        context['status'] = 'success'

    return render(request, 'predict/input_form_daily_pl.html',context)


def report(request):
    zone = daily.objects.all().values('name_zone').annotate(total=Count('name_zone'))
    Z = daily.objects.filter(name_zone="Z").aggregate(Z = Sum('energy'))
    ZP = daily.objects.filter(name_zone="ZP").aggregate(ZP = Sum('energy'))
    PL = daily.objects.filter(name_zone="PL").aggregate(PL = Sum('energy'))
    date = daily.objects.all().values('date').annotate(total=Count('date'))

    energy = daily.objects.all().filter(name_zone="Z").values('energy')
    energyZp = daily.objects.all().filter(name_zone="ZP").values('energy')
    energyPl = daily.objects.all().filter(name_zone="PL").values('energy')


    print(energy)
    return render(request, 'predict/report.html', { 'zone': zone,
                                                    'Z': Z, 
                                                    'ZP': ZP, 
                                                    'PL':PL,
                                                    'date': date,
                                                    'energy': energy,
                                                    'energyZp': energyZp,
                                                    'energyPl': energyPl })
