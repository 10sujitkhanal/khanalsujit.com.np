import imp
from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path('add/',views.addContact,name = "add-contact"),
]