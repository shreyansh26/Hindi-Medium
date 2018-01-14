from django import forms


class url_form(forms.Form):
    url = forms.CharField(label='URL of the video', max_length=100)
    email = forms.EmailField(label='Enter your email')
