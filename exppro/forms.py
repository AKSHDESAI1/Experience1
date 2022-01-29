from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.forms import ValidationError


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        print('email', email)
        user = None
        try:
            user = User.objects.get(email=email)
        except:
            return email

        if user is not None:
            raise ValidationError(
                'Email-Id is already exists. please try with another one')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=50, required=True, label='Email')

    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.get(email=email)
            result = authenticate(username=user.username, password=password)
            if result is not None:
                login(self.request, result)
                return result
            else:
                raise ValidationError("Email or password invalid")
        except:
            raise ValidationError("Email or password invalid")
