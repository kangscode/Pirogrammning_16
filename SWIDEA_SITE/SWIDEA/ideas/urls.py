from os import name
from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', view = views.idea_list, name='idea_list'),
    path('idea_create/', view = views.idea_create, name='idea_create'),
    path('<int:pk>/', view=views.idea_detail, name='idea_detail'),
    path('<int:pk>/idea_update', view=views.idea_update, name='idea_update'),
    path('<int:pk>/idea_delete', view=views.idea_delete, name='idea_delete'),
    path('devt_list', view = views.devt_list, name='devt_list' ),
    path('devt_create/', view=views.devt_create, name='devt_create'),
    path('<int:pk>/devt_detail', view=views.devt_detail, name='devt_detail'),
    path('<int:pk>/devt_update', view=views.devt_update, name='devt_update'),
    path('<int:pk>/devt_delete', view=views.devt_delete, name='devt_delete'),


]