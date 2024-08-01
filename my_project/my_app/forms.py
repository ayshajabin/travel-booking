from django  import forms
from .models import  Contact,Bookings,Customized,Register
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'password', 'confirm_password', 'email']

    def username(self):
        username = self.cleaned_data['username']
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long")
        return username

    def password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        return password

    def confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise ValidationError("Password does not match")
        return confirm_password

    def email(self):
        email = self.cleaned_data['email']
        if not email.endswith('.com'):
            raise ValidationError("Please enter a valid email address")
        return email




class DateInput(forms.DateInput):
    input_type='date'


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        
       
        
        labels={
            'username':'Username',
            'email':'Email',
            'whatsapp':"Whatsapp",
            'phone':'Phone number',
            'message':'Text message'
        }
        

class BookingForm(forms.ModelForm):
   
    class Meta:
        model = Bookings
        fields = ["fname",'lname','phone', 'whatsapp', 'booking_date']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your WhatsApp number'}),
            'booking_date':DateInput(attrs={'class': 'form-control'}),
        }
    
       
class CustomizeForm(forms.ModelForm):
    class Meta:
        model = Customized
        fields = ["fname",'lname', 'phone','whatsapp','adult','child','infant','travel_date','travel_dest','num_days','other']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'adult': forms.NumberInput(attrs={'class': 'form-control'}),
            'child': forms.NumberInput(attrs={'class': 'form-control'}),
            'infant': forms.NumberInput(attrs={'class': 'form-control'}),
            'travel_date': DateInput(attrs={'class': 'form-control'}),
            'travel_dest': forms.TextInput(attrs={'class': 'form-control'}),
            'num_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'other': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'customize_on': forms.DateInput(attrs={'class': 'form-control'}),
        }
