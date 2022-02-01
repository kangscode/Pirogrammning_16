from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', view = views.review_list, name='list'),
    path('<int:pk>/', view=views.review_detail, name='detail'),
    path('create/', view=views.review_create, name='create'),
    path('<int:pk>/update', view=views.review_update, name='update'),
    path('<int:pk>/delete', view=views.review_delete, name='delete'),
]