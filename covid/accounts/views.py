from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterform,HospitalForm
from django.views.generic import CreateView, ListView, UpdateView
from .models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        if user:
            if user.is_active:
                login(request, user)
                if user.is_patient == True:
                    return redirect('index')
                else:
                    return redirect('index2')

        else:
            print("someone tried to login and falied!")
            print("Username : {} and Password : {}".format(username,password))
            return render(request , 'accounts/login.html' , {'error':'Username or password does not exist'})

    else:
        return render(request , 'accounts/login.html' , {})

class PatientSignUpView(CreateView):
    model = User
    form_class = UserRegisterform
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()
        return redirect('index')

class HospitalSignUpView(CreateView):
    model = User
    form_class = HospitalForm
    template_name = 'accounts/register1.html'


    def form_valid(self, form):
        form.save()
        return redirect('index2')