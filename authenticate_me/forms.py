from dataclasses import fields
import email
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User



# from django.contrib.auth.models import User
# from dataclasses import fields
# import imp
# from pyexpat import model
# from django import forms
# from .models import Profile

# class UpdateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100,
#                                 required=True, 
#                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class  Meta:
#         model = User
#         fields = ['username','email']

# class UpdateProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
#     bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))

#     class Meta:
#         model=Profile
#         fields=['avatar','bio']

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User    
        fields = ('username','first_name','last_name','email')

class PasswordChangingForm(PasswordChangeForm):
    old_password: forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1: forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2: forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User    
        fields = ('old_password','new_password1','new_password2')
