# Generated by Django 4.2.1 on 2023-06-25 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TaskAssignment', '0001_initial'),
        ('ModuleTaskManagement', '0001_initial'),
        ('RoleCreation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwithtask',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userwithrole',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RoleCreation.role'),
        ),
        migrations.AddField(
            model_name='userwithrole',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userwithmodule',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModuleTaskManagement.module'),
        ),
        migrations.AddField(
            model_name='userwithmodule',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]