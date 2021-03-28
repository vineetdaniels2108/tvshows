from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('show', views.index),
    path('show/new', views.add_show_page),
    path('show/create', views.add_show),
    path('show/<int:show_id>', views.show),
    path('show/<int:show_id>/edit', views.show_edit_page),
    path('show/<int:show_id>/update', views.edit_show), 
    path('show/<int:show_id>/destroy', views.delete_show)
]