# Generated by Django 4.2.1 on 2023-06-30 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('WpSeller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('details', models.TextField(default='')),
                ('service', models.CharField(default='', max_length=50)),
                ('rated_by', models.CharField(default='', max_length=100)),
                ('user_id', models.PositiveIntegerField(null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WpSeller.portfolio')),
            ],
            options={
                'db_table': 'core_wprating_seller_rating',
            },
        ),
    ]
