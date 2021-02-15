from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Hospital
class UserRegisterform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model =User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        return user
class HospitalForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_hospital = True
        if commit:
            user.save()
        return user