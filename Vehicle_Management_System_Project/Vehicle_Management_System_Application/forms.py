from django import forms
from django.forms import extras
class Super_Admin_Registration_Form(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Full Name',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'User Name',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )
class Super_Admin_Login_Form(forms.Form):
    username=forms.CharField(
        label='Enter Super Admin Username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Super Admin Username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Enter Super Admin Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Super Admin Password',
                'class':'form-control'
            }
        )
    )
class Admin_Login_Form(forms.Form):
    username=forms.CharField(
        label='Enter Admin Username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Admin Username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Admin Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Admin Password',
                'class':'form-control'
            }
        )
    )
class Admin_Registration_Form(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Full Name',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'User Name',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )
class User_Registration_Form(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Full Name',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'User Name',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )
class User_Login_Form(forms.Form):
    username=forms.CharField(
        label='Enter Admin Username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Admin Username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Admin Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Admin Password',
                'class':'form-control'
            }
        )
    )
