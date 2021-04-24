from django.urls import path, include
from . import views
from rest_framework import routers
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('createCat', views.createCat, name='createCat'),

]