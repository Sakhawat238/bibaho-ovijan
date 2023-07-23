# Generated by Django 4.2.1 on 2023-06-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('icon', models.ImageField(null=True, upload_to='')),
                ('seller_count', models.PositiveIntegerField(default=0)),
                ('visitor_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'core_wpservice_service',
            },
        ),
    ]
