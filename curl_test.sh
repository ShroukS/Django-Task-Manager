echo "Adding New Task"
curl -X POST http://localhost:8000/api/tasks/ \
     -H "Content-Type: application/json" \
     -d '{
            "title": "CURL Task",
            "description": "Task added by CURL command",
            "due_date": "2025-05-20",
            "priority": "M",
            "completed": false
          }'
echo
echo

echo "Getting tasks from the database..."
curl -X GET http://localhost:8000/api/tasks/

echo