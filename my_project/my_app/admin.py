from django.contrib import admin
from .models import Register ,LoginData,Contact, Package,Contact,Bookings,Customized

# # Register your models here.

admin.site.register(Register)
admin.site.register(LoginData)
admin.site.register(Package)
admin.site.register(Bookings)
admin.site.register(Customized)
admin.site.register(Contact)