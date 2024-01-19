from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from emp_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('viewall/', views.viewall, name='viewall'),
    path('remove/', views.remove, name='remove'),
    path('add/', views.add, name='add'),
    path('filter_emp/', views.filter_emp, name='filter_emp'),
    path('viewall/viewone/<int:id>/', views.viewone, name='viewone'),
    path('remove/removeindv/<int:id>/', views.removeindv, name='removeindv'),
    
    
    
   
    
]

