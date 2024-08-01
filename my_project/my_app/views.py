from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .forms import  ContactForm,CustomizeForm,BookingForm,RegisterForm
from .models import *


def register(request):
 
    
    return render(request,"register.html")



def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            confirm_password = form.cleaned_data['confirm_password']

          
            new_user = User.objects.create_user(username, email, password)
           
           
            data = form.save(commit=False)
            data.save()

           
            login_data = LoginData(username=username, password=password, is_staff=False)
            login_data.save()

            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register.html", {'form': form})




def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
           login_data = LoginData.objects.get(username=username)
        except LoginData.DoesNotExist:
           return HttpResponse('Error: User does not exist')
            
        user =authenticate (request,username=username,password=password)
        if user is not None:
                login(request, user)
                if login_data.is_staff:
                    
                    return redirect('admin')
                else:
                    return redirect('user')
        else:
                return HttpResponse('Error: Invalid credentials')
    return render(request, "login.html", {})



def user(request):
    return render(request,"user.html")



@login_required

def logoutuser(request):
    logout(request)
    return redirect('user')


@login_required
def logindetails(request):
    data=Register.objects.all()
    data1=LoginData.objects.all()
    return render(request,"registerview.html",{"result":data,"result1":data1})



@login_required
def adminn(request):
   
    login_data = LoginData.objects.get(username=request.user.username) 
    if not login_data.is_staff:
        return HttpResponse('Error: Access Denied')
    
    return render(request, "admin.html")

@login_required
def contact(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm
    dict_cont ={
        'form':form
    }
    return render(request,"contact.html", dict_cont )



@login_required
def about(request):
    return render(request,"about.html")

def packagesadd(request):
    data2=Package.objects.all()
    return render(request,"packagesadd.html",{"result2":data2})

@login_required   
def packagesdisplay(request):
    data2=Package.objects.all()
    return render(request,'packagesviews.html',{'result1':data2}) 


def packagesviews(request):  
    if request.method == "POST": 
        photo=request.FILES['photo']
        destination_name=request.POST['destination_name']
        days=request.POST['days']
        amount=request.POST['amount']
                                                                       
    
        data3=Package(destination_name=destination_name,days=days,amount=amount,photo=photo) 
        data3.save()
    return render(request,'packagesadd.html')

def updateData(request, id):
    if request.method == "POST":

        edit = Package.objects.get(id=id)

       
        if 'photo' in request.FILES:
            photo = request.FILES['photo']
            edit.photo = photo

      
        edit.destination_name = request.POST.get('destination_name', edit.destination_name)
        edit.days = request.POST.get('days', edit.days)
        edit.amount = request.POST.get('amount', edit.amount)

      
        edit.save()

        return redirect("packagesadd")
    
    d = Package.objects.get(id=id)
    context = {'d': d}
    return render(request, 'edit.html', context)

def deleteData(request,id):
    d=Package.objects.get(id=id)
    d.delete()
    return redirect("packagesadd")


def profile(request):
    user = request.user
    bookings = Bookings.objects.filter(user=user)
    custom=Customized.objects.filter(user=user)
    context = {
        'username': user.username,
        'email': user.email,
        'bookings': bookings,  
        'custom':custom
    }
    return render(request, 'myprofile.html', context)

def booking(request, package_id):
    package = Package.objects.get(id=package_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.destination_name = package
            booking.user = request.user
            booking.save()
    else:
        initial_data = {'username': request.user.username, 'email': request.user.email}
        form = BookingForm(initial=initial_data)

    context = {
        'package': package,
        'form': form,
    }
    return render(request, "bookingpage.html", context)

@login_required
def customized(request):
    if request.method == 'POST':
        form = CustomizeForm(request.POST)
        if form.is_valid():
            customized = form.save(commit=False)
            customized.user = request.user
            customized.email = request.user.email
            customized.save()
    else:
        initial_data = {'user': request.user.username, 'email': request.user.email}
        form = CustomizeForm(initial=initial_data)
    
    context = {
        'form': form,
    }
    return render(request, 'customized.html', context)


def customdetails(request):
    data3=Customized.objects.all()
    return render(request,"customdetails.html",{"result3":data3})

def contactdetails(request):
    data4=Contact.objects.all()
    return render(request,"contactdetails.html",{"result4":data4})


def bookingdetails(request):
    data5=Bookings.objects.all()
    return render(request,"bookingdetails.html",{"result5":data5})

def edit_booking(request,id):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        whatsapp=request.POST['whatsapp']
        booking_date=request.POST['booking_date']
        
        edit=Bookings.objects.get(id=id)
        edit.fname=fname
        edit.lname=lname
        edit.phone=phone
        edit.whatsapp=whatsapp
        edit.booking_date=booking_date
        edit.save()
        return redirect("profile")
    d1=Bookings.objects.get(id=id)
    context={'d1':d1}
        
    return render(request,'editbook.html',context)



def cancelbook(request,id):
    d2=Bookings.objects.get(id=id)
    d2.delete()
    return redirect("profile")

def edit_custom(request,id):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        whatsapp=request.POST['whatsapp']
        adult=request.POST['adult']
        child=request.POST['child']
        infant=request.POST['infant']
        travel_date=request.POST['travel_date']
        travel_dest=request.POST['travel_dest']
        num_days =request.POST['num_days']
        other=request.POST['other']
        edit=Customized.objects.get(id=id)
        edit.fname=fname
        edit.lname=lname
        edit.phone=phone
        edit.whatsapp=whatsapp
        edit.adult=adult
        edit.child=child
        edit.infant=infant
        edit.travel_date=travel_date
        edit.travel_dest=travel_dest
        edit.num_days=num_days
        edit.other=other
        
        edit.save()
        return redirect("profile")
    d2=Customized.objects.get(id=id)
    context={'d2':d2}
        
    return render(request,'editcustom.html',context)

def cancelcustom(request,id):
    d3=Customized.objects.get(id=id)
    d3.delete()
    return redirect("profile")


