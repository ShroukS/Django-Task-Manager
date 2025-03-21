from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
import csv

# Task List View
def task_list(request):
    tasks = Task.objects.all()

    # Filtering
    filter_status = request.GET.get('status')
    if filter_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_status == 'pending':
        tasks = tasks.filter(completed=False)

    # Sorting
    sort_by = request.GET.get('sort')
    if sort_by == 'priority':
        priority_order = {'H': 0, 'M': 1, 'L': 2}  # Custom order: High > Medium > Low
        tasks = sorted(tasks, key=lambda t: priority_order[t.priority])
    elif sort_by == 'due_date':
        tasks = tasks.order_by('due_date')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Create Task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Edit Task
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Delete Task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Toggle Complete/Incomplete
def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

# Export to CSV
def export_tasks_csv(request):
    tasks = Task.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks.csv"'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Due Date', 'Priority', 'Completed'])
    for task in tasks:
        writer.writerow([task.title, task.description, task.due_date, task.priority, task.completed])
    return response
