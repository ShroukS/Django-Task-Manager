# Django-Task-Manager
A Task Management web application built with Django, designed to help manage tasks efficiently.This project focuses on clean functionality for learning CRUD operations, filtering, sorting, and exporting data.

## Features
### Phase 1: 
- Create Task: Add a new task with title, description, due date, priority, and completion status

- Edit Task: Update task details

- Delete Task: Remove task with confirmation

- Mark Task Complete/Incomplete: Toggle task's completion status

- Task List View: Display all tasks in a clean list view

- Filter by Completion Status: Filter tasks: All, Completed, Pending

- Sort Tasks: Sort by Priority (High > Medium > Low) and Due Date

- Export to CSV: Download the current task list as a .csv file

### Phase 2:
- Task Categories / Tags: Assign categories (e.g., Work, Personal) and filter tasks by category

- Task Search Bar: Search tasks by title or description

- Highlight Overdue Tasks: Visually indicate overdue or due-today tasks

- Bulk Actions: Select multiple tasks to delete or mark as complete at once

- Subtasks:Create subtasks linked to parent tasks

- Import Tasks from CSV: Upload CSV files to bulk import tasks

- Progress Tracker: Show completion percentage of all tasks
- Creating Restful API: GET request to retrieve a list of all tasks, and POST request to create a new task.

### Setup Instructions
1. Clone the repo:

>git clone https://github.com/ShroukS/taskmanager.git

>cd taskmanager

2. Create Virtual Environment:

>python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

3. Install Dependencies:

>pip install django

4. Apply Migrations:

>python manage.py migrate

5. Run the Development Server:

>python manage.py runserver

6. Access the App:

Visit: http://127.0.0.1:8000/
