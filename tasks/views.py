from django.shortcuts import render, HttpResponse
from tasks.models import Persons, TaskTypes, Tasks, TaskAssign


class TaskView:

    def task_index(request):
        tasks = TaskAssign.objects.all()
        return render(request, 'tasks/tasks.html', dict(title='Tasks', tasks=tasks))
