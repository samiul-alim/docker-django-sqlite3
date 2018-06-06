from django.contrib import admin
from tasks.models import Persons, TaskTypes, Tasks, TaskAssign


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TaskTypes)
class TaskTypesAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    fields = ('name', 'task_type')
    list_display = ('id', 'name', 'task_type')


@admin.register(TaskAssign)
class TaskAssignAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'task')

