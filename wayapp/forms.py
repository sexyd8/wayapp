from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Shopcart,Profile
from django import forms


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields=('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        widgets = {
             'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
             'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
             'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
             'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
             'password1':forms.PasswordInput(attrs={'class':'form-control'}),
             'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }


class MemberForm(UserCreationForm):
    class Meta:
        model = User
        fields=('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        widgets = {
             'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
             'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
             'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
             'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
             'password1':forms.PasswordInput(attrs={'class':'form-control'}),
             'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }



class ShopCartForm(forms.ModelForm):
    class Meta:
        models=Shopcart
        fields=('quantity',)



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('first_name', 'last_name', 'phone','address', 'fee', 'gender', 'email')
        widgets = {
             'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
             'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
             'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
             'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
             'fee':forms.NumberInput(attrs={'class':'form-control','placeholder':'fee'}),
             'gender':forms.TextInput(attrs={'class':'form-control','placeholder':'Gender'}),
             'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }


