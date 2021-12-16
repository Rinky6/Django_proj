from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def display(request):
    # return HttpResponse('hello Rinky')
    return render(request, 'myapp/home.html')


def display1(request):
    r=""" <h1>  Do want you want </h1>"""
    return HttpResponse(r)