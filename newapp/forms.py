from django import forms
class RegForm(forms.Form):
    fristname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10,widget=forms.PasswordInput())
    cpassword = forms.CharField(max_length=10,widget=forms.PasswordInput())
    mobileno = forms.IntegerField()
    emailid = forms.EmailField()
class LonginForm(forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=10,widget=forms.PasswordInput())
