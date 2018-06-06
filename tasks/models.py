from django.db import models


class Persons(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'persons'


class TaskTypes(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_types'


class Tasks(models.Model):

    name = models.CharField(max_length=64)
    task_type = models.ForeignKey(TaskTypes, on_delete=models.SET(1))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'


class TaskAssign(models.Model):

    person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    class Meta:
        db_table = 'task_assign'

