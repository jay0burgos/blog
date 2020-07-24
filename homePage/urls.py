from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('post', views.create),
    path('logout', views.logout),
    path('comment', views.newComment)
]

