# app_name/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    add = forms.CharField(max_length=100, required=False)
    dob = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'add', 'dob']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Profile.objects.filter(user=user).update(
                dob=self.cleaned_data.get('dob')
            )
        return user
