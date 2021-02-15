from django.urls import path
from . import views
from .views import Enrollment,HospitalPageView,Final,Henrollment,Hstatus
urlpatterns = [
    path('',views.home,name='home'),
    path('enroll/',Enrollment.as_view(),name='enroll'),
    path('book/', HospitalPageView.as_view(), name='book'),
    path('final/',Final.as_view(),name='final'),
    path('phase2/',views.phase2,name='phase2'),
    path('henroll/',Henrollment.as_view(),name='henroll'),
    path('hstatus/',Hstatus.as_view(),name='hstatus'),
    path('pindex/',views.Pindex,name='pindex'),
    path('hinde/',views.Hindex,name='hindex'),
]