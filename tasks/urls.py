# from django.conf.urls import url
from django.urls import path
from tasks.views import TaskView


urlpatterns = [
    path('', TaskView.task_index, name='task-index'),
]
