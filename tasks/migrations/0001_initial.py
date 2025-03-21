# Generated by Django 5.1.7 on 2025-03-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='M', max_length=1)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
