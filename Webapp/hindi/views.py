from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from .run import *
import random


def home(request):
    x = random.randint(1, 10000)
    return HttpResponseRedirect("/geturl/"+str(x))

def get_url(request, user):
    # print("Sajndkans")
    form = url_form()
    if request.method == 'POST':
        # print("Shreyaksnd")
        form = url_form(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data.get('url')
            email_user = form.cleaned_data.get('email')
            # print("Sjrei")
            main(video_url, user)
        else:
            form = url_form()
    return render(request, 'geturl.html', {'form': form})
