from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
   email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
   first_name = forms.CharField(label="", max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first Name'}))
   last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

   class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

   def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'User Name'
      self.fields['username'].label = ''
      self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required 150 Character</small></span>'

      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['placeholder'] = 'Password'
      self.fields['password1'].label = ''
      self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Your password cant be so small</small></span>'

      self.fields['password2'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['placeholder'] = 'Confrim Password'
      self.fields['password2'].label = ''
      self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter same password</small></span>'