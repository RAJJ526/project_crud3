from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.index),
    path('add/', views.save_data),
    path('delete/<int:id>/', views.delete),
    path('update/<int:id>/', views.update),

]
