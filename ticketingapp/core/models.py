from django.db import models

class Trains(models.Model):
	train_no = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)

class Stations(models.Model):
	station_no = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)

class Schedules(models.Model):
	schedule_no = models.AutoField(primary_key=True)
	train_no = models.ForeignKey(Trains, on_delete=models.CASCADE)
	fare = models.IntegerField()
	departure_time = models.TimeField(null=True, blank=True, default=None)
	arrival_time = models.TimeField(null=True, blank=True, default=None)
	departure_station = models.ForeignKey(Stations, related_name='departure_station', on_delete=models.CASCADE)
	arrival_station = models.ForeignKey(Stations, related_name='arrival_station', on_delete=models.CASCADE)

class Bookings(models.Model):
	booking_no = models.AutoField(primary_key=True)
	schedule_no = models.ForeignKey(Schedules, on_delete=models.CASCADE)
	passenger_name = models.CharField(max_length=100)
	passenger_age = models.IntegerField()
	passenger_contact = models.IntegerField()
	passenger_email = models.CharField(max_length=100)
	seat_count = models.IntegerField()