from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    due_date = serializers.DateField(required=False, allow_null=True)
    class Meta:
        model = Task
        fields = '__all__'
