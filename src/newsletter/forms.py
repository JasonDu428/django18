from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required = False)
    email = forms.EmailField()
    message = forms.CharField()
    def clean_email(self): #this is very powerful, railse the correct error and exceptions as validation

        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not domain =='gmail':
            raise forms.ValidationError("Please make sure you use your gmail email")
        #if not "edu" in email:
        if not extension =="com":
            raise forms.ValidationError("Please use a valid .com email address")
        return email

    def clean_full_name(self):
        full_name= self.cleaned_data.get('full_name')

        return full_name




#customize form for admin page for sign up page
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields=['full_name','email']
        ### exclude = ['full_name] use sparingly
    def clean_email(self): #this is very powerful, railse the correct error and exceptions as validation

        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not domain =='gmail':
            raise forms.ValidationError("Please make sure you use your gmail email")
        #if not "edu" in email:
        if not extension =="com":
            raise forms.ValidationError("Please use a valid .com email address")
        return email

    def clean_full_name(self):
        full_name= self.cleaned_data.get('full_name')

        return full_name