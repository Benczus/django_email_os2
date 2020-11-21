from django.urls import path

from email_test import views

urlpatterns = [
    path('sleep/', views.email)

]