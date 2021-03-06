from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from .run import *
import random
import threading
from io import StringIO, BytesIO
from django.core.mail import send_mail, EmailMessage
import zipfile
import os
import uuid
from platform import system as system_name # Returns the system/OS name
from os import system as system_call 
from time import sleep
import subprocess

def first(request):
    return render(request,'first.html')

def team(request):
    return render(request,'team.html')

def sites(request):
    return render(request,'sites.html')

def home(request):
    x = str(uuid.uuid4())[:5]
    return HttpResponseRedirect("/geturl/"+x)

def get_url(request, user):
    # print("Sajndkans")
    form = url_form()
    if request.method == 'POST':
        # print("Shreyaksnd")
        form = url_form(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data.get('url')
            email_user = form.cleaned_data.get('email')

            t = threading.Thread(target=tryping)
            t.setDaemon(True)
            t.start()
            # html="<html><head><script>alert('Your file will be downloaded shortly')</script></head><body>Thankyou for using our service</body></html>"
            PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
            main(video_url, user)
            # data = open(os.path.join(PROJECT_PATH,'english_subtitles_'+str(user)+'.srt'),'r').read()
            # resp = HttpResponse(data, content_type='application/x-download')
            # resp['Content-Disposition'] = 'attachment;filename=english_subtitles.srt'
            filenames = [os.path.join(PROJECT_PATH,'english_subtitles_'+str(user)+'.srt'), os.path.join(PROJECT_PATH,'hindi_subtitles_'+str(user)+'.srt')]

            zip_subdir = "subtitles"
            zip_filename = "%s.zip" % zip_subdir

            # Open BytesIO to grab in-memory ZIP contents
            s = BytesIO()

            zf = zipfile.ZipFile(s, "w")

            for fpath in filenames:
                fdir, fname = os.path.split(fpath)
                zip_path = os.path.join(zip_subdir, fname)

                zf.write(fpath, zip_path)

            zf.close()
            resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
            resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
            mail=EmailMessage(
                'Subtitle files',
                'PFA the subtitle files for your video',
                'hindimedium969@gmail.com',
                [email_user,],
            )
            for ff in filenames:
                mail.attach_file(ff)
            mail.send()
            os.remove(os.path.join(PROJECT_PATH,'english_subtitles_'+str(user)+'.srt'))
            os.remove(os.path.join(PROJECT_PATH,'hindi_subtitles_'+str(user)+'.srt'))
            return resp
        else:
            form = url_form()
    return render(request, 'geturl.html', {'form': form})

def download(request, user, video_url):
    PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
    main(video_url, user)
    data = open(os.path.join(PROJECT_PATH,'english_subtitles_'+str(user)+'.srt'),'r').read()
    resp = HttpResponse(data, content_type='application/x-download')
    resp['Content-Disposition'] = 'attachment;filename=english_subtitles.srt'
    print(type(resp))
    return HttpResponse("Hello")
    # return resp

def tryping():
	for i in range(50):
		a = subprocess.Popen(["/bin/ping", "-c1", "-w100", "google.com"], stdout=subprocess.PIPE).stdout.read()
		print(a)
		sleep(2)

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

    # Pinging
    return system_call("ping " + parameters + " " + host) == 0
