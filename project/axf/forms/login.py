from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=12, min_length=6,required=True,error_messages={"required":'not null','invalid':'format error'},widget=forms.TextInput(attrs={"class":"c"}))
    passwd = forms.CharField(max_length=16, min_length=16,widget=forms.PasswordInput)

