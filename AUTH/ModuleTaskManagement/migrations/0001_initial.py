# Generated by Django 4.2.1 on 2023-06-25 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('url', models.CharField(blank=True, default='', max_length=100)),
                ('order', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='modules/')),
                ('is_archived', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'AUTH_ModuleTaskManagement_Module',
            },
        ),
        migrations.CreateModel(
            name='SubModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('order', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sub-modules/')),
                ('module_type', models.CharField(blank=True, choices=[('default', 'Default'), ('configuration', 'Configuration'), ('reports', 'Reports'), ('operation', 'Operation')], max_length=30, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModuleTaskManagement.module')),
            ],
            options={
                'db_table': 'AUTH_ModuleTaskManagement_SubModule',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('order', models.IntegerField(null=True)),
                ('task_url', models.CharField(blank=True, default='', max_length=50)),
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
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModuleTaskManagement.submodule')),
            ],
            options={
                'db_table': 'AUTH_ModuleTaskManagement_Task',
                'ordering': ['order'],
            },
        ),
    ]
