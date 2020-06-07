from django.shortcuts import render
from .models import Trains, Stations, Schedules, Bookings
from django import forms

def home(request):
	params = {
		'title': '',
		'trains': Trains.objects.all(),
		'stations': Stations.objects.all(),
	}
	return render(request, 'core/home.html', params)

def form(request):
	if request.method == "POST":
		form = BookingForm(request.POST)
		form.save()
		return render(request, 'core/form.html', { 'title': 'Form', 'submitted': True })
	else:
		form = BookingForm()
		return render(request, 'core/form.html', { 'title': 'Form', 'form': form })

def list(request):
	params = {
		'title': 'List',
		'bookings': Bookings.objects.all(),
	}
	return render(request, 'core/list.html', params)

def details(request):
	params = {
		'title': 'Details',
		'trains': Trains.objects.all(),
		'stations': Stations.objects.all(),
		'schedules': Schedules.objects.all(),
	}
	return render(request, 'core/details.html', params)


class BookingForm(forms.ModelForm):

	class Meta:
		model = Bookings
		fields = ( 'schedule_no', 'passenger_name', 'passenger_age', 'passenger_contact', 'passenger_email', 'seat_count',)
