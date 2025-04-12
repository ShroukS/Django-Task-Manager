from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils.timezone import now
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
import csv
from django.contrib import messages
from .forms import CSVImportForm
from datetime import datetime
from rest_framework import generics
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def import_csv(request):
    if request.method == "POST":
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            decoded_file = file.read().decode("utf-8").splitlines()
            reader = csv.reader(decoded_file)

            next(reader)  # Skip header row if present

            for row in reader:
                try:
                    title = row[0]
                    description = row[1]
                    due_date = datetime.strptime(row[2], "%Y-%m-%d").date() if row[2] else None
                    priority = row[3] if row[3] in ['L', 'M', 'H'] else 'M'
                    completed = row[4].strip().lower() in ["true", "1", "yes"]

                    Task.objects.create(
                        title=title,
                        description=description,
                        due_date=due_date,
                        priority=priority,
                        completed=completed
                    )
                except Exception as e:
                    messages.error(request, f"Error processing row: {row} - {str(e)}")

            messages.success(request, "Tasks imported successfully!")
            return redirect("task_list")

    else:
        form = CSVImportForm()

    return render(request, "tasks/import_csv.html", {"form": form})


def bulk_actions(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        selected_tasks = request.POST.getlist('selected_tasks')
        
        if action == 'complete':
            Task.objects.filter(id__in=selected_tasks).update(completed=True)
        elif action == 'delete':
            Task.objects.filter(id__in=selected_tasks).delete()
        
        return redirect('task_list')  # Redirect back to the task list page
    return HttpResponse("Invalid request method.", status=405)


def calculate_completion_percentage():
    # Retrieve all parent tasks
    parent_tasks = Task.objects.filter(parent_task__isnull=True)
    total_weight = 0
    completed_weight = 0

    for parent in parent_tasks:
        # Retrieve all subtasks for the current parent task
        subtasks = parent.subtasks.all()
        num_subtasks = subtasks.count()

        if num_subtasks == 0:
            # No subtasks: parent task counts as 1 unit
            total_weight += 1
            if parent.completed:
                completed_weight += 1
        else:
            # With subtasks: each subtask contributes equally, parent contributes based on subtask completion
            subtask_weight = 1 / (num_subtasks + 1)
            parent_completed = parent.completed
            all_subtasks_completed = True
            for subtask in subtasks:
                total_weight += subtask_weight
                if subtask.completed:
                    completed_weight += subtask_weight
                else:
                    all_subtasks_completed = False
            # Parent task contributes its share only if all subtasks are completed
            total_weight += subtask_weight
            #if parent_completed and all_subtasks_completed:
            completed_weight += subtask_weight
                

    if total_weight == 0:
        return 0
    return (completed_weight / total_weight) * 100

# Task List View
def task_list(request):
    category_filter = request.GET.get('category', '')
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort_by', '')

    tasks = Task.objects.filter(parent_task__isnull=True) 

    if category_filter:
        tasks = tasks.filter(category=category_filter)

    if status_filter:
        tasks = tasks.filter(completed=True if status_filter == "completed" else False)

    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    # Apply sorting
    if sort_by:
        if sort_by == "priority":
            priority_order = {'H': 1, 'M': 2, 'L': 3}
            tasks = sorted(tasks, key=lambda t: priority_order.get(t.priority, 2))  # Sort manually for priority
        else:
            tasks = tasks.order_by(sort_by)

    # Add overdue status for each task
    today = now().date()
    for task in tasks:
        if task.due_date:
            if task.due_date < today:
                task.overdue = True
            elif task.due_date == today:
                task.due_today = True
            else:
                task.overdue = False
                task.due_today = False
    
    completion_percentage = calculate_completion_percentage()

    #total_tasks = tasks.count()
    #completed_tasks = tasks.filter(completed=True).count()
    #print(f"total tasks: {total_tasks}")
    #print(f"completed tasks: {completed_tasks}")
    #if total_tasks > 0:
    #    completion_percentage = (completed_tasks / total_tasks) * 100
    #else:
    #    completion_percentage = 0

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'categories': Task.CATEGORY_CHOICES,
        'search_query': search_query,  # Keep search query visible in input
        'category_filter': category_filter,
        'status_filter': status_filter,
        'sort_by': sort_by,
        'completion_percentage': completion_percentage
    })


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
