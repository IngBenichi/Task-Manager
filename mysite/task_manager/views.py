from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Project, Task
import json



def index(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    return render(request, 'index.html', {'projects': projects, 'tasks': tasks})


@csrf_exempt
def create_project(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description', '')
        due_date = data.get('due_date', None)
        priority = data.get('priority', 1)
        tags = data.get('tags', '')

        project = Project.objects.create(
            name=name,
            description=description,
            due_date=due_date,
            priority=priority,
            tags=tags
        )

        return JsonResponse({
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'due_date': project.due_date,
            'priority': project.priority,
            'tags': project.tags
        })


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_id = data.get('project_id')
        name = data.get('name')
        description = data.get('description', '')
        due_date = data.get('due_date', None)
        priority = data.get('priority', 1)
        tags = data.get('tags', '')
        parent_task_id = data.get('parent_task_id', None)

        project = Project.objects.get(id=project_id)
        parent_task = Task.objects.get(id=parent_task_id) if parent_task_id else None

        task = Task.objects.create(
            project=project,
            name=name,
            description=description,
            due_date=due_date,
            priority=priority,
            tags=tags,
            parent_task=parent_task
        )

        return JsonResponse({
            'id': task.id,
            'name': task.name,
            'description': task.description,
            'due_date': task.due_date,
            'priority': task.priority,
            'tags': task.tags
        })


@csrf_exempt
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return JsonResponse({'success': True})


@csrf_exempt
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    return JsonResponse({'success': True})
