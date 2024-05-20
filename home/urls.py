from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('student/', views.student, name = 'student'),
    path('card/', views.card, name = 'card'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
]
