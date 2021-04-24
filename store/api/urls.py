from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.index),
    path("create", views.store),
    path("<int:id>", views.show),
    path("edit/<int:id>", views.update),
    path("delete/<int:id>", views.destroy),
    path("create-token", obtain_auth_token),
    #path("signup", views.signup),

]