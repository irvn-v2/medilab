from django.contrib import admin
from django.urls import path, include
from medilabapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('departments/', views.departments, name='departments'),
    path('appointments/', views.appointments, name='appointments'),
    path('show/', views.show, name='show'),
    path('delete/')
]
