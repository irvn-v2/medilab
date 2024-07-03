from django.contrib import admin
from django.urls import path, include
from medilabapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('start/', views.start, name='start'),

]
