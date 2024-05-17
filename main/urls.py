from django.urls import path
from main import views


urlpatterns = [
    path('counter', views.counter, name='counter'),

]