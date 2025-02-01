from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    author = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def save(self):
        user = User(username=self.cleaned_data['username'],
                    email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])  # Hash password
        user.save()
        return user