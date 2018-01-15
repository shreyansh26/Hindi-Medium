from django import forms
from django.forms import Widget

class url_form(forms.Form):
    url = forms.CharField(label='URL of the video', max_length=100)
    url.widget = forms.TextInput(attrs={'placeholder':'url of the video', 'size':'50px'})
    email = forms.EmailField(label='Enter your email',widget=forms.TextInput(attrs={'placeholder':'e-mail address', 'size':'50px'}))
