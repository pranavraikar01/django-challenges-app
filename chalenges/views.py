from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
d="december"
def index1(request):
    return HttpResponse("This is the ,month of january!")      #html pages can also be returned as resposes 
def index2(request):
    return HttpResponse("This is the month of february!") 
def index3(request):
    return HttpResponse("This is the month of march!") 
def index4(request):
    return HttpResponse("This is the month of april!") 
def index5(request):
    return HttpResponse("This is the month of may!") 
def index6(request):
    return HttpResponse("This is the month of june!") 
def index7(request):
    return HttpResponse("This is the month of july!") 
def index8(request):
    return HttpResponse("This is the month of august!") 
def index9(request):
    return HttpResponse("This is the month of september!") 
def index10(request):
    return HttpResponse("This is the month of october!") 
def index11(request):
    return HttpResponse("This is the month of november!") 
def index12(request):
    return HttpResponse("This is the month of  "+ d +" !")  #just declared a variable and used it 