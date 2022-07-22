from django.contrib import admin
from django.urls import path
from .webscrap import webscraping

urlpatterns = [
    path("webstraping/", webscraping, name="webscraping"),
]
