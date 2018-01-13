from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from .run import *
import random
import threading


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
            t = threading.Thread(target=main,args=(video_url, user,))
            t.setDaemon(True)
            t.start()
            html="<html><head><script>alert('Your file will be downloaded shortly')</script></head><body>Thankyou for using our service</body></html>"

            return HttpResponse(html)

        else:
            form = url_form()
    return render(request, 'geturl.html', {'form': form})
