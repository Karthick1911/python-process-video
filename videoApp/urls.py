from django.urls import path
from . import views

urlpatterns = [ path('list/', views.showAll, name="video-list"), path('create', views.save, name="video-create") ]