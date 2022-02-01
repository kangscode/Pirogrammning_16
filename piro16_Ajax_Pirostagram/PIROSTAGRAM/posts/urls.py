from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('delete_ajax/', views.delete_ajax, name='delete_ajax'),
    path('post_ajax/', views.post_ajax, name='post_ajax'),


]
