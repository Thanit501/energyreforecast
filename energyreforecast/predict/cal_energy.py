# from .models import *
# def cal_energy(zone, production, working_day, allocate, saving, month_predict):
#     # y = mx + b
#     m = 0
#     b = 0
#     table = ''
#     ratio = 0
#     if(zone == 'Z'):
#         m = 0.414
#         b = 281.459
#         table = Z_Cal
#         ratio = Z_MAKE
#     elif(zone == 'ZP'):
#         m = 0
#         b = 0
#         table = ZP_Cal
#         ratio = Z_MAKE
    # elif(zone == 'PL'):
    #     m = 0
    #     b = 0
    #     table = ZP_Cal
    #     ratio = Z_MAKE
    # elif(zone == 'AV-NB'):
    #     m = 0
    #     b = 0
    #     table = ZP_Cal
    #     ratio = Z_MAKE
    # elif(zone == 'AV-NR'):
    #     m = 0
    #     b = 0
    #     table = ZP_Cal
    #     ratio = Z_MAKE
    # elif(zone == 'AV-RTD'):
    #     m = 0
    #     b = 0
    #     table = ZP_Cal
    #     ratio = Z_MAKE
    # ratio.objects.filter(month='2021-10').values('tech_ratio')
    # var = production * m
    # fix = working_day * b
    # total_varfix = var + fix
    # energy_var = var * float(ratio)
    # energy_fix = fix * float(ratio)
    # total_energy_predict = (energy_var + energy_fix) * (allocate / 100) * (saving / 100)
    # before_saving = total_energy_predict - (saving / 100)
    # after_saving = total_energy_predict - (allocate / 100)
    
    # table.objects.create(
    #     month_predict=month_predict,
    #     var=var,
    #     fix=fix,
    #     total_varfix=total_varfix,
    #     total_energy_predict=total_energy_predict,
    #     before_saving=before_saving,
    #     after_saving=after_saving
    # )
    # return int(total_energy_predict), int(before_saving), int(after_saving)
