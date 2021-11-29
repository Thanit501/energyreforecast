from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('select_zone/', select_zone),    
    path('report', report),
    path('foobar', input_form),
    path('result_display', result_display),
    path('input_form', input_form),
    path('input_form_zp', input_form_zp),
    path('input_form_pl', input_form_pl),
    
     

    # path('test', test),
    path('input_form_daliy', input_form_daliy),
    path('input_form_daily_zp', input_form_daily_zp),
    path('input_form_daily_pl', input_form_daily_pl)

    # path('select_mach', select_mach)



]
