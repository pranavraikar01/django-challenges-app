from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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


# #NOTE:we can write different views like the above syntax also but it is too time consuming if we have more and more views on our website therefore we do it in differetnt
# #  format as shown below:
# def monthly_chalenges_by_number(request,month):
#     return HttpResponse(month)                 #returns the month value 

# def monthly_chalenges(request,month):           #syntax of arguments to the view function imp here
#     if month=='january':
#         chalenge_text="This is the ,month of january!"
#     elif month=='february':
#         chalenge_text="This is the ,month of february!"
#     elif month=='march':
#         chalenge_text="This is the ,month of march!"
#     elif month=='april':
#         chalenge_text="This is the ,month of april!"
#     else:
#         return HttpResponseNotFound("this month is not supported")          #this throws a error using similar concept like exception handling 
    
#     #and so on we can write for other months too
#     return HttpResponse(chalenge_text)



# #NOTE: WE CAN WRITE THE ABOVE CODE MORE DYNAMICALLY AS SHOWN BELOW instead of creating a lot of elif statements use dictionary

# #first create dictionary in which key are the paths here it is months
# monthly_chalenges={
#     "january":"This is january",
#     "february":"this is february",
#     "march":"this is march",
#     "april":"this is april",
#     "may":"this is may",
#     "june":"this is june",
#     "july":"this is july",
#     "august":"this is august"
# }
# #if month is entyered as integer then this view is called
# def monthly_chalenge_by_number(request,month):
#     months=list(monthly_chalenges.keys())       #.keys gives the keys  from monthly_chalenges dictionary and they are stored in a list named months
#     if month>len(months):
#       return HttpResponseNotFound("invalid month")

#     redirect_month=months[month-1]             #the enterd number is then matched with the key number of dictioanry and its key i.e month_name is saved in redirect_month


#     # return HttpResponseRedirect("/chalenges/" + redirect_month)      #redirects to the monthly_chalenge view
#     redirect_path=reverse("month-chalenge",args=[redirect_month]) # the reverse function convets this to /chalenge/january thus our path is more dynamic now
#     return HttpResponseRedirect(redirect_path) 
    

# def monthly_chalenge(request,month):           #syntax of arguments to the view function imp here
#    try:
#     chalenge_text=monthly_chalenges[month]          #data from dictionary is fetched using its respective key
#     return HttpResponse(chalenge_text)
#    except:
#     return HttpResponseNotFound("this month doesnt exist")
    





#NOTE:ABOVE WE HAVE CREATED THE URLS FOR PRINTING DATA IN THE FORM OF STRING ON OUR WEB PAGE,BELOW WILL SHOW HTML PAGES ON OUR WEB PAGE USING DJANGO

#first create dictionary in which key are the paths here it is months
monthly_chalenges={
    "january":"This is january",
    "february":"this is february",
    "march":"this is march",
    "april":"this is april",
    "may":"this is may",
    "june":"this is june",
    "july":"this is july",
    "august":"this is august"
}

def index(request):
    list_items=""       #generates an empty string initially
    months=list(monthly_chalenges.keys()) 

    for month in months:
       capitalized_month=month.capitalize()
       month_path=reverse("month-chalenge",args=[month])
       list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"     #new link is genereated for every month on same page

    response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)




#if month is entyered as integer then this view is called
def monthly_chalenge_by_number(request,month):
    months=list(monthly_chalenges.keys())       #.keys gives the keys  from monthly_chalenges dictionary and they are stored in a list named months
    if month>len(months):
      return HttpResponseNotFound("invalid month")

    redirect_month=months[month-1]             #the enterd number is then matched with the key number of dictioanry and its key i.e month_name is saved in redirect_month


    # return HttpResponseRedirect("/chalenges/" + redirect_month)      #redirects to the monthly_chalenge view
    redirect_path=reverse("month-chalenge",args=[redirect_month]) # the reverse function convets this to /chalenge/january thus our path is more dynamic now
    return HttpResponseRedirect(redirect_path) 
    

def monthly_chalenge(request,month):           #syntax of arguments to the view function imp here
   try:
    chalenge_text=monthly_chalenges[month]          #data from dictionary is fetched using its respective key
    response_data=f"<h1>{chalenge_text}</h1>"
    return HttpResponse(chalenge_text)
   except:
    return HttpResponseNotFound("<h1>this month doesnt exist</h1>")