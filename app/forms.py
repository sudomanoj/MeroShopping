from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, password_validation, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from app.models import Customer

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
        
class LoginForm(AuthenticationForm):
    username = UsernameField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'autofocus':True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete':'current-password'}))
    
class CustomerPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'auto-complete':'new-password', 'autofocus':True, 'class':'form-control'}))
    
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'auto-complete':'new-password', 'class':'form-control'}),
    help_text = password_validation.password_validators_help_text_html())
    
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'auto-complete':'new-password', 'class':'form-control'}))
    
class CustomerPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))
    
class CustomerSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'auto-complete':'new-password', 'class':'form-control'}),
    help_text = password_validation.password_validators_help_text_html())
    
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'auto-complete':'new-password', 'class':'form-control'}))
    
    
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'city', 'locality', 'zipcode']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
                   }
        labels = {
            'locality':'Tole',
            'city':'Area',
        }
        
        
# class SearchForm(forms.Form):
#     query = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Search'}))
    