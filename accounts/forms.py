from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })

class SignInForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       for field in self.fields:
        self.fields[field].widget.attrs.update({
            'class':'form-control',
        }) 
        
class UpdatePassForm(PasswordChangeForm):
    def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       for field in self.fields:
        self.fields[field].widget.attrs.update({
            'class':'form-control',
        }) 