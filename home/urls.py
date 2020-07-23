from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('createUser', views.newUser),
    path('create', views.create),
    path('login', views.login),
    path('logout', views.logout),
]