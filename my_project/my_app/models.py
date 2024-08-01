from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    confirm_password = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.username
    
    
class LoginData(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
class Contact(models.Model):
  username=models.CharField(max_length=20)
  email=models.EmailField()
  phone=models.CharField( max_length=10)
  message=models.TextField(max_length=200)
  contact_on=models.DateField(auto_now=True) 
  
  def __str__(self):
        return self.username
  
class Package(models.Model) :
  photo=models.ImageField(upload_to="packages")
  destination_name=models.CharField(max_length=40)
  days=models.CharField(max_length=10)
  amount=models.CharField(max_length=10)
  
  
  def __str__(self):
      return self.destination_name
    
class Bookings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=10)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True) 
    destination_name = models.ForeignKey(Package, on_delete=models.CASCADE)
    username = models.CharField(max_length=150) 
    email = models.EmailField()  

    def __str__(self):
        return f"{self.user.username}'s booking on {self.booking_date}"

    
  
class Customized(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='custom')
  email=models.EmailField()
  fname=models.CharField(max_length=20)
  lname=models.CharField(max_length=20)
  phone=models.CharField( max_length=10)
  whatsapp=models.CharField( max_length=10)
  adult=models.IntegerField() 
  child=models.IntegerField()
  infant=models.IntegerField()
  travel_date=models.DateField()
  travel_dest=models.CharField(max_length=100)
  num_days=models.IntegerField()
  other=models.TextField(max_length=200)
  customize_on=models.DateField(auto_now=True)
 
 
            
  def __str__(self):
          return self.user
    
    