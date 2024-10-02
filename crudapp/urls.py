
from django import views
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.login, name='login'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('signup/', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('usercreate/', views.usercreate, name='usercreate'),
    path('home/', views.home, name='home'),
    path('edit_func/', views.edit_func, name='edit_func'),
    path('add_func/', views.add_func, name='add_func'),
    path('delete_fuc/', views.delete_fuc, name='delete_fuc'),
]
