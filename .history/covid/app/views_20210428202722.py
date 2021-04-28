from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserAttributeForm,HospitalForm,HospitalAttributeForm
from .models import User_Attributes,Hospital,Request
from accounts.models import User
from django.views.generic import FormView,TemplateView
from django.views import View
from django.contrib import messages
import datetime
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import hospital_required,patient_required
from ML import covid_priority



def home(request):
    return render(request,'app/home.html')
def Pindex(request):
    return render(request,'app/patient_index.html')
def Hindex(request):
    return render(request,'app/Hospital_index.html')

@method_decorator([login_required, patient_required], name='dispatch')
class IndexPageView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        context['filled_form'] = User_Attributes.objects.filter(user=context['user'].id)
        context['booked_hospital'] = Request.objects.filter(user=context['user'].id)
        context['users'] = User.objects.count()
        context['hospitals'] = Hospital.objects.count()
        context['bed_alloted'] = Request.objects.filter(fulfilled=1).count()
        return context
@method_decorator([login_required, patient_required], name='dispatch')
class Enrollment(View):
    def post(self,request):
        form = UserAttributeForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = self.request.user.id
            newform.date = datetime.datetime.now()
            newform.details_filled = 1
            newform.save()
            return redirect('index')
        return render(request, 'app/enrollment.html', {'form': form})
    def get(self,request):
        form=UserAttributeForm()
        return render(request,'app/enrollment.html',{'form':form})


@method_decorator([login_required, patient_required], name='dispatch')
class HospitalPageView(FormView):
    template_name = 'app/book.html'
    form_class = HospitalForm

    def get_context_data(self, **kwargs):
        context = super(HospitalPageView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['hospitals'] = Hospital.objects.all()
        n=context['hospitals'].count()
        i=0
        while i<n:
            obj = Hospital.objects.all()[i]
            avb = obj.available_Vaccine
            try:
                while avb > 0:
                    pending = Request.objects.filter(hospital=Hospital.objects.all()[i].id).filter(fulfilled=0).order_by('priority')[0]
                    pending.fulfilled = 1
                    pending.confirmtime = datetime.datetime.now()
                    pending.save()
                    avb -= 1
                    obj.available_Vaccine -= 1
                    obj.save()
            except:
                pass
            obj.que= Request.objects.filter(fulfilled=0).filter(hospital=Hospital.objects.all()[i].id).count()
            obj.save()
            i=i+1
        return context
    def form_valid(self, form):
        request = self.request
        user = self.request.user.id
        hospital = form.cleaned_data['hospital']
        fulfilled = 0
        pref_hospital = Hospital.objects.filter(id=hospital)[0]
        confirmtime = "NA"
        if pref_hospital.available_Vaccine > 0:
            pref_hospital.available_Vaccine -= 1
            pref_hospital.save()
            fulfilled = 1
            confirmtime = (pref_hospital.available_Vaccine)*0.5+9
        det = User_Attributes.objects.filter(user=self.request.user.id).latest('id')
        breathing = det.breathing
        pneumonia = det.pneumonia
        age = det.age
        pregnant = det.pregnant
        diabetes = det.diabetic
        copd = det.copd
        asthma = det.asthma
        immsupr = det.immunocompromised
        hypertension = det.blood
        other = det.others
        cardio = det.heart
        obesity = det.obesity
        renal = det.ckd
        smoker = det.smoker
        priority = covid_priority.priority(breathing, pneumonia, age, pregnant, diabetes, copd, asthma, immsupr,
                                           hypertension,
                                           other, cardio, obesity, renal, smoker)
        Request.objects.create_data(user, hospital, priority, fulfilled, confirmtime)
        messages.success(
            request, ('Your request for bed has been confirmed.'))

        return redirect('index')

@method_decorator([login_required, patient_required], name='dispatch')
class Final(TemplateView):
    template_name = 'app/final.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        try:
            context['filled_form'] = User_Attributes.objects.filter(user=context['user'].id)
            context['booked_hospital'] = Request.objects.filter(user=context['user'].id)
            av = Hospital.objects.filter(id=context['booked_hospital'][0].hospital)[0]
            avb = Hospital.objects.filter(id=context['booked_hospital'][0].hospital)[0].available_Vaccine
            while avb > 0:
                pending =Request.objects.filter(hospital=context['booked_hospital'][0].hospital).filter(fulfilled=0).order_by('priority')[0]
                pending.fulfilled = 1
                pending.confirmtime = datetime.datetime.now()
                pending.save()
                avb -= 1
                av.available_Vaccine -= 1
                av.save()
            av.que=Request.objects.filter(fulfilled=0).filter(hospital=context['booked_hospital'][0].hospital).count()
            av.save()
            context['queue'] = Request.objects.filter(fulfilled=0).filter(hospital=context['booked_hospital'][0].hospital).count()
            #context['index'] = Request.objects.filter(fulfilled=0).filter(hospital=context['booked_hospital'][0].hospital).filter(priority=context['booked_hospital'][0].priority).order_by('priority').count()
            context['index'] = Request.objects.filter(fulfilled=0).filter(hospital=context['booked_hospital'][0].hospital).filter(priority__lte=context['booked_hospital'][0].priority).count()
        except:
            pass
        context['hospitals'] = Hospital.objects.all()
        return context

@method_decorator([login_required, patient_required], name='dispatch')
def phase2(request):
    return render(request,'app/phase2.html')

@method_decorator([login_required, hospital_required], name='dispatch')
class HospitalIndexPageView(TemplateView):
    template_name = 'app/index2.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        context['filled_form'] = Hospital.objects.filter(admin=context['user'].id)[0]
        return context

@method_decorator([login_required, hospital_required], name='dispatch')
class Henrollment(View):
    def post(self,request):
        form = HospitalAttributeForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.admin = self.request.user.id
            newform.save()
            return redirect('index2')
        return render(request, 'app/hospenrollment.html', {'form': form})
    def get(self,request):
        form=HospitalAttributeForm()
        return render(request,'app/hospenrollment.html',{'form':form})

@method_decorator([login_required, hospital_required], name='dispatch')
class Hstatus(TemplateView):
    template_name = 'app/hstatus.html'

    def get_context_data(self, **kwargs):
        u = self.request.user.id
        t=Hospital.objects.filter(admin=u)[0]
        print(t.id)
        context = {}
        context['requests'] = Request.objects.filter(hospital=t.id)
        context['UserDetails']=User_Attributes.objects.all()
        context['name']=User.objects.all()
        return context
