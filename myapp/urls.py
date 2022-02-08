from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('' , views.index , name='index'),
    path("about/" , views.about , name='about'),
    path("rooms/" , views.rooms , name='rooms'),
    path("dives/" , views.dives , name='dives'),
    path("foods/" , views.food , name='foods'),
    path("news/" , views.news , name='news'),
    path("contact/" , views.contact , name='contact'),
]
