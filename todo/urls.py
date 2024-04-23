from django.urls import path

from .views import*

urlpatterns = [
    # URL pattern for the task list page
    path('',task_list, name='task_list'),
    # URL pattern for adding a new task
    path('add/', add_task, name='add_task'),
    # URL pattern for marking a task as completed
    path('complete/<int:task_id>/', mark_completed, name='mark_completed'),
    # URL pattern for deleting a task
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
