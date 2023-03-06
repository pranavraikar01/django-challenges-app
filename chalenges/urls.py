
from . import views
from django.urls import path


urlpatterns=[
    # path("january", views.index1),    #i.e if i request /january then execute index function
    # path("february",views.index2),
    # path("march",views.index3),
    # path("april",views.index4),
    # path("may",views.index5),
    # path("june",views.index6),
    # path("july",views.index7),
    # path("august",views.index8),
    # path("september",views.index9),
    # path("october",views.index10),
    # path("november",views.index11),
    # path("december",views.index12),


# #NOTE:we can write different urls like the above syntax also but it is too time consuming if we have more and more views on our website therefore we do it in differetnt
# #  format as shown below:
#     path("<int:month>",views.monthly_chalenges_by_number),        #i.e first url will check number if yes then it will call number vala view
#     path("<str:month>",views.monthly_chalenges)         #<name_of_path_which_is_dynamic>   this is used to create dynamic path segments
     


#NOTE:we can write different urls like the above syntax also but it is too time consuming if we have more and more views on our website therefore we do it in differetnt
#  format as shown below it is same as above but used for dynamic paths using dictionary in views therefore written it again here:
    path("<int:month>",views.monthly_chalenge_by_number),        #i.e first url will check number if yes then it will call number vala view
    path("<str:month>",views.monthly_chalenge)         #<name_of_path_which_is_dynamic>   this is used to create dynamic path segments

]