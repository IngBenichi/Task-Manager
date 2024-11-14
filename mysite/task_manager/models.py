from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=1)
    tags = models.CharField(max_length=255, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=1)
    tags = models.CharField(max_length=255, blank=True) 
    parent_task = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="subtasks")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
