from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
# d="december"
# def index1(request):
#     return HttpResponse("This is the ,month of january!")      #html pages can also be returned as resposes 
# def index2(request):
#     return HttpResponse("This is the month of february!") 
# def index3(request):
#     return HttpResponse("This is the month of march!") 
# def index4(request):
#     return HttpResponse("This is the month of april!") 
# def index5(request):
#     return HttpResponse("This is the month of may!") 
# def index6(request):
#     return HttpResponse("This is the month of june!") 
# def index7(request):
#     return HttpResponse("This is the month of july!") 
# def index8(request):
#     return HttpResponse("This is the month of august!") 
# def index9(request):
#     return HttpResponse("This is the month of september!") 
# def index10(request):
#     return HttpResponse("This is the month of october!") 
# def index11(request):
#     return HttpResponse("This is the month of november!") 
# def index12(request):
#     return HttpResponse("This is the month of  "+ d +" !")  #just declared a variable and used it 
#NOTE:we can write different views like the above syntax also but it is too time consuming if we have more and more views on our website therefore we do it in differetnt
#  format as shown below:
def monthly_chalenges(request,month):           #syntax of arguments to the view function imp here
    if month=='january':
        chalenge_text="This is the ,month of january!"
    elif month=='february':
        chalenge_text="This is the ,month of february!"
    elif month=='march':
        chalenge_text="This is the ,month of march!"
    elif month=='april':
        chalenge_text="This is the ,month of april!"
    else:
        return HttpResponseNotFound("this month is not supported")          #this throws a error using similar concept like exception handling 
    
    #and so on we can write for other months too
    return HttpResponse(chalenge_text)