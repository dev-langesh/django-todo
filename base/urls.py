from django.urls import path

from . import views

urlpatterns = [
    path('',views.getTodos,name='home'),
    path('create/',views.createTodo,name='create')
]