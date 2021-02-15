from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterform,HospitalForm
from django.views.generic import CreateView, ListView, UpdateView
from .models import User

class PatientSignUpView(CreateView):
    model = User
    form_class = UserRegisterform
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()
        return redirect('enroll')

class HospitalSignUpView(CreateView):
    model = User
    form_class = HospitalForm
    template_name = 'accounts/register.html'


    def form_valid(self, form):
        form.save()
        return redirect('henroll')