from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Main post list
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Post detail view
]