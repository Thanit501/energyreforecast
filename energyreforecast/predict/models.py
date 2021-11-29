from django.db import models
from numpy import fix
from numpy.core.fromnumeric import var
# Create your models here.


# class Z(models.Model):
#     month_range = models.CharField(max_length=150)
#     month_predict = models.CharField(max_length=150)
#     production = models.IntegerField()
#     working_day = models.IntegerField()
#     allocate = models.IntegerField()
#     saving = models.IntegerField()
#     energy_predict = models.FloatField()
#     before_saving = models.FloatField()
#     after_saving = models.FloatField()

#     def __str__(self):
#         return self.month_predict

#     class Meta:
#         db_table = "predict_z"


# class Z_Cal(models.Model):
#     month_predict = models.CharField(max_length=150)
#     var = models.IntegerField()
#     fix = models.IntegerField()
#     total_varfix = models.IntegerField()
#     total_energy_predict = models.IntegerField()
#     before_saving = models.IntegerField()
#     after_saving = models.IntegerField()


# class Z_MAKE(models.Model):
#     month = models.CharField(max_length=150, default=None)
#     production_month = models.IntegerField()
#     energy_month = models.FloatField()
#     working_day = models.IntegerField()
#     tech_ratio = models.FloatField()
#     MWh_day = models.FloatField()

#     def __str__(self):
#         return self.month

    
#     class Meta:
#         db_table = "predict_z_make"


class predict(models.Model):   
    name_machine = models.CharField(max_length=150)
    # name_machine = models.CharField(max_length=20)
    datein = models.DateField()
    dateout = models.DateField()
    month_predict = models.CharField(max_length=150)
    production = models.IntegerField()
    working_day = models.IntegerField()
    allocate = models.IntegerField()
    saving = models.IntegerField()
    energy_predict = models.FloatField()
    before_saving = models.FloatField()
    after_saving = models.FloatField()
    var = models.FloatField()
    fix = models.FloatField()
    energyvar = models.FloatField()
    energyfix = models.FloatField()
    techratio = models.FloatField()
    MWh_day = models.FloatField()


    def __str__(self):
        return self.month_predict

    class Meta:
        db_table = "predict"


class Cal(models.Model):
    name_zone = models.CharField(max_length=10)
    var = models.IntegerField()
    fix = models.IntegerField()
    total_varfix = models.IntegerField()
    def __str__(self):
        return self.month_predict
    class Meta:
        db_table = "predict_Cal"

class predict_graph(models.Model):
    graph_datein = models.DateField()
    graph_dateout = models.DateField()
    graph_production = models.FloatField()
    graph_workingday = models.FloatField()
    graph_allocate = models.FloatField()
    graph_saving = models.FloatField()
    graph_zone = models.CharField(max_length=10)
    graph_monthpredict = models.IntegerField()
    graph_ts = models.DateTimeField()
    def __str__(self):
        return self.monthpredict
    class Meta:
        db_table = "predict_graph"

# class Make(models.Model):
#     name_zone = models.CharField(max_length=10)
#     month = models.CharField(max_length=150, default=None)
#     production_month = models.IntegerField()
#     energy_month = models.FloatField()
#     working_day = models.IntegerField()
#     tech_ratio = models.FloatField()
#     MWh_day = models.FloatField()

#     def __str__(self):
#         return self.name_zone
#     class Meta:
#         db_table = "predict_Make"

class daily(models.Model):
    name_zone = models.CharField(max_length=10)
    name_machine = models.CharField(max_length=20)
    date = models.DateField()
    production = models.FloatField()
    energy = models.FloatField()
    def __str__(self):
        return self.name_zone


class Z_DALIY(models.Model):
    date = models.CharField(max_length=150)
    production_day = models.IntegerField()
    # energy_day = models.IntegerField()
