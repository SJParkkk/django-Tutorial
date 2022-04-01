from django.contrib import admin
from django.core.management import templates
from django.urls import path, include
from django.views.generic import TemplateView

from myapp import views
urlpatterns = [
    path('', views.index, name="homepage"),
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('update/<id>', views.update),
    path('delete/', views.delete),
]
