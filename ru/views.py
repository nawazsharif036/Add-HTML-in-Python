from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("Welcome to RU")


def Course(request):
    return HttpResponse("Welcome to Course")


def courseDetails(request,courseid):
    return HttpResponse(courseid)
