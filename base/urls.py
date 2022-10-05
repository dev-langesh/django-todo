from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.getTodos, name='home'),
    path('create/', views.createTodo, name='create'),
    path('edit/<int:pk>', views.editTodo, name='edit'),
    path('delete/<int:pk>', views.deleteTodo, name='delete'),

    # auth
    path("login/", views.loginUser, name='login'),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.register, name="register")


]
