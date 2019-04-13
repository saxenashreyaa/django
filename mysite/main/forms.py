from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    number = forms.DecimalField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "number", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.number = self.cleaned_data["number"]

        if commit:
            user.save()
        return user

