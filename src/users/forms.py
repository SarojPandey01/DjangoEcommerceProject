from django import forms
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class LoginForm(forms.Form):
    username  = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method','contact_no','address', 'quantity']



class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']

    def __init__(self,*args,**kwargs):
        super(ProfileUpdateForm, self).__init__(*args,**kwargs)
        self.fields.pop('password',None)


  