from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ticketing-home'),
    path('form/', views.form, name='ticketing-form'),
    path('list/', views.list, name='ticketing-list'),
    path('details/', views.details, name='ticketing-details'),
]
