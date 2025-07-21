from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

urlpatterns = [
    path('', lambda request: HttpResponse('Example')),  # placeholder
]
