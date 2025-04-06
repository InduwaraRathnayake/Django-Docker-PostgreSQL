from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_users, name='get_all_users'),
    path('<str:id>/', views.get_user_by_id, name='get_user_by_id'),
    path('create/', views.create_user, name='create_user'),
    path('update/<str:id>/', views.update_user, name='update_user'),
    path('delete/<str:id>/', views.delete_user, name='delete_user'),
]