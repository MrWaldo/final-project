# Generated by Django 4.0.1 on 2022-01-31 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_delete_usuario_task_coment_task_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('ToDo', 'ToDo'), ('In Progres', 'In Progres'), ('Done', 'Done'), ('Close', 'Close')], default='ToDo', max_length=10),
        ),
    ]