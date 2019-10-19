from django import forms
from django.contrib.auth.models import User
from food_waste_management_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField( )
    last_name = forms.CharField()

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
