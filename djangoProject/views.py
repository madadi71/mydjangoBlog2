from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    #return HttpResponse("دومین دوره آموزشی جنگو")
    return render (request , 'Home.html')

def about(request):
    #return HttpResponse("اینجا صفحه ی اصلی است")
    return render (request, 'about.html')
