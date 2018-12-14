from django.contrib import admin
from .models import UserRegister
from .models import RoomBooking
from .models import display
from .models import Contact
# Register your models here.
class UserRegisteradmin(admin.ModelAdmin):
    list_display = ['fname','email_id','contact_no']
    class meta:
        model=UserRegister
class RoomBookingadmin(admin.ModelAdmin):
    list_display = ['room_type','available_rooms','date']
    class meta:
        model=RoomBooking

admin.site.register(UserRegister,UserRegisteradmin)
admin.site.register(RoomBooking,RoomBookingadmin)
admin.site.register(display)
admin.site.register(Contact)