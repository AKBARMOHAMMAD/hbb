from django.shortcuts import render
from django .db import IntegrityError
from .models import UserRegister
from .models import RoomBooking
from .models import display
from .models import Contact
# Create your views here.
def openHomePage(request):
    type="home"
    return render(request,'index.html',{"type":type})


def openServicesPage(request):
    type=request.GET.get("type")
    return render(request,'index.html',{"type":type})


def openUserLogin(request):
    type=request.GET.get("type")
    return render(request,'index.html',{"type":type})


def openSignUpPage(request):
    type=request.GET.get("type")
    return render(request,'index.html',{"type":type})
#=========================================================================

def registerUser(request):
    u_fname = request.POST.get('u_fname')
    u_lname = request.POST.get('u_lname')
    u_email = request.POST.get('u_email')
    u_pass = request.POST.get('u_pass')
    u_rpass = request.POST.get('u_rpass')
    u_cno = request.POST.get('u_cno')
    u_add = request.POST.get('u_add')
    #print(u_fname,u_lname,u_email,u_pass,u_cno,u_add)
    ur=UserRegister(fname=u_fname,lname=u_lname,email_id=u_email,password=u_pass,rpassword=u_rpass,contact_no=u_cno,address=u_add)
    ur.save()
    return render(request,'index.html',{"type":"h_user","message":"User Register Successfully"})
#======================================================================================================

def loginUser(request):
    username=request.POST.get("email")
    password=request.POST.get("pass")
    res=UserRegister.objects.filter(email_id=username,password=password)
    #print(res)
    if not res:
        return render(request,'index.html',{"type":'h_user',"message":"Invalid User"})
    else:
        for x in res:
            print(x)
        return render(request,'index2.html',{"type":type,"name":x})
#============================================================================================================
def openUserHomePage(request):
    type="home"
    res=UserRegister.objects.filter()
    for x in res:
        print(x)
    return render(request,'index2.html',{"type":type,"name":x})
#================================================================
def openBookingPage(request):
    type=request.GET.get("type")
    res = UserRegister.objects.filter()
    qs=RoomBooking.objects.filter()

    for x in res:
        print(x)
    return render(request,'index2.html',{"type":type,"name":x,"qs":qs})
#==================================================================

def openPayment(request):
    type=request.GET.get("type")
    qs=RoomBooking.objects.filter()
    qs1 = RoomBooking.objects.filter()

    return render(request, 'index2.html', {"type": type,"qs":qs,"qs1":qs1})

#===================================================================
def openPreview(request):
    check_in_date = request.POST.get("CHECK_IN_DATE")
    check_out_date = request.POST.get("CHECK_OUT_DATE")
    username = request.POST.get("USERNAME")
    cost = request.POST.get("TOTAL_COST")
    room_no = request.POST.get("ROOM_NO")
    room_type = request.POST.get("ROOM_TYPE")
    f=display(CHECK_IN_DATE=check_in_date,CHECK_OUT_DATE=check_out_date,USERNAME=username,TOTAL_COST=cost,ROOM_NO=room_no,ROOM_TYPE=room_type)
    f.save()
    print(f)

    return render(request, 'index2.html', {"type": type})





def openContactpage(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})

def ContactPage(request):
    u_name=request.POST.get('u_name')
    u_email=request.POST.get('u_email')
    u_phone=request.POST.get('u_phone')
    u_mess=request.POST.get('u_mess')
    #print(u_name,u_email,u_phone,u_phone,u_mess)
    uc=Contact(name=u_name,Email_id=u_email,phone_no=u_phone,message=u_mess)
    uc.save()
    print(uc)
    return render(request,'index.html',{"type":'h_contact',"message":'Successfully message sent'})


def openCancelPage(request):
    type=request.GET.get("type")
    return render(request,'index2.html',{"type":type})

def CancelPage(request):
    u_name=request.POST.get('u_name')
    u_room=request.POST.get('u_room')
    u_id=request.POST.get('u_id')
    ucan=display(USERNAME=u_name,ROOM_NO=u_room,CUSTOMER_ID=u_id)
    ucan.save()
    return render(request,'index2.html',{"type":'u_cancel',"message":"Successfully Room Canceled"})