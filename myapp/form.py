from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import fields, widgets




class CustomerRegistration(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Re-Password'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
        'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter E-Mail'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
        }

class CustomerLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter User Password'}))
    class Meta:
        model = User
        fields = ['username','password']


class UserPasswordchange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Re-Password'}))


class Userchangeprofile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        widgets = {

        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),

        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),

        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),

        'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter E-Mail'}),

    }

# Password Reset TextBox With Registred E-Mail
class PassResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Enter Your Registered E-Mail'}))

# New Password Set Registred E-Mail Link
class SetNewPassForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm New Password'}))