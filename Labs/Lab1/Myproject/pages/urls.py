from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('R', views.R, name='index'),
    path('index2', views.index2, name='index'),
    path('index_include', views.index_include, name='index'),

]