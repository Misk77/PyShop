from django.urls import path

from . import views

urlpatterns = [
    path('', views.misk_django_index),
    path('misk_django_aboutMe', views.misk_django_aboutMe)

]
