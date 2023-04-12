from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, error_messages={
        'required': 'Please enter your username',
    })
    password = forms.CharField(label='Password', widget=forms.PasswordInput, error_messages={
        'required': 'Please enter your password',
    })

    def non_field_errors(self):
        return ['Please enter a correct username and password. Note that both fields may be case-sensitive.']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
