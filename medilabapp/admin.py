from django.contrib import admin
from medilabapp.models import Product
from medilabapp.models import Student
from medilabapp.models import Register

# Register your models here.
admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Register)