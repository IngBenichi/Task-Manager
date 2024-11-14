from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('create_project/', views.create_project, name='create_project'),
    path('create_task/', views.create_task, name='create_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
]
