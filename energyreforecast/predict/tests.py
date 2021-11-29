from django.test import TestCase

# Create your tests here.





# from django.shortcuts import render, redirect           
# from django.db import IntegrityError
# from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.http import HttpResponse
# from django.urls import reverse
# import matplotlib.pyplot as plt
# import logging
# import numpy as np
# from .cal_energy_sum import cal_energy_sum
# from django.db.models import Count
# from .form import *   # form z
# from .models import *          # model.py
# import pandas as pd
# # Create your views here.
# def Home(request):
#     return render(request, 'predict/firstscreen.html')
# def select_zone(request):
#     zone = daily.objects.all().values('name_zone').annotate(total=Count())
#     # zone = Make.objects.filter(name_zone='z').filter(month='2021-10').values('tech_ratio')  /
#     # zone = Make.objects.all().query/
#     # zone.group_by = ['name_zone']/
#     # zone = ['Z', 'ZP', 'PL', 'AV_NB', 'AV_NR', 'AV_RTD']/
#     return render(request, 'predict/select_zone.html', {'zone': zone})

# def report(request):
#     return render(request, 'predict/report.html')
# # model = Z
# # model = Z
# # form = ZForm
# def input_form(request):
#     submitted = False
#     zone = request.GET['zone']
#     if request.method == "POST":
#         form = predictForm(request.POST)
#         if form.is_valid():
#             deform = request.POST.dict()
#             item = cal_sum(
#                 # int(deform.get('production')),/
#                 # int(deform.get('working_day')),/
#                 # int(deform.get('allocate')),/
#                 # int(deform.get('saving'))/
#                 int(deform.get('production')),
#                 int(deform.get('working_day')),
#                 int(deform.get('allocate')),
#                 int(deform.get('saving'))
                   
#             )

            # energy_predict, before_saving, after_saving = cal_energy_sum(/
            #     'Z',/
            #     int(deform.get('production')),//
            #     int(deform.get('working_day')),/
            #     int(deform.get('allocate')),/
            #     int(deform.get('saving')),/
            #         deform.get('month_predict')/
            #     )/
            section = form.save(commit=False)
            section.energy_predict = item.get('energy_predict')
            section.before_saving = item.get('before_saving')
            # + int(deform.get('production'))/
            section.after_saving = item.get('after_saving')
            section.save()
            # form.save_m2m()
            return HttpResponseRedirect('/result_display')
            # return HttpResponseRedirect('/test')/
    else:
        form = predictForm
        # foo = 'bar'/
        return render(request, 'predict/input_form.html', {'zone': zone})

def cal_sum(production, working_day, allocate, saving):
    # m = 0/
    # b = 0/
    # name_zone = ''/
    # ratio = 0/
    # if(name_zone == 'z'):/
    #     m = 0.414/
    #     b = 281.459/
    #     table = predict/
    #     ratio = Make/
    # elif(name_zone == 'zp'):/
    #     m = 10/
    #     b = 20/
    #     table = predict/
    #     ratio = Make/

    # ratio = Make.objects.filter(name_zone='z').filter(month='2021-10').values('tech_ratio') /
    # var = production * m/
    # fix = working_day * b/
    # total_varfix = var + fix/
    # energy_var = var * float(ratio)/
    # energy_fix = fix * float(ratio)/
    # energy_predict = (energy_var + energy_fix) * (allocate / 100) * (saving / 100)/
    # before_saving = energy_predict - (saving / 100)/
    # after_saving = energy_predict - (allocate / 100)/

    # Cal.objects.create(/
    #     name_zone=name_zone,/
    #     var=var,/
    #     fix=fix,/
    #     total_varfix=total_varfix,/
    # )/
    # return int(energy_predict), int(before_saving), int(after_saving)/
    return {'energy_predict': energy_predict, 'before_saving':before_saving ,'after_saving':after_saving  }
# {'energy_predict': 0, 'before_saving':before_saving ,'after_saving':after_saving  }/
def result_display(request):
# def test(request):/
    form = predict.objects.order_by('id').reverse()[0:1]
    # form = Z_MAKE.objects.order_by('id')/
    # form = Z_MAKE.objects.filter(month='2021-10').values('tech_ratio')/
    return render(request, 'predict/result_display.html', {'form': form}) 

def input_form_daliy(request):
    return render(request, 'predict/input_form_daliy.html')
def cal(request):

    return render(request, 'predict/input_form_daliy.html')