from ast import Delete
from django.contrib import admin
from django.urls import path
from myapp.views import home, login, sign, add, signout, delete_todo,change_todo

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('signup', sign),
    path('add-todo/',add),
    path('delete-todo/<int:id>' ,delete_todo),
    path('change-status/<int:id>/<str:status>' ,change_todo),
    path('logout', signout)
    ]
