from django import forms
from .models import User_Attributes,Hospital
class UserAttributeForm(forms.ModelForm):
    class Meta:
        model =User_Attributes
        fields=['age', 'gender', 'pneumonia',
                             'breathing',
            'pregnant',
            'smoker',
             'diabetic',
                'ckd', 'copd', 'immunocompromised',
            'heart',
            'asthma',
            'blood',
            'obesity',
            'others']
class HospitalForm(forms.Form):
    hospital = forms.IntegerField()

class HospitalAttributeForm(forms.ModelForm):
    class Meta:
        model =Hospital
        fields=['name',
    'address',
    'phone',
    'available_Vaccine']

class VaccineForm(forms.Form):
    vaccine = forms.IntegerField()
class DateForm(forms.Form):
    date = forms.CharField(max_length=100)
    time= forms.CharField(max_length=100)