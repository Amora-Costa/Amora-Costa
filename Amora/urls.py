from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("register",views.register,name='register'),
    path('faq_submit',views.faq_submit, name='faq_submit')
]