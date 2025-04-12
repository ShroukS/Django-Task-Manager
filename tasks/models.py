from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Study', 'Study'),
        ('Other', 'Other'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

        # New field for subtasks
    parent_task = models.ForeignKey(
        'self',  # This makes the field reference the same model (Task)
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subtasks'  # Enables easy access to related subtasks
    )

    def __str__(self):
        return self.title
