from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext as _


SEX_CHOICES = (
    ("M", ("Male")),
    ("F", ("Female"))
)

ENGLISH_LEVEL_CHOICES = (
    (1, ("A1")),
    (2, ("A2")),
    (3, ("B1")),
    (4, ("B2")),
    (5, ("C1")),
    (5, ("C2"))
)

class MyForm(forms.Form):
    nickname = forms.CharField(label='Nickname', max_length=100)
    sex = forms.ChoiceField(label='Sex', choices=SEX_CHOICES)
    age = forms.IntegerField(label='Age')
    english_level = forms.ChoiceField(label='English_level', choices=ENGLISH_LEVEL_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        sex = self.cleaned_data.get('sex')
        age = self.cleaned_data.get('age')
        english_level = int(self.cleaned_data.get('english_level'))
        if sex == "M" and age >= 20 and english_level >= 4:
            pass
        elif sex == "F" and age >= 22 and english_level >= 3:
            pass
        else:
            raise forms.ValidationError('Not you')

class AuthenticationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput) 

    def clean(self):
            cleaned_data = super().clean()
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            if username and password:
                self.user = authenticate(username=username, password=password)
                if self.user is None:
                    raise forms.ValidationError()

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_repeat= forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_repeat')

    def clean(self):
        cleaned_data = super().clean()    
        if cleaned_data['password'] != cleaned_data['password_repeat']:
            raise forms.ValidationError('Passwords don\'t match')
        return cleaned_data        
    

class Password_change(forms.Form):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    new_password= forms.CharField(label="Enter new password", widget=forms.PasswordInput)
    check_new_password= forms.CharField(label="Confirm new password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean() 
        password = cleaned_data.get('password')
        new_password = cleaned_data.get('new_password')
        check_new_password = cleaned_data.get('check_new_password')

        if password == new_password:
            raise forms.ValidationError('This password already used')
        if new_password != check_new_password:
            raise forms.ValidationError('Passwords don\'t match')

class Get_Comment(forms.Form):
    # text = forms.CharField(label = 'Enter text of your comment', max_length=255)
    # user = forms.BooleanField(label='Comment user', required=False)
    search = forms.CharField(required=False)





