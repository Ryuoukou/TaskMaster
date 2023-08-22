# Generated by Django 4.2 on 2023-08-21 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execution_date', models.DateField()),
                ('completion_time', models.PositiveIntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_management.task')),
            ],
        ),
    ]
