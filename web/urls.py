from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.show_list, name = 'show_list'),
    path('register/',views.register, name = 'register')
]