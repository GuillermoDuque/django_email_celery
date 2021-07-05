from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from example.task import send_email_task


def index(request):
    send_email_task()
    return HttpResponse('<h1>Se envio el email!</h1>')
