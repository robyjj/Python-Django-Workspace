from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('orm_tuts/', views.orm_tuts),
]
