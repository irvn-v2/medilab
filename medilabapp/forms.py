from django import forms
from medilabapp.models import Appointments

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']