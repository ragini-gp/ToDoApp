from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update/<str:primary_k>',views.update,name="update"),
    path('delete/<str:primary_k>',views.delete,name="delete")
]
