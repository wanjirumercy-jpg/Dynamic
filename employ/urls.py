from django.urls import path
from . import views


app_name = 'employ'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('portfolio/',views.portfolio,name = 'portfolio'),
    path('service/',views.service, name = 'service'),
    path('starter/',views.service, name = 'starter'),

]



