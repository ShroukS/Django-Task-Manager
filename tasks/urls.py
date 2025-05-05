from django.urls import path, include
from . import views
from .views import import_csv
from .views import TaskListCreateView, TaskDetailView


urlpatterns = [
    path("import_csv/", import_csv, name="import_csv"),
    path('', views.task_list, name='task_list'),
    path('bulk-actions/', views.bulk_actions, name='bulk_actions'),
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('toggle/<int:pk>/', views.task_toggle_complete, name='task_toggle'),
    path('export/', views.export_tasks_csv, name='export_tasks_csv'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
