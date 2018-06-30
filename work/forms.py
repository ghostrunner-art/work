from django import forms # 这里需要看djangoproject.com文档
from django.contrib import auth

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',required=True)
    password = forms.CharField(label='密码',widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username,password = password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['uesr']=user
        return self.cleand_data

