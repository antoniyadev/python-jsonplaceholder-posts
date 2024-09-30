from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.index, name='posts_index'),
    path('posts/<int:post_id>/', views.show, name='posts_show'),
]
