from django.db import models
import datetime
# Create your models here.
class UserRegister(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    rpassword = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=100)
class RoomBooking(models.Model):
    room_type=models.CharField(max_length=20)
    available_rooms=models.IntegerField()
    date = models.DateField()
    card_type=models.CharField(max_length=20)
class display(models.Model):
    USERNAME = models.CharField(max_length=20, primary_key=True)
    ROOM_NO = models.IntegerField()
    CUSTOMER_ID = models.IntegerField()
    CHECK_IN_DATE=  models.DateField()
    CHECK_OUT_DATE=models.DateField()
    ROOM_TYPE=models.ForeignKey(RoomBooking,on_delete=models.CASCADE)
    TOTAL_COST=models.DecimalField(max_digits=10,decimal_places=5)
class Contact(models.Model):
    name=models.CharField(max_length=20)
    Email_id=models.EmailField(max_length=20,primary_key=True)
    phone_no=models.IntegerField()
    message=models.CharField(max_length=220)


