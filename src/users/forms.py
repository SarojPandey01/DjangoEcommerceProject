from django import forms
from django.contrib.auth.models import User
from . models import *


class LoginForm(forms.Form):
    username  = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method','contact_no','address', 'quantity']


  