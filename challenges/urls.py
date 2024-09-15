from django.urls import path
from .import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge_by_String, name = "Month_ka_Challenge"),
    #We are using name function here because we don't want to change the url everywhere 
    # we can access by using this name of str:month urls in views.py file
    path("", views.index)
    # this path will conclude http://127.0.0.1:8000/challenge/ this url too it will not give error 404

]

