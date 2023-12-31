from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('book_search/', views.book_search, name="book_search"),
]