
from . import views
from django.urls import path


urlpatterns=[
    path("january", views.index)    #i.e if i request /january then execute index function
]