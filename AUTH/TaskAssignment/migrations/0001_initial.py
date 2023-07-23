# Generated by Django 4.2.1 on 2023-06-25 07:16

import AUTH.TaskAssignment.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ModuleTaskManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWithModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'AUTH_TaskAssignment_UserWithModule',
            },
        ),
        migrations.CreateModel(
            name='UserWithRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='userimg/default.png', upload_to=AUTH.TaskAssignment.models.upload_location)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'AUTH_TaskAssignment_UserWithRole',
            },
        ),
        migrations.CreateModel(
            name='UserWithTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_task', models.BooleanField(default=False)),
                ('add_task', models.BooleanField(default=False)),
                ('edit_task', models.BooleanField(default=False)),
                ('delete_task', models.BooleanField(default=False)),
                ('print_task', models.BooleanField(default=False)),
                ('cancel_task', models.BooleanField(default=False)),
                ('reset_task', models.BooleanField(default=False)),
                ('find_task', models.BooleanField(default=False)),
                ('save_task', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModuleTaskManagement.task')),
            ],
            options={
                'db_table': 'AUTH_TaskAssignment_UserWithTask',
            },
        ),
    ]
