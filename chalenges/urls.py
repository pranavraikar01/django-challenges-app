
from . import views
from django.urls import path


urlpatterns=[
    path("january", views.index1),    #i.e if i request /january then execute index function
    path("february",views.index2),
    path("march",views.index3),
    path("april",views.index4),
    path("may",views.index5),
    path("june",views.index6),
    path("july",views.index7),
    path("august",views.index8),
    path("september",views.index9),
    path("october",views.index10),
    path("november",views.index11),
    path("december",views.index12),
]