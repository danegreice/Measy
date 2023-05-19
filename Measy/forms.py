from django import forms

from .models import Manager

class ManagerForm(forms.ModelForm):

    class Meta:
        model = Manager
        fields = ('cpf', 'name','email', 'phone', 'login', 'password')