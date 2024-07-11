from django.shortcuts import render, redirect

from medilabapp.models import Appointments


# Create your views here.

def index(request):
    return render(request,'index.html')

def start(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def departments(request):
    return render(request, 'departments.html')

def appointments(request):
    if request.method == 'POST':
        Appointments = appointments(name=request.POST['name'],
                                    email=request.POST['email'],
                                    phone=request.POST['phone'],
                                    date=request.POST['date'],
                                    department=request.POST['department'],
                                    doctor=request.POST['doctor'],
                                    message=request.POST['message'])

        Appointments.save()
        return redirect('appointments/')
    else:
        return render(request, 'appointments.html')

def show(request):
    data = Appointments.objects.all()
    return render(request, 'show.html', {'appointment': data})

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')





