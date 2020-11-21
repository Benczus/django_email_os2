from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from email_test.tasks import sleepy, test_mail_send


def index(request):
    return HttpResponse("Django is working!")


def email(request):
    test_mail_send.delay("testing", "This is a message sent by django", "cicakutyazebra@gmail.com", ["xkydltweohlfgdkfek@wqcefp.online"])
    return HttpResponse("Sleeping!")

def html_render(request):
    return render(request, "test_html.html")