from django import forms
from django.forms import ModelForm
from django import forms
from .models import *
# from .models import ZP
# from .models import PL
# from .models import AV_NB
# from .models import AV_NR
# from .models import AV_TD


# class ZForm(forms.ModelForm):
#     class Meta:
#         model = Z
#         fields = ['month_range', 'month_predict',
#                   'production', 'working_day', 'allocate', 'saving']
#         exclude = "__all__"
#         required = True
class predictForm(forms.ModelForm):
    class Meta:
        model = predict
        fields = '__all__'
        # fields = ['month_range', 'month_predict',
        #           'production', 'working_day', 'allocate', 'saving']
        exclude = "__all__"
        required = True

class  dailyForm(forms.ModelForm):
    class Meta:
        model =  daily
        fields = '__all__'
        # fields = ['month_range', 'month_predict',
        #           'production', 'working_day', 'allocate', 'saving']
        exclude = "__all__"
        required = True

# class ZMAKEForm(forms.ModelForm):
#     class Meta:
#         model = Z_MAKE
#         fields = '__all__'
        # widgets = {
        #     'production_month': forms.TextInput(attrs={'class': 'form-control'}),
        #     'energy_month': forms.TextInput(attrs={'class': 'form-control'}),
        # }

# class ZFormdaliy(forms.modelForm):
#     class Meta:
#         model = Zdaliy
#         exclude = "__all__"
#         required = True

# class ZPForm(forms.ModelForm):
#     class Meta:
#         model = ZP
#         fields = "__all__"


# class PLForm(forms.ModelForm):
#     class Meta:
#         model = PL
#         fields = "__all__"


# class AV_NBForm(forms.ModelForm):
#     class Meta:
#         model = AV_NB
#         fields = "__all__"


# class AV_NR(forms.ModelForm):
#     class Meta:
#         model = AV_NR
#         fields = "__all__"


# class AV_TDForm(forms.ModelForm):
#     class Meta:
#         model = AV_TD
#         fields = "__all__"
