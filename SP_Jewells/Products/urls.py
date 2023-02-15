from django.shortcuts import redirect
from django.urls import path
from . import views
urlpatterns = [
    path('product/',views.index,name='index'),
]